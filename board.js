"use strict";
exports.__esModule = true;
exports.Game2048 = void 0;
var Game2048 = /** @class */ (function () {
    function Game2048() {
        this.score = 0;
        this.board = [[], [], [], []];
        for (var i = 0; i < 4; i++) {
            for (var i_1 = 0; i_1 < 4; i_1++) {
                this.board[i_1].push(0);
            }
        }
        this.addRandomTile();
        this.addRandomTile();
    }
    Game2048.prototype.randomInt = function (x, y) {
        return x + Math.floor(Math.random() * (y - x + 1));
    };
    Game2048.prototype.transformRow = function (arr, positive) {
        var A, B;
        A = arr.filter(function (i) { return i !== 0; });
        B = [];
        positive === true ? A.reverse() : NaN;
        if (A.length !== 0) {
            while (A.length !== 1 && A.length !== 0) {
                if (A[0] === A[1]) {
                    B.push(2 * A[0]);
                    this.score += 2 * A[0];
                    A.splice(0, 1);
                }
                else
                    B.push(A[0]);
                A.splice(0, 1);
            }
            if (A.length !== 0) {
                B.push(A[0]);
                A.splice(0, 1);
            }
        }
        positive === true ? B.reverse() : NaN;
        while (B.length !== 4) {
            if (positive)
                B.splice(0, 0, 0);
            else
                B.push(0);
        }
        return B;
    };
    Game2048.prototype.addRandomTile = function () {
        var _a;
        var candidates = [];
        for (var i = 0; i < 4; i++) {
            for (var j = 0; j < 4; j++) {
                if (this.board[i][j] === 0)
                    candidates.push([i, j]);
            }
        }
        var x, y, ind;
        ind = this.randomInt(0, candidates.length - 1);
        _a = candidates[ind], x = _a[0], y = _a[1];
        this.board[x][y] = this.randomInt(0, 1) === 0 ? 2 : 4;
    };
    Game2048.prototype.printBoard = function () {
        var _loop_1 = function (i) {
            var A = "";
            this_1.board[i].forEach(function (j) { return (A += j.toString() + " "); });
            console.log(A);
        };
        var this_1 = this;
        for (var i = 0; i < 4; i++) {
            _loop_1(i);
        }
        console.log("\n");
    };
    Game2048.prototype.swipeLeft = function () {
        if (this.gameOver())
            return;
        for (var i = 0; i < 4; i++) {
            this.board[i] = this.transformRow(this.board[i], false);
        }
        if (this.gameOver())
            return;
        this.addRandomTile();
    };
    Game2048.prototype.swipeRight = function () {
        if (this.gameOver())
            return;
        for (var i = 0; i < 4; i++) {
            this.board[i] = this.transformRow(this.board[i], true);
        }
        if (this.gameOver())
            return;
        this.addRandomTile();
    };
    Game2048.prototype.swipeUp = function () {
        var _a;
        if (this.gameOver())
            return;
        for (var i = 0; i < 4; i++) {
            _a = this.transformRow([
                this.board[0][i],
                this.board[1][i],
                this.board[2][i],
                this.board[3][i],
            ], false), this.board[0][i] = _a[0], this.board[1][i] = _a[1], this.board[2][i] = _a[2], this.board[3][i] = _a[3];
        }
        if (this.gameOver())
            return;
        this.addRandomTile();
    };
    Game2048.prototype.swipeDown = function () {
        var _a;
        if (this.gameOver())
            return;
        for (var i = 0; i < 4; i++) {
            _a = this.transformRow([
                this.board[0][i],
                this.board[1][i],
                this.board[2][i],
                this.board[3][i],
            ], true), this.board[0][i] = _a[0], this.board[1][i] = _a[1], this.board[2][i] = _a[2], this.board[3][i] = _a[3];
        }
        if (this.gameOver())
            return;
        this.addRandomTile();
    };
    Game2048.prototype.gameOver = function () {
        var zeroExists = false;
        this.board.forEach(function (board) {
            board.forEach(function (val) {
                if (val === 0)
                    zeroExists = true;
            });
        });
        for (var i = 0; i < 4; i++) {
            for (var j = 0; j < 3; j++) {
                if (this.board[i][j] === this.board[i][j + 1])
                    return false;
                if (this.board[j][i] === this.board[j + 1][i])
                    return false;
            }
        }
        return true && !zeroExists;
    };
    return Game2048;
}());
exports.Game2048 = Game2048;
