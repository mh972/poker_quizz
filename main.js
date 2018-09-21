/**
 * Description
 */

// Librairies
const math = require("mathjs");
// const readline = require("readline");
const orRanges = require("./public/openRaiseRanges");
const ranges3Bet = require("./public/3betRanges");
const inquirer = require("inquirer");

// Constant Variables
const CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"];
const COLORS = ["d", "h", "c", "s"];
const POSITIONS = ["EP", "CO", "BTN", "SB"];

// Functions
class Card {
    constructor(rank, color) {
        (this.rank = CARDS[rank]), (this.color = COLORS[color]);
    }

    show() {
        return this.rank + this.color;
    }
}

class Hand {
    constructor(alreadyUsed = []) {
        let card1 = new Card(
            math.randomInt(0, CARDS.length - 1),
            math.randomInt(0, COLORS.length - 1)
        );
        while (alreadyUsed.includes(card1)) {
            card1 = new Card(
                math.randomInt(0, CARDS.length - 1),
                math.randomInt(0, COLORS.length - 1)
            );
        }

        alreadyUsed.push(card1);

        let card2 = new Card(
            math.randomInt(0, CARDS.length - 1),
            math.randomInt(0, COLORS.length - 1)
        );
        while (alreadyUsed.includes(card2)) {
            card2 = new Card(
                math.randomInt(0, CARDS.length - 1),
                math.randomInt(0, COLORS.length - 1)
            );
        }

        // Sorting ranks to always have the top rank in card 1
        let index1 = CARDS.indexOf(card1.rank);
        let index2 = CARDS.indexOf(card2.rank);

        this.card1 = index1 <= index2 ? card1 : card2;
        this.card2 = index1 <= index2 ? card2 : card1;
    }

    show() {
        let result = this.card1.rank + this.card2.rank;
        if (this.card1.rank !== this.card2.rank) {
            result += this.card1.color === this.card2.color ? "s" : "o";
        }
        return result;
    }
}

function quizzOR() {
    let myHand = new Hand();
    let myPositon = math.randomInt(0, POSITIONS.length);
    let question = {
        type: "input",
        name: "quizz",
        message: "Your hand is "
            .concat(myHand.show())
            .concat(" from ")
            .concat(POSITIONS[myPositon])
            .concat(". Should you Open Raise ?")
    };
    let shouldRaise = orRanges(myPositon).includes(myHand.show());

    return new Promise(function (resolve, reject) {
        inquirer
            .prompt([question])
            .then(answer => {
                resolve({
                    hand: myHand.show(),
                    position: POSITIONS[myPositon],
                    action: (answer.quizz === "1") ? "raise" : "fold",
                    goodAction: shouldRaise ? "raise" : "fold"
                });
            })
            .catch(err => {
                console.log(err);
                reject(err);
            });
    });
}

function quizz3Bet() {
    let myHand = new Hand();
    let myPositon = math.randomInt(0, POSITIONS.length);
    let aggPosition = math.max(math.randomInt(0, myPositon), 0);
    let question = {
        type: "input",
        name: "quizz",
        message: "Your hand is "
            .concat(myHand.show())
            .concat(" from ")
            .concat(POSITIONS[myPositon])
            .concat(" and agg is raising from ")
            .concat(POSITIONS[aggPosition])
            .concat(". Should you 3Bet ?")
    };
    let shouldRaise = ranges3Bet(myPositon, aggPosition).includes(myHand.show());

    return new Promise(function (resolve, reject) {
        inquirer
            .prompt([question])
            .then(answer => {
                resolve({
                    hand: myHand.show(),
                    position: POSITIONS[myPositon],
                    aggPosition: POSITIONS[aggPosition],
                    action: (answer.quizz === "1") ? "3bet" : "other",
                    goodAction: shouldRaise ? "3bet" : "other"
                });
            })
            .catch(err => {
                console.log(err);
                reject(err);
            });
    });
}

async function quizzesOR(nb) {
    let stats = [];
    let errors = [];
    for (let i = 0; i < nb; i++) {
        console.log("Question #", i, "out of", nb)
        let result = await quizzOR();
        stats.push(result.action === result.goodAction);
        if (result.action !== result.goodAction) errors.push(result.hand + " from " + result.position + " where you " + result.action + " instead of " + result.goodAction)
    }
    console.log(
        "You have a score of",
        math.round((stats.filter(elt => elt).length / stats.length) * 100, 2), "%"
    );
    console.log("Your errors are")
    console.log(errors)
}

async function quizzes3Bet(nb) {
    let stats = [];
    let errors = [];
    for (let i = 0; i < nb; i++) {
        console.log("Question #", i, "out of", nb)
        let result = await quizz3Bet();
        stats.push(result.action === result.goodAction);
        if (result.action !== result.goodAction) errors.push(result.hand + " from " + result.position + " against " + result.aggPosition + " where you " + result.action + " instead of " + result.goodAction)
    }
    console.log(
        "You have a score of",
        math.round((stats.filter(elt => elt).length / stats.length) * 100, 2), "%"
    );
    console.log("Your errors are")
    console.log(errors)
}

// quizzesOR(5);
// quizzes3Bet(5);

function getProbabilities(nb) {
    let init = new Date()
    let played = new Map([[0, 0], [1, 0], [2, 0], [3, 0]])
    for (let i = 0; i < nb; i++) {
        let myHand = new Hand();
        for (let j = 0; j < POSITIONS.length; j++) {
            if (orRanges(j).includes(myHand.show())) {
                let inc = played.get(j) + 1
                played.set(j, inc)
            }
        }
    }

    console.log("All raising stats are:")
    let pfr = 0
    for (let key of played.keys()) {
        let pb = played.get(key) / nb
        pfr += pb / 6
        console.log("From", POSITIONS[key], math.round(pb * 100, 2), "%")
    }
    console.log("And total PFR = ", math.round(pfr * 100, 2), "%")

    console.log("Running the computations took", (new Date() - init) / 1000, "secondes")

}

// // getProbabilities(10000000)

// let init = new Date()
// for (let i = 1;i<10000000;i++) {
//     let t = math.random();
// }
// console.log("Running the computations took",(new Date()-init)/1000,"secondes")


/**
 * Main
 */
let question = {
    type: "list",
    name: "type",
    message: "What do you want to learn ?",
    choices: ["open raise", "3bet", "other"]
};

inquirer.prompt([question])
    .then(answer => {
        switch (answer.type) {
            case "open raise":
                quizzesOR(100);
                break;
            case "3bet":
                quizzes3Bet(100);
                break;
            default:
                console.log("Bye")
        }
    })