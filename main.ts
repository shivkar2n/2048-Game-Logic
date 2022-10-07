import { Game2048 } from "./board";
const prompt = require("prompt-sync")({ sigint: true });

let G = new Game2048();
let done: Boolean = false;
let n: string;

console.log(`Direction: Up(w), Down(s), Left(a), Right(d)`);

while (!done) {
  G.printBoard();
  console.log(`Score: ${G.score}`);
  n = prompt("Enter Move: ");
  if (n === "a") G.swipeLeft();
  else if (n === "d") G.swipeRight();
  else if (n === "w") G.swipeUp();
  else if (n === "s") G.swipeDown();
  else if (n === "e") done = true;
  else console.log("Invalid Option");
}
