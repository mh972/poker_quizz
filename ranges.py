"""
GTO-adapted preflop ranges for 6-max NL.
Based on modern solver outputs, tuned for NL10-NL50 live/online play.

Positions: UTG, HJ, CO, BTN, SB, BB
Scenarios: RFI, vs_rfi (call/3bet), BB_defense
"""

# ---------------------------------------------------------------------------
# RFI (Raise First In) — open or fold
# ---------------------------------------------------------------------------

RFI = {
    # ~14% — tight, only strong hands and good connected/suited broadways
    "UTG": [
        "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",
        "AKs","AQs","AJs","ATs","A5s","A4s",
        "AKo","AQo","AJo",
        "KQs","KJs","KTs",
        "QJs","QTs",
        "JTs","T9s","98s","87s","76s","65s",
    ],

    # ~18% — add more Ax suited, open up some offsuit broadways
    "HJ": [
        "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",
        "AKs","AQs","AJs","ATs","A9s","A8s","A5s","A4s","A3s",
        "AKo","AQo","AJo","ATo",
        "KQs","KJs","KTs","K9s",
        "KQo",
        "QJs","QTs","Q9s",
        "JTs","J9s",
        "T9s","T8s","98s","87s","76s","65s","54s",
    ],

    # ~26% — add weaker Ax, Kx suited, more connected hands
    "CO": [
        "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",
        "AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s",
        "AKo","AQo","AJo","ATo","A9o","A8o",
        "KQs","KJs","KTs","K9s","K8s",
        "KQo","KJo","KTo",
        "QJs","QTs","Q9s","Q8s",
        "QJo",
        "JTs","J9s","J8s",
        "T9s","T8s","T7s",
        "98s","97s","87s","86s","76s","75s","65s","64s","54s","53s",
    ],

    # ~42% — near-button open, exploit fold equity vs blinds
    "BTN": [
        "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",
        "AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s",
        "AKo","AQo","AJo","ATo","A9o","A8o","A7o","A6o","A5o","A4o",
        "KQs","KJs","KTs","K9s","K8s","K7s","K6s","K5s",
        "KQo","KJo","KTo","K9o",
        "QJs","QTs","Q9s","Q8s","Q7s",
        "QJo","QTo","Q9o",
        "JTs","J9s","J8s","J7s",
        "JTo","J9o",
        "T9s","T8s","T7s","T6s",
        "T9o",
        "98s","97s","96s","87s","86s","85s","76s","75s","74s","65s","64s","54s","53s","43s",
    ],

    # ~35% — playing OOP vs BB, need stronger hands than BTN
    "SB": [
        "AA","KK","QQ","JJ","TT","99","88","77","66","55","44","33","22",
        "AKs","AQs","AJs","ATs","A9s","A8s","A7s","A6s","A5s","A4s","A3s","A2s",
        "AKo","AQo","AJo","ATo","A9o","A8o","A7o",
        "KQs","KJs","KTs","K9s","K8s","K7s","K6s",
        "KQo","KJo","KTo","K9o",
        "QJs","QTs","Q9s","Q8s",
        "QJo","QTo",
        "JTs","J9s","J8s",
        "JTo",
        "T9s","T8s","T7s",
        "98s","97s","87s","86s","76s","75s","65s","64s","54s","53s",
    ],
}

# ---------------------------------------------------------------------------
# vs RFI: for each (hero_pos, villain_pos), hands split into 3bet / call / fold
# Fold = everything not in 3bet or call
# ---------------------------------------------------------------------------

