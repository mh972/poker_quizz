/* ============================================================
   GTO Preflop Trainer — Quiz logic
   ============================================================ */

const SUITS = ["s", "h", "d", "c"];
const SUIT_SYMBOLS = { s: "♠", h: "♥", d: "♦", c: "♣" };
const SUIT_COLOR   = { s: "card-black", h: "card-red", d: "card-red", c: "card-black" };
const RANKS = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"];

// Keyboard shortcuts per action
const ACTION_KEYS = { open: "o", fold: "f", call: "c", "3bet": "3" };

let current = null;
let answered = false;
let sessionTotal = 0;
let sessionCorrect = 0;
let streak = 0;

// ---------------------------------------------------------------------------
// Card rendering
// ---------------------------------------------------------------------------

function randomCard(usedCards) {
  let card;
  do {
    const rank = RANKS[Math.floor(Math.random() * RANKS.length)];
    const suit = SUITS[Math.floor(Math.random() * SUITS.length)];
    card = { rank, suit };
  } while (usedCards.some(c => c.rank === card.rank && c.suit === card.suit));
  usedCards.push(card);
  return card;
}

function cardsForHand(hand) {
  // hand = "AKs", "AKo", "AA", etc.
  const usedCards = [];
  let r1, r2, suited;

  if (hand.length === 2) {
    // pair — different suits
    r1 = hand[0]; r2 = hand[1];
    const s1 = SUITS[Math.floor(Math.random() * SUITS.length)];
    let s2;
    do { s2 = SUITS[Math.floor(Math.random() * SUITS.length)]; } while (s2 === s1);
    return [{ rank: r1, suit: s1 }, { rank: r2, suit: s2 }];
  }

  r1 = hand[0];
  r2 = hand[1];
  suited = hand[2] === "s";

  const s1 = SUITS[Math.floor(Math.random() * SUITS.length)];
  let s2;
  if (suited) {
    s2 = s1;
  } else {
    do { s2 = SUITS[Math.floor(Math.random() * SUITS.length)]; } while (s2 === s1);
  }
  return [{ rank: r1, suit: s1 }, { rank: r2, suit: s2 }];
}

function renderCard(el, card) {
  const color = SUIT_COLOR[card.suit];
  const sym   = SUIT_SYMBOLS[card.suit];
  el.innerHTML = `
    <span class="card-rank-top ${color}">${card.rank}</span>
    <span class="card-suit-center ${color}">${sym}</span>
    <span class="card-rank-bot ${color}">${card.rank}</span>
  `;
}

// ---------------------------------------------------------------------------
// Question flow
// ---------------------------------------------------------------------------

async function loadQuestion() {
  answered = false;
  document.getElementById("feedback-box").classList.add("hidden");
  document.getElementById("action-row").innerHTML = "";
  document.getElementById("hand-canonical").textContent = "";
  document.getElementById("scenario-label").textContent = "Loading…";
  document.getElementById("card1").innerHTML = "";
  document.getElementById("card2").innerHTML = "";

  const res = await fetch("/api/question");
  current = await res.json();

  // Render scenario
  document.getElementById("scenario-label").textContent = current.label;

  // Render cards
  const cards = cardsForHand(current.hand);
  renderCard(document.getElementById("card1"), cards[0]);
  renderCard(document.getElementById("card2"), cards[1]);
  document.getElementById("hand-canonical").textContent = current.hand;

  // Render action buttons
  const row = document.getElementById("action-row");
  current.actions.forEach(action => {
    const btn = document.createElement("button");
    const cssClass = action === "3bet" ? "tbbet" : action;
    btn.className = `action-btn ${cssClass}`;
    btn.textContent = action === "3bet" ? "3-Bet" : action.charAt(0).toUpperCase() + action.slice(1);
    btn.dataset.action = action;
    btn.onclick = () => submitAnswer(action);
    row.appendChild(btn);
  });

  // Keyboard hint
  let hint = document.querySelector(".kbd-hint");
  if (!hint) {
    hint = document.createElement("div");
    hint.className = "kbd-hint";
    document.querySelector(".quiz-main").insertBefore(hint, document.getElementById("feedback-box"));
  }
  const keys = current.actions.map(a => `<kbd>${ACTION_KEYS[a] || a[0]}</kbd> ${a}`).join(" · ");
  hint.innerHTML = keys;
}

async function submitAnswer(action) {
  if (answered) return;
  answered = true;

  const res = await fetch("/api/answer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      scenario: current.scenario,
      hand: current.hand,
      action,
    }),
  });
  const data = await res.json();

  // Update buttons
  const btns = document.querySelectorAll(".action-btn");
  btns.forEach(btn => {
    btn.disabled = true;
    const a = btn.dataset.action;
    if (a === data.correct) {
      btn.classList.add("result-correct");
    } else if (a === action && !data.is_right) {
      btn.classList.add("result-wrong");
    }
  });

  // Feedback
  sessionTotal++;
  if (data.is_right) {
    sessionCorrect++;
    streak++;
  } else {
    streak = 0;
  }
  updateStats();

  const box  = document.getElementById("feedback-box");
  const icon = document.getElementById("feedback-icon");
  const text = document.getElementById("feedback-text");
  const expl = document.getElementById("feedback-explanation");

  box.classList.remove("hidden");
  if (data.is_right) {
    icon.textContent = "✅";
    text.textContent = "Correct!";
    text.style.color = "var(--green)";
  } else {
    icon.textContent = "❌";
    text.textContent = `Wrong — correct action: ${data.correct.toUpperCase()}`;
    text.style.color = "var(--red)";
  }
  expl.textContent = data.explanation;
}

function nextQuestion() {
  loadQuestion();
}

function updateStats() {
  document.getElementById("stat-streak").textContent = `Streak: ${streak}`;
  document.getElementById("stat-session").textContent =
    `Session: ${sessionCorrect}/${sessionTotal} (${sessionTotal ? Math.round(sessionCorrect/sessionTotal*100) : 0}%)`;
}

// ---------------------------------------------------------------------------
// Keyboard shortcuts
// ---------------------------------------------------------------------------

document.addEventListener("keydown", (e) => {
  if (answered) {
    if (e.key === "Enter" || e.key === " " || e.key === "ArrowRight") {
      e.preventDefault();
      nextQuestion();
    }
    return;
  }
  if (!current) return;

  const map = {};
  current.actions.forEach(a => { map[ACTION_KEYS[a] || a[0]] = a; });
  const action = map[e.key.toLowerCase()];
  if (action) submitAnswer(action);
});

// ---------------------------------------------------------------------------
// Boot
// ---------------------------------------------------------------------------

loadQuestion();
