/**
 * Return a range for a position
 */

// Librairies

// Constants
const EP = [["AA","KK","QQ","AKs","AKo","A5s","A4s"]]
const CO = [EP[0]]
const BTN = [EP[0],EP[0].concat("JJ","TT","AQs","AQo","A3s","A2s","87s","76s")]
const SB = [["AA","KK","AKs","AKo","A5s"],EP[0].concat("JJ","AQs","AQo","A3s","A2s","87s","76s"),BTN[1].concat("AJs","A7s","A6s","KQs")]
const BB = [SB[0],SB[1],SB[2],SB[2].concat("AJo","KQo","65s","86s","75s")]

const POSITIONS_RANGES = new Map([[0,EP],[1,CO],[2,BTN],[3,SB]])

// Exports
module.exports = function (positionHero,positionAgg) {
    return POSITIONS_RANGES.get(positionHero)[positionAgg]
}