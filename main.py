from Game2048.Game import Game_2048
from Game2048.AI import heuristic, goalTest
from Game2048.PriorityQueue import PriorityQueue
import time

def printBoard(board: list):
    for row in board:
        print(row)
    print('\n')

def UniformCostSearch(game: object):
    start_time = time.time()
    pathCost = 0
    PQ = PriorityQueue()
    PQ.insert([game.getBoard(),0])
    explored = []

    while True:
        if PQ.isEmpty(): return False

        if pathCost == 100000:
            printBoard(PQ.delete())
            print(pathCost)
            return False

        node = PQ.delete()
        game.insertNewNumber(node,None)
        node = game.getBoard()
        explored.append(node)

        if goalTest(node):
            printBoard(node)
            print(pathCost)
            return True

        pathCost += 1

        moves = {
            'left' : game.move_left,
            'right' : game.move_right,
            'up' : game.move_up,
            'down' : game.move_down
        }

        for cfg, move in zip([node.copy() for i in range(4)],moves):
            temp = moves[move](cfg)
            if not temp in explored and not temp in [i[0] for i in PQ]:
                PQ.insert([temp,heuristic(temp)])

        print("Seconds: %s" % (time.time() - start_time), end="\r",flush=True)


def DepthFirstSearch(board: list, game: object, visited: list, height: int):
    global maxCost, maxState, defaultHeight
    currHeight = height
    if currHeight == 1 or board in visited: return

    print("\n")

    if goalTest(board):
        printBoard(board)
        return

    # print("Seconds: %s" % (time.time() - start_time), end="\r",flush=True)

    visited.append(board)
    node = game.insertNewNumber(board)

    printBoard(board)
    print("\n")

    moves = {
        'left' : game.move_left,
        'right' : game.move_right,
        'up' : game.move_up,
        'down' : game.move_down
    }
    for cfg, move in zip([node.copy() for i in range(4)],moves):
        temp = moves[move](cfg)
        print(f"Move: {move}, Height: {height}")
        printBoard(temp)
        DepthFirstSearch(temp,game,visited,currHeight-1)


start_time = time.time()
G = Game_2048()
# UniformCostSearch(G)

initialBoard = G.getBoard().copy()
DepthFirstSearch(initialBoard,G,[],3)
