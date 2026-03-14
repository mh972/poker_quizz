# Stratégie NL 6-max — Base solide pour NL5 / NL10

> Document de référence. Utilisable indépendamment dans d'autres projets.
> Ranges basées sur outputs de solvers GTO, adaptées pour le jeu exploitatif basse limite.

---

## Table des matières

1. [Positions et dynamiques](#1-positions-et-dynamiques)
2. [Concepts fondamentaux](#2-concepts-fondamentaux)
3. [RFI — Raise First In](#3-rfi--raise-first-in)
4. [vs RFI — Défense et 3-bet](#4-vs-rfi--défense-et-3-bet)
5. [Défense des blindes](#5-défense-des-blindes)
6. [Postflop — Principes de base](#6-postflop--principes-de-base)
7. [Ajustements exploitatifs NL5/NL10](#7-ajustements-exploitatifs-nl5nl10)
8. [Erreurs fréquentes à éviter](#8-erreurs-fréquentes-à-éviter)

---

## 1. Positions et dynamiques

```
BTN  SB  BB
      |
CO  HJ  UTG
```

**Ordre d'action préflop** (dernier à parler = meilleur) :
```
UTG → HJ → CO → BTN → SB → BB
```

**Position postflop** (pire = OOP) :
```
SB < BB < UTG < HJ < CO < BTN (IP = meilleur)
```

| Position | Abrév. | Contexte |
|----------|--------|---------|
| Under The Gun | UTG | Premier à parler — range tight |
| Hijack | HJ | Deuxième — légèrement plus large |
| Cutoff | CO | Deux avant BTN — assez large |
| Button | BTN | Meilleur poste — très large |
| Small Blind | SB | OOP vs BB — open sélectif |
| Big Blind | BB | Défend large grâce au pot odds |

---

## 2. Concepts fondamentaux

### Polarisation des ranges

En GTO, les ranges de 3-bet sont **polarisées** :

```
3-bet VALUE  ──▶  Très fortes mains (AA, KK, AKs...)
3-bet BLUFF  ──▶  Mains avec blockers + potentiel (A5s, A4s, K4s...)
─────────────────────────────────────────────────────
CALL         ──▶  Mains moyennes-fortes (TT, AJs, KQs...)
FOLD         ──▶  Tout le reste
```

**Pourquoi ne pas 3-bet TT ou AJs ?**
Ces mains ont trop d'equity pour bluff mais pas assez pour value pure face à une range tight. On les call pour garder une range de call défendable avec showdown value.

### Blockers

Un **blocker** est une carte qui réduit la probabilité que l'adversaire ait une main forte.

- `A5s` comme bluff de 3-bet : l'As **bloque AA et AK** dans la range adverse
- `K4s` comme bluff de 3-bet : le Roi **bloque KK et AK**

### Pot odds et equity requise

```
Pot odds = montant à caller / (pot total après call)
Equity requise ≈ pot odds
```

Exemple : pot 10€, adversaire bet 5€ → tu calls 5€ pour un pot de 20€ → tu as besoin de 25% d'equity.

### Range advantage

Celui qui a ouvert (aggressor) a souvent un **range advantage** sur le flop.
- UTG vs BB : UTG a peu de mains très fortes mais sa range moyenne est plus forte
- BTN vs BB : BTN a un **range advantage** ET **nut advantage** sur beaucoup de boards

---

## 3. RFI — Raise First In

> Sizing standard : **2,5 BB** en position (HJ, CO, BTN), **3 BB** depuis SB.

### UTG — ~14% des mains

Range tight. Seulement les meilleures mains car tu joues OOP contre 5 adversaires potentiels.

**Paires** : `AA KK QQ JJ TT 99 88 77 66 55 44 33 22`

**Suited** : `AKs AQs AJs ATs A5s A4s | KQs KJs KTs | QJs QTs | JTs T9s 98s 87s 76s 65s`

**Offsuit** : `AKo AQo AJo`

---

### HJ — ~18% des mains

On ajoute quelques Ax suited supplémentaires et des broadways offsuit.

**Paires** : toutes (22+)

**Suited** : `AKs AQs AJs ATs A9s A8s A5s A4s A3s | KQs KJs KTs K9s | QJs QTs Q9s | JTs J9s | T9s T8s 98s 87s 76s 65s 54s`

**Offsuit** : `AKo AQo AJo ATo | KQo`

---

### CO — ~26% des mains

Range significativement plus large. On joue tous les Ax suited, plus de connecteurs.

**Paires** : toutes (22+)

**Suited** : `AKs→A2s (tous) | KQs KJs KTs K9s K8s | QJs QTs Q9s Q8s | JTs J9s J8s | T9s T8s T7s | 98s 97s 87s 86s 76s 75s 65s 64s 54s 53s`

**Offsuit** : `AKo AQo AJo ATo A9o A8o | KQo KJo KTo | QJo`

---

### BTN — ~42% des mains

Position de choix. Range très large, on exploite au maximum le fold equity vs blindes.

**Paires** : toutes (22+)

**Suited** : `AKs→A2s | KQs KJs KTs K9s K8s K7s K6s K5s | QJs QTs Q9s Q8s Q7s | JTs J9s J8s J7s | T9s T8s T7s T6s | 98s 97s 96s 87s 86s 85s 76s 75s 74s 65s 64s 54s 53s 43s`

**Offsuit** : `AKo→A4o | KQo KJo KTo K9o | QJo QTo Q9o | JTo J9o | T9o`

---

### SB — ~35% des mains

Plus tight que BTN car on joue **OOP** contre BB sur tous les streets postflop.
Sizing recommandé : **3 BB** pour compenser le désavantage positionnel.

**Paires** : toutes (22+)

**Suited** : `AKs→A2s | KQs KJs KTs K9s K8s K7s K6s | QJs QTs Q9s Q8s | JTs J9s J8s | T9s T8s T7s | 98s 97s 87s 86s 76s 75s 65s 64s 54s 53s`

**Offsuit** : `AKo AQo AJo ATo A9o A8o A7o | KQo KJo KTo K9o | QJo QTo | JTo`

---

## 4. vs RFI — Défense et 3-bet

### Principe général

| Situation | 3-bet | Call | Fold |
|-----------|-------|------|------|
| IP vs open serré (UTG) | Polarisé, peu de bluffs | Mains playables avec SD value | Tout le reste |
| IP vs open large (BTN) | Plus de bluffs possibles | Large range de call | Moins |
| OOP | 3-bet ou fold — le call OOP est souvent une erreur | Possible mais sélectif | Plus souvent |

---

### HJ vs UTG open

```
3-bet :  AA KK QQ JJ | AKs AQs AJs AKo AQo | A5s A4s (bluffs)
Call  :  TT 99 88 77 66 55 | ATs A9s | KQs KJs KTs | QJs QTs | JTs T9s 98s 87s 76s
Fold  :  tout le reste
```

---

### CO vs UTG open

```
3-bet :  AA KK QQ JJ | AKs AQs AKo AQo | A5s A4s (bluffs)
Call  :  TT 99 88 77 66 55 | AJs ATs A9s | KQs KJs KTs | QJs QTs | JTs T9s 98s 87s 76s 65s
Fold  :  tout le reste
```

---

### CO vs HJ open

```
3-bet :  AA KK QQ JJ | AKs AQs AJs AKo AQo | A5s A4s A3s (bluffs)
Call  :  TT 99 88 77 66 55 44 | ATs A9s A8s | KQs KJs KTs K9s | QJs QTs Q9s | JTs J9s T9s T8s 98s 87s 76s 65s 54s
Fold  :  tout le reste
```

---

### BTN vs UTG open

```
3-bet :  AA KK QQ JJ | AKs AQs AKo AQo | A5s A4s (bluffs)
Call  :  TT 99 88 77 66 55 | AJs ATs A9s | KQs KJs KTs | QJs QTs | JTs T9s 98s 87s 76s 65s
Fold  :  tout le reste
```

---

### BTN vs HJ open

```
3-bet :  AA KK QQ JJ | AKs AQs AJs AKo AQo AJo | A5s A4s A3s (bluffs)
Call  :  TT 99 88 77 66 55 44 | ATs A9s A8s | KQs KJs KTs K9s | QJs QTs Q9s | JTs J9s T9s T8s 98s 97s 87s 76s 65s 54s
Fold  :  tout le reste
```

---

### BTN vs CO open

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs ATs AKo AQo AJo | A5s A4s A3s A2s | KQs (valeur + bluffs)
Call  :  99 88 77 66 55 44 33 | A9s A8s A7s | KJs KTs K9s | QJs QTs Q9s Q8s | JTs J9s J8s | T9s T8s 98s 97s 87s 86s 76s 75s 65s 64s 54s
Fold  :  tout le reste
```

---

### SB vs BTN open

> Depuis SB, on est OOP sur tous les streets. Le call est possible mais sélectif. On 3-bet large.

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs ATs AKo AQo AJo | A5s A4s A3s A2s | KQs K5s K4s (bluffs avec blockers)
Call  :  99 88 77 66 55 44 33 22 | A9s A8s A7s A6s | KJs KTs K9s K8s K7s K6s | QJs QTs Q9s Q8s | JTs J9s J8s | T9s T8s T7s | 98s 97s 87s 86s 76s 75s 65s 64s 54s 53s
Fold  :  tout le reste
```

---

### SB vs CO open

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs AKo AQo AJo | A5s A4s A3s | KQs (bluffs)
Call  :  99 88 77 66 55 44 33 22 | ATs A9s A8s A7s | KJs KTs K9s K8s | QJs QTs Q9s | JTs J9s T9s T8s 98s 87s 76s 65s 54s
Fold  :  tout le reste
```

---

## 5. Défense des blindes

> Le BB a le meilleur prix sur le pot. Sa range de défense est la plus large du tableau.

### BB vs UTG open

```
3-bet :  AA KK QQ JJ | AKs AQs AKo AQo | A5s A4s (bluffs)
Call  :  TT 99 88 77 66 55 44 33 22 | AJs ATs A9s A8s A3s A2s | KQs KJs KTs | QJs QTs | JTs J9s | T9s T8s 98s 87s 76s 65s 54s
Fold  :  tout le reste (range UTG est très tight — respecter)
```

---

### BB vs HJ open

```
3-bet :  AA KK QQ JJ | AKs AQs AJs AKo AQo AJo | A5s A4s A3s (bluffs)
Call  :  TT 99 88 77 66 55 44 33 22 | ATs A9s A8s A7s A6s | ATo A9o | KQs KJs KTs K9s K8s | KQo KJo KTo | QJs QTs Q9s Q8s | QJo | JTs J9s J8s | T9s T8s T7s | 98s 97s 87s 86s 76s 75s 65s 54s
Fold  :  tout le reste
```

---

### BB vs CO open

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs AKo AQo AJo | A5s A4s A3s | KQs (bluffs)
Call  :  99 88 77 66 55 44 33 22 | ATs A9s A8s A7s A6s A2s | ATo A9o A8o | KJs KTs K9s K8s K7s | KQo KJo KTo | QJs QTs Q9s Q8s | QJo QTo | JTs J9s J8s | JTo | T9s T8s T7s | 98s 97s 87s 86s 76s 75s 65s 64s 54s 53s
Fold  :  tout le reste
```

---

### BB vs BTN open

> BTN ouvre très large → BB peut défendre très large aussi.

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs ATs AKo AQo AJo | A5s A4s A3s A2s | KQs K5s K4s K3s | 76s 65s 54s (bluffs avec equity)
Call  :  99 88 77 66 55 44 33 22 | A9s A8s A7s A6s | ATo A9o A8o A7o | KJs KTs K9s K8s K7s K6s | KQo KJo KTo K9o | QJs QTs Q9s Q8s Q7s | QJo QTo Q9o | JTs J9s J8s J7s | JTo J9o | T9s T8s T7s T6s | T9o | 98s 97s 96s 87s 86s 85s 75s 74s 64s 63s 53s 43s
Fold  :  très peu de mains
```

---

### BB vs SB open

> SB ouvre OOP → BB peut être très agressif. Range de 3-bet très large.

```
3-bet :  AA KK QQ JJ TT | AKs AQs AJs ATs AKo AQo AJo ATo | A5s A4s A3s A2s | KQs K5s K4s | QJs Q8s | 76s 65s 54s 43s (bluffs larges)
Call  :  99 88 77 66 55 44 33 22 | A9s A8s A7s A6s | A9o A8o A7o A6o A5o | KJs KTs K9s K8s K7s K6s K5s | KQo KJo KTo K9o K8o | QTs Q9s Q7s Q6s | QJo QTo Q9o | JTs J9s J8s J7s | JTo J9o | T9s T8s T7s T6s | T9o | 98s 97s 96s 87s 86s 85s 75s 74s 64s 63s 53s 42s
Fold  :  quasi rien
```

---

## 6. Postflop — Principes de base

### C-bet (continuation bet)

**IP (en position)** :
- C-bet fréquemment sur les boards qui favorisent ta range (boards secs, hauts)
- Taille : **33-50% du pot** sur boards secs, **50-75%** sur boards humides
- Ne pas c-bet 100% — checker les mains moyennes pour protection

**OOP (hors position)** :
- C-bet plus sélectivement
- Préférer les mains avec bonne équité ou nut advantage
- Checker-call avec les mains moyennes, checker-raise avec les draws forts et les top pairs

### Boards favorables pour le pré-flop aggressor

| Type de board | Range advantage pour |
|--------------|---------------------|
| A-K-x sec | UTG/HJ — plus d'AK, AQ dans leur range |
| 2-7-9 arc-en-ciel | BTN/CO — range basse n'est pas connectée |
| T-J-Q connecté | BB / range large — connects bien avec range de call |
| Monotone flush | Avantage à la range suited |

### Tailles de bet

```
Value thin / bluff → 33% pot (cheap, maximize calls)
Value bet standard → 50-67% pot
Overpot / jam       → 100-120% pot (KK+/top set vs draws)
```

### Blinds vs IP aggressor postflop

- **Folder** beaucoup sur les boards qui manquent ta range
- **Donk bet** très rare en GTO — préférer check-raise
- **Float** possible IP mais OOP ça coûte cher

---

## 7. Ajustements exploitatifs NL5/NL10

À ces stakes, les joueurs ont des **fuites massives** qu'on peut exploiter directement plutôt que de jouer full GTO.

### vs les limpers (très courant NL5)

En position : **iso-raise** à 4-5 BB + 1 BB par limper
- Mains recommandées : TT+, AJs+, AQo+, KQs et tous les jouables IP
- Objectif : jouer IP HU contre un joueur passif

### vs les fishs passifs (call stations)

- **Value bet large** : 75-100% pot avec top pair+
- **Bluff très peu** — les call stations ne foldent pas
- **Extraire maximum sur 3 streets** avec les bonnes mains

### vs les niteux (tight-passifs)

- **Steal wide** les blindes — ils défendent trop peu
- **Fold equity élevée** — tes 3-bets ont beaucoup de valeur
- **Respecter** leurs 3-bets / raises — ils ont toujours quelque chose

### vs les aggros / 3-betteurs fréquents

- **Call** plus de mains IP pour les pièger
- **4-bet** les bluffs probables avec polarisation (AA/KK + A5s/A4s)
- **Réduire** les mains marginales d'ouverture si tu te fais 3-bet 15%+

### Ajustements selon les stats (si tu as un HUD)

| Stat | Que faire |
|------|-----------|
| VPIP > 40% | Value bet large, pas de bluff |
| PFR < 8% | Respect total de ses raises — fold wide |
| 3-bet > 12% | 4-bet bluff ou call IP, ne pas fold top-pair+ |
| Fold to c-bet > 70% | C-bet systématique sur ses bigs blindes |
| Fold to 3-bet > 70% | 3-bet steal large depuis BTN/CO/SB |

---

## 8. Erreurs fréquentes à éviter

### Préflop

| Erreur | Correction |
|--------|-----------|
| 3-bet TT/AJs face à UTG | Call — trop bien pour bluff, range too strong pour value thin |
| Limper depuis SB | Open ou fold — le limp crée une range exploitable |
| Call depuis SB vs BTN | Souvent mieux de 3-bet ou fold — on joue OOP sur 3 streets |
| Over-fold le BB | BB a le meilleur prix — défendre large |
| Ouvrir trop large UTG | UTG = tight. 22+ oui, mais pas les hands connectées faibles |

### Postflop

| Erreur | Correction |
|--------|-----------|
| C-bet 100% du temps OOP | Checker les mains moyennes, garder une range équilibrée |
| Bluffer les call stations | Ne pas bluffer — only value |
| Bet trop petit avec les nuts | Extraire max : 75-100% du pot sur mains très fortes |
| Trop de passivité avec les draws forts | Semi-bluff / check-raise avec les flush draws + straight draws |
| Stack off avec top pair sur board humide | Évaluer la combinaison de board — parfois fold top pair |

---

## Références rapides

### Notation des mains

```
AKs = As Ks (suited / même couleur)
AKo = Ac Kd (offsuit / couleurs différentes)
AA  = As Ah (paire)
```

### Hiérarchie des mains

```
Royal Flush > Quinte Flush > Carré > Full House > Flush >
Quinte > Brelan > Deux paires > Paire > Haute carte
```

### Pot odds rapides

| Bet / Pot | Equity requise |
|-----------|---------------|
| 33% (1/3) | 20% |
| 50% (1/2) | 25% |
| 75% (3/4) | 30% |
| 100%      | 33% |
| 150%      | 40% |

---

*Document basé sur les ranges du projet GTO Preflop Trainer. Les ranges sont des approximations GTO adaptées pour NL10-NL50 — pas des solutions solver exactes.*