VS_RFI = {

    # --- HJ facing UTG open ---
    "HJ_vs_UTG": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AJs","AKo","AQo",
            "A5s","A4s",  # polarized bluffs
        ],
        "call": [
            "TT","99","88","77","66","55",
            "ATs","A9s",
            "KQs","KJs","KTs",
            "QJs","QTs",
            "JTs","T9s","98s","87s","76s",
        ],
    },

    # --- CO facing UTG open ---
    "CO_vs_UTG": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AKo","AQo",
            "A5s","A4s",
        ],
        "call": [
            "TT","99","88","77","66","55",
            "AJs","ATs","A9s",
            "KQs","KJs","KTs",
            "QJs","QTs",
            "JTs","T9s","98s","87s","76s","65s",
        ],
    },

    # --- CO facing HJ open ---
    "CO_vs_HJ": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AJs","AKo","AQo",
            "A5s","A4s","A3s",
        ],
        "call": [
            "TT","99","88","77","66","55","44",
            "ATs","A9s","A8s",
            "KQs","KJs","KTs","K9s",
            "QJs","QTs","Q9s",
            "JTs","J9s","T9s","T8s","98s","87s","76s","65s","54s",
        ],
    },

    # --- BTN facing UTG open ---
    "BTN_vs_UTG": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AKo","AQo",
            "A5s","A4s",
        ],
        "call": [
            "TT","99","88","77","66","55",
            "AJs","ATs","A9s",
            "KQs","KJs","KTs",
            "QJs","QTs",
            "JTs","T9s","98s","87s","76s","65s",
        ],
    },

    # --- BTN facing HJ open ---
    "BTN_vs_HJ": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AJs","AKo","AQo","AJo",
            "A5s","A4s","A3s",
        ],
        "call": [
            "TT","99","88","77","66","55","44",
            "ATs","A9s","A8s",
            "KQs","KJs","KTs","K9s",
            "QJs","QTs","Q9s",
            "JTs","J9s","T9s","T8s","98s","97s","87s","76s","65s","54s",
        ],
    },

    # --- BTN facing CO open ---
    "BTN_vs_CO": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","ATs","AKo","AQo","AJo",
            "A5s","A4s","A3s","A2s",
            "KQs",
        ],
        "call": [
            "99","88","77","66","55","44","33",
            "A9s","A8s","A7s",
            "KJs","KTs","K9s",
            "QJs","QTs","Q9s","Q8s",
            "JTs","J9s","J8s",
            "T9s","T8s","98s","97s","87s","86s","76s","75s","65s","64s","54s",
        ],
    },

    # --- SB facing BTN open ---
    "SB_vs_BTN": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","ATs","AKo","AQo","AJo",
            "A5s","A4s","A3s","A2s",
            "KQs","K5s","K4s",
        ],
        "call": [
            "99","88","77","66","55","44","33","22",
            "A9s","A8s","A7s","A6s",
            "KJs","KTs","K9s","K8s","K7s","K6s",
            "QJs","QTs","Q9s","Q8s",
            "JTs","J9s","J8s",
            "T9s","T8s","T7s",
            "98s","97s","87s","86s","76s","75s","65s","64s","54s","53s",
        ],
    },

    # --- SB facing CO open ---
    "SB_vs_CO": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","AKo","AQo","AJo",
            "A5s","A4s","A3s",
            "KQs",
        ],
        "call": [
            "99","88","77","66","55","44","33","22",
            "ATs","A9s","A8s","A7s",
            "KJs","KTs","K9s","K8s",
            "QJs","QTs","Q9s",
            "JTs","J9s","T9s","T8s","98s","87s","76s","65s","54s",
        ],
    },

    # --- BB facing BTN open ---
    "BB_vs_BTN": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","ATs","AKo","AQo","AJo",
            "A5s","A4s","A3s","A2s",
            "KQs","K5s","K4s","K3s",
            "76s","65s","54s",
        ],
        "call": [
            "99","88","77","66","55","44","33","22",
            "A9s","A8s","A7s","A6s",
            "ATo","A9o","A8o","A7o",
            "KJs","KTs","K9s","K8s","K7s","K6s",
            "KQo","KJo","KTo","K9o",
            "QJs","QTs","Q9s","Q8s","Q7s",
            "QJo","QTo","Q9o",
            "JTs","J9s","J8s","J7s",
            "JTo","J9o",
            "T9s","T8s","T7s","T6s",
            "T9o",
            "98s","97s","96s","87s","86s","85s","75s","74s","64s","63s","53s","43s",
        ],
    },

    # --- BB facing CO open ---
    "BB_vs_CO": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","AKo","AQo","AJo",
            "A5s","A4s","A3s",
            "KQs",
        ],
        "call": [
            "99","88","77","66","55","44","33","22",
            "ATs","A9s","A8s","A7s","A6s","A2s",
            "ATo","A9o","A8o",
            "KJs","KTs","K9s","K8s","K7s",
            "KQo","KJo","KTo",
            "QJs","QTs","Q9s","Q8s",
            "QJo","QTo",
            "JTs","J9s","J8s",
            "JTo",
            "T9s","T8s","T7s",
            "98s","97s","87s","86s","76s","75s","65s","64s","54s","53s",
        ],
    },

    # --- BB facing HJ open ---
    "BB_vs_HJ": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AJs","AKo","AQo","AJo",
            "A5s","A4s","A3s",
        ],
        "call": [
            "TT","99","88","77","66","55","44","33","22",
            "ATs","A9s","A8s","A7s","A6s",
            "ATo","A9o",
            "KQs","KJs","KTs","K9s","K8s",
            "KQo","KJo","KTo",
            "QJs","QTs","Q9s","Q8s",
            "QJo",
            "JTs","J9s","J8s",
            "T9s","T8s","T7s",
            "98s","97s","87s","86s","76s","75s","65s","54s",
        ],
    },

    # --- BB facing UTG open ---
    "BB_vs_UTG": {
        "3bet": [
            "AA","KK","QQ","JJ",
            "AKs","AQs","AKo","AQo",
            "A5s","A4s",
        ],
        "call": [
            "TT","99","88","77","66","55","44","33","22",
            "AJs","ATs","A9s","A8s","A3s","A2s",
            "KQs","KJs","KTs",
            "QJs","QTs",
            "JTs","J9s",
            "T9s","T8s","98s","87s","76s","65s","54s",
        ],
    },

    # --- BB facing SB open ---
    "BB_vs_SB": {
        "3bet": [
            "AA","KK","QQ","JJ","TT",
            "AKs","AQs","AJs","ATs","AKo","AQo","AJo","ATo",
            "A5s","A4s","A3s","A2s",
            "KQs","K5s","K4s",
            "QJs","Q8s",
            "76s","65s","54s","43s",
        ],
        "call": [
            "99","88","77","66","55","44","33","22",
            "A9s","A8s","A7s","A6s",
            "A9o","A8o","A7o","A6o","A5o",
            "KJs","KTs","K9s","K8s","K7s","K6s","K5s",
            "KQo","KJo","KTo","K9o","K8o",
            "QTs","Q9s","Q7s","Q6s",
            "QJo","QTo","Q9o",
            "JTs","J9s","J8s","J7s",
            "JTo","J9o",
            "T9s","T8s","T7s","T6s",
            "T9o",
            "98s","97s","96s","87s","86s","85s","75s","74s","64s","63s","53s","42s",
        ],
    },
}

