# GTO Preflop Trainer

Application web interactive pour s'entraîner aux décisions préflop GTO (Game Theory Optimal) en NL Texas Hold'em 6-max.

## Fonctionnement

À chaque main, l'app te présente :
- une **position** (UTG, HJ, CO, BTN, SB, BB)
- un **scénario** (RFI ou face à un open)
- une **main aléatoire**

Tu dois prendre la bonne décision — ouvrir, folder, caller ou 3-better — selon les ranges GTO adaptées aux stakes NL10-NL50.

Chaque décision est enregistrée. Le dashboard te montre tes points faibles par scénario.

## Stack

| Couche | Tech |
|--------|------|
| Backend | Python 3, Flask 3+ |
| Base de données | SQLite3 |
| Frontend | HTML5, CSS3, Vanilla JS |
| Templates | Jinja2 |

## Lancer le projet

```bash
pip install -r requirements.txt
python app.py
```

Puis ouvre [http://localhost:5000](http://localhost:5000).

## Structure

```
poker_quizz/
├── app.py          # Serveur Flask, routes API
├── database.py     # Persistance SQLite (progress.db)
├── ranges.py       # Ranges GTO — source de vérité
├── requirements.txt
├── templates/
│   ├── index.html      # Page d'accueil
│   ├── quiz.html       # Interface quiz
│   └── dashboard.html  # Stats et progression
└── static/
    ├── css/style.css
    └── js/quiz.js
```

## API

| Route | Méthode | Description |
|-------|---------|-------------|
| `/` | GET | Page d'accueil |
| `/quiz` | GET | Interface quiz |
| `/dashboard` | GET | Tableau de bord |
| `/api/question` | GET | Génère une question aléatoire |
| `/api/answer` | POST | Valide une réponse, log en BDD |
| `/api/stats` | GET | Retourne les statistiques |

## Raccourcis clavier

| Touche | Action |
|--------|--------|
| `O` | Open / Ouvrir |
| `F` | Fold |
| `C` | Call |
| `3` | 3-bet |

## Scénarios couverts

**RFI (Raise First In)** — 5 positions :
UTG (~14%), HJ (~18%), CO (~26%), BTN (~42%), SB (~35%)

**vs RFI** — 13 scénarios :
HJ/CO/BTN vs UTG, CO/BTN vs HJ, BTN vs CO, SB vs BTN/CO, BB vs UTG/HJ/CO/BTN/SB

## Ranges

Toutes les ranges sont dans `ranges.py`. Elles sont basées sur les outputs de solvers modernes, ajustées pour le jeu pratique NL10-NL50. Voir aussi `STRATEGIE_NL6MAX.md` pour la stratégie complète documentée.
