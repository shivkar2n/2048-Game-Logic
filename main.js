"use strict";
exports.__esModule = true;
var board_1 = require("./board");
var prompt = require("prompt-sync")({ sigint: true });
var G = new board_1.Game2048();
var done = false;
var n;
console.log("Direction: Up(w), Down(s), Left(a), Right(d)");
while (!done) {
    G.printBoard();
    console.log("Score: ".concat(G.score));
    n = prompt("Enter Move: ");
    if (n === "a")
        G.swipeLeft();
    else if (n === "d")
        G.swipeRight();
    else if (n === "w")
        G.swipeUp();
    else if (n === "s")
        G.swipeDown();
    else if (n === "e")
        done = true;
    else
        console.log("Invalid Option");
}
