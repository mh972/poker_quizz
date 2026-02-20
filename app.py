"""Flask application — GTO Preflop Trainer."""

import random
from flask import Flask, render_template, request, jsonify

import database as db
import ranges as rng

app = Flask(__name__)


def random_question():
    """Pick a random scenario + hand and return the question dict."""
    # 40% RFI, 60% vs-RFI (more interesting decision trees)
    mode = random.choices(["rfi", "vs_rfi"], weights=[40, 60])[0]

    if mode == "rfi":
        scenario = random.choice(rng.get_rfi_scenarios())
        hand = random.choice(rng.ALL_HANDS)
        correct = rng.get_action(hand, scenario)
        actions = ["open", "fold"]
        return {
            "mode": "rfi",
            "scenario": scenario,
            "hand": hand,
            "correct": correct,
            "actions": actions,
            "label": rng.label_scenario(scenario),
        }
    else:
        scenario = random.choice(rng.get_vs_rfi_scenarios())
        hand = random.choice(rng.ALL_HANDS)
        correct = rng.get_action(hand, scenario)
        actions = ["3bet", "call", "fold"]
        return {
            "mode": "vs_rfi",
            "scenario": scenario,
            "hand": hand,
            "correct": correct,
            "actions": actions,
            "label": rng.label_scenario(scenario),
        }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


@app.route("/dashboard")
def dashboard():
    stats = db.get_stats()
    return render_template("dashboard.html", stats=stats)


@app.route("/api/question")
def api_question():
    q = random_question()
    # Don't send correct answer to client
    return jsonify({
        "scenario": q["scenario"],
        "hand": q["hand"],
        "actions": q["actions"],
        "label": q["label"],
        "mode": q["mode"],
    })


@app.route("/api/answer", methods=["POST"])
def api_answer():
    data = request.get_json()
    scenario = data["scenario"]
    hand = data["hand"]
    action = data["action"]

    correct = rng.get_action(hand, scenario)
    is_right = db.log_decision(scenario, hand, action, correct)

    # Build explanation
    if scenario in rng.RFI:
        explanation = _explain_rfi(hand, scenario, correct)
    else:
        explanation = _explain_vs_rfi(hand, scenario, correct)

    return jsonify({
        "correct": correct,
        "is_right": bool(is_right),
        "explanation": explanation,
    })


@app.route("/api/stats")
def api_stats():
    return jsonify(db.get_stats())


def _explain_rfi(hand, scenario, correct):
    pos_pct = {
        "UTG": "~14%", "HJ": "~18%", "CO": "~26%", "BTN": "~42%", "SB": "~35%"
    }
    pct = pos_pct.get(scenario, "")
    if correct == "open":
        return f"{hand} is in the {scenario} opening range ({pct}). Open raise."
    else:
        return f"{hand} is not in the {scenario} opening range ({pct}). Fold."


def _explain_vs_rfi(hand, scenario, correct):
    parts = scenario.split("_vs_")
    hero, villain = parts[0], parts[1]
    if correct == "3bet":
        return f"{hand} is a 3-bet from {hero} vs {villain} open (value or bluff)."
    elif correct == "call":
        return f"{hand} calls from {hero} vs {villain} open — good implied odds / position."
    else:
        return f"{hand} folds from {hero} vs {villain} open — outside the defending range."


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True, port=5000)
