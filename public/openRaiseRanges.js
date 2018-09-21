/**
 * Return a range for a position
 */

// Librairies

// Constants
const EP = [
  "AA",
  "KK",
  "QQ",
  "JJ",
  "TT",
  "99",
  "88",
  "77",
  "66",
  "55",
  "44",
  "33",
  "22",
  "AKs",
  "AQs",
  "AJs",
  "ATs",
  "A5s",
  "A4s",
  "A3s",
  "A2s",
  "AKo",
  "AQo",
  "KQs",
  "QJs",
  "JTs",
  "T9s",
  "98s",
  "87s",
  "76s"
];
const CO = EP.concat([
  "A9s",
  "A8s",
  "A7s",
  "A6s",
  "AJo",
  "ATo",
  "A9o",
  "A8o",
  "KJs",
  "KTs",
  "QTs",
  "KQo",
  "65s",
  "J9s",
  "T8s",
  "97s"
]);
const BTN = CO.concat([
    "A7o","A6o","A5o","A4o","A3o","A2o","KJo","KTo","QJo","86s","K9s","K8s","K7s","K6s","K5s","K4s","K3s","K2s","Q9s"
])
const SB = ["AA","KK","QQ","JJ","TT","99","AKs","AQs","AJs","ATs","KQs","KJs","AKo","AQo","AJo"]
const POSITIONS_RANGES = new Map([[0,EP],[1,CO],[2,BTN],[3,SB]])

// Functions

// Exports
module.exports = function (positionIndex) {
    return POSITIONS_RANGES.get(positionIndex)
}

// Tests