# ---------------------------------------------------------------------------
# Helper: all 169 hand types
# ---------------------------------------------------------------------------

RANKS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

ALL_HANDS = []
for i, r1 in enumerate(RANKS):
    for j, r2 in enumerate(RANKS):
        if i < j:
            ALL_HANDS.append(r1 + r2 + "s")  # suited
            ALL_HANDS.append(r1 + r2 + "o")  # offsuit
        elif i == j:
            ALL_HANDS.append(r1 + r2)         # pair


def get_action(hand: str, scenario_key: str) -> str:
    """Return GTO-adapted action: '3bet', 'call', 'open', or 'fold'."""
    # RFI scenario
    if scenario_key in RFI:
        return "open" if hand in RFI[scenario_key] else "fold"

    # vs-RFI scenario
    if scenario_key in VS_RFI:
        data = VS_RFI[scenario_key]
        if hand in data["3bet"]:
            return "3bet"
        if hand in data["call"]:
            return "call"
        return "fold"

    return "fold"


def get_rfi_scenarios():
    return list(RFI.keys())


def get_vs_rfi_scenarios():
    return list(VS_RFI.keys())


def label_scenario(key: str) -> str:
    """Human-readable label for a scenario key."""
    if key in RFI:
        labels = {
            "UTG": "UTG — first to act",
            "HJ": "HJ — first to act",
            "CO": "CO — first to act",
            "BTN": "BTN — first to act",
            "SB": "SB — first to act (vs BB)",
        }
        return labels.get(key, key)

    if key in VS_RFI:
        parts = key.split("_vs_")
        hero, villain = parts[0], parts[1]
        return f"{hero} vs {villain} open"

    return key
