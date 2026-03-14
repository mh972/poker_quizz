"""SQLite persistence layer for quiz progress tracking."""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "progress.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS decisions (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                ts        DATETIME DEFAULT CURRENT_TIMESTAMP,
                scenario  TEXT NOT NULL,
                hand      TEXT NOT NULL,
                action    TEXT NOT NULL,
                correct   TEXT NOT NULL,
                is_right  INTEGER NOT NULL
            )
        """)
        conn.commit()


def log_decision(scenario: str, hand: str, action: str, correct: str):
    is_right = 1 if action == correct else 0
    with get_db() as conn:
        conn.execute(
            "INSERT INTO decisions (scenario, hand, action, correct, is_right) VALUES (?,?,?,?,?)",
            (scenario, hand, action, correct, is_right),
        )
        conn.commit()
    return is_right


def get_stats():
    with get_db() as conn:
        total = conn.execute("SELECT COUNT(*) FROM decisions").fetchone()[0]
        correct = conn.execute("SELECT COUNT(*) FROM decisions WHERE is_right=1").fetchone()[0]

        by_scenario = conn.execute("""
            SELECT scenario,
                   COUNT(*) as total,
                   SUM(is_right) as correct
            FROM decisions
            GROUP BY scenario
            ORDER BY (1.0 * SUM(is_right) / COUNT(*)) ASC
        """).fetchall()

        recent = conn.execute("""
            SELECT scenario, hand, action, correct, is_right, ts
            FROM decisions
            ORDER BY id DESC
            LIMIT 20
        """).fetchall()

    return {
        "total": total,
        "correct": correct,
        "pct": round(correct / total * 100, 1) if total else 0,
        "by_scenario": [dict(r) for r in by_scenario],
        "recent": [dict(r) for r in recent],
    }
