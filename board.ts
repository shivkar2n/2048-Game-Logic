class Game2048 {
  board: Array<Array<number>>;
  score: number;

  randomInt(x: number, y: number): number {
    return x + Math.floor(Math.random() * (y - x + 1));
  }

  transformRow(arr: Array<number>, positive: boolean): Array<number> {
    let A, B: Array<number>;
    A = arr.filter((i) => i !== 0);
    B = [];
    positive === true ? A.reverse() : NaN;
    if (A.length !== 0) {
      while (A.length !== 1 && A.length !== 0) {
        if (A[0] === A[1]) {
          B.push(2 * A[0]);
          this.score += 2 * A[0];
          A.splice(0, 1);
        } else B.push(A[0]);
        A.splice(0, 1);
      }
      if (A.length !== 0) {
        B.push(A[0]);
        A.splice(0, 1);
      }
    }
    positive === true ? B.reverse() : NaN;
    while (B.length !== 4) {
      if (positive) B.splice(0, 0, 0);
      else B.push(0);
    }
    return B;
  }

  constructor() {
    this.score = 0;
    this.board = [[], [], [], []];
    for (let i: number = 0; i < 4; i++) {
      for (let i: number = 0; i < 4; i++) {
        this.board[i].push(0);
      }
    }
    this.addRandomTile();
    this.addRandomTile();
  }

  addRandomTile(): void {
    let candidates: Array<Array<number>> = [];
    for (let i: number = 0; i < 4; i++) {
      for (let j: number = 0; j < 4; j++) {
        if (this.board[i][j] === 0) candidates.push([i, j]);
      }
    }
    let x, y, ind: number;
    ind = this.randomInt(0, candidates.length - 1);
    [x, y] = candidates[ind];
    this.board[x][y] = this.randomInt(0, 1) === 0 ? 2 : 4;
  }

  printBoard(): void {
    for (let i: number = 0; i < 4; i++) {
      let A: string = "";
      this.board[i].forEach((j) => (A += j.toString() + " "));
      console.log(A);
    }
    console.log("\n");
  }

  swipeLeft(): void {
    if (this.gameOver()) return;
    for (let i: number = 0; i < 4; i++) {
      this.board[i] = this.transformRow(this.board[i], false);
    }
    if (this.gameOver()) return;
    this.addRandomTile();
  }

  swipeRight(): void {
    if (this.gameOver()) return;
    for (let i: number = 0; i < 4; i++) {
      this.board[i] = this.transformRow(this.board[i], true);
    }
    if (this.gameOver()) return;
    this.addRandomTile();
  }

  swipeUp(): void {
    if (this.gameOver()) return;
    for (let i: number = 0; i < 4; i++) {
      [this.board[0][i], this.board[1][i], this.board[2][i], this.board[3][i]] =
        this.transformRow(
          [
            this.board[0][i],
            this.board[1][i],
            this.board[2][i],
            this.board[3][i],
          ],
          false
        );
    }
    if (this.gameOver()) return;
    this.addRandomTile();
  }

  swipeDown(): void {
    if (this.gameOver()) return;
    for (let i: number = 0; i < 4; i++) {
      [this.board[0][i], this.board[1][i], this.board[2][i], this.board[3][i]] =
        this.transformRow(
          [
            this.board[0][i],
            this.board[1][i],
            this.board[2][i],
            this.board[3][i],
          ],
          true
        );
    }
    if (this.gameOver()) return;
    this.addRandomTile();
  }

  gameOver(): boolean {
    let zeroExists: Boolean = false;
    this.board.forEach((board) => {
      board.forEach((val) => {
        if (val === 0) zeroExists = true;
      });
    });
    for (let i: number = 0; i < 4; i++) {
      for (let j: number = 0; j < 3; j++) {
        if (this.board[i][j] === this.board[i][j + 1]) return false;
        if (this.board[j][i] === this.board[j + 1][i]) return false;
      }
    }
    return true && !zeroExists;
  }
}

export { Game2048 };
