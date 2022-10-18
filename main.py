from Game2048.Game import Game_2048
from Game2048.AI import heuristic, goalTest, isGameOver, averageWeight

def printBoard(board: list):
    for row in board:
        print(row)
    print('\n')

def DepthFirstSearch(board: list, game: object, visited: list):
    if isGameOver(board): return

    if goalTest(board):
        for board in visited:
            printBoard(board)
        return

    # print("Seconds: %s" % (time.time() - start_time), end="\r",flush=True)

    visited.append(board)

    # printBoard(board)
    # print("\n")

    moves = {
        'left' : game.move_left,
        'right' : game.move_right,
        'up' : game.move_up,
        'down' : game.move_down
    }

    # printBoard(board)
    posBoardCfg = [ [move, averageWeight(moves[move](board.copy()))] for move in moves]
    posBoardCfg = sorted(posBoardCfg, key= lambda x: x[1], reverse=True)

    for pos in posBoardCfg:
        boardCopy = moves[pos[0]](board.copy())
        if board == boardCopy: continue
        boardCopy = game.insertNewNumber(boardCopy)
        printBoard(boardCopy)
        print(pos[0])
        DepthFirstSearch(boardCopy, game, visited)


# start_time = time.time()
G = Game_2048()
# UniformCostSearch(G)

initialBoard = G.getBoard().copy()
DepthFirstSearch(initialBoard,G,[])
