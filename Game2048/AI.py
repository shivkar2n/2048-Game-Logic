# x1 - number of tiles
# x2 - maximum tile value
# x3 - number of adjacent tiles

def noOfTiles(board: list) -> int:
    return 16 - sum(row.count(0) for row in board)

def maxTileValue(board: list) -> int:
    return max([max(row) for row in board])

def numAdjTiles(board: list, colWise: bool) -> int:
    noZeroBoard = board
    if colWise:
        list(zip(*noZeroBoard[::-1]))  # Rotate matrix
    n = 0
    for row in range(4):
        nums = [num for num in noZeroBoard[row] if num != 0]
        i = 0
        mergedNums = []
        while i < len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                mergedNums.append(2*nums[i])
                n += 1
                i += 2
            else:
                mergedNums.append(nums[i])
                i += 1
        mergedNums = mergedNums + [0] * (4-len(mergedNums))
        noZeroBoard[row] = mergedNums
    return n


def heuristic(board: list) -> float:
    [x1, x2, x3] = [noOfTiles(board.copy()), maxTileValue(
        board.copy()), numAdjTiles(board.copy(), False)+numAdjTiles(board.copy(),True)]
    return 16/x1+x2/11+x3/8


def averageWeight(board: list) -> float:
    total = n = 0
    temp = board.copy()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 0:
                temp[i][j], total = 2, total+heuristic(temp)
                temp[i][j], total = 4, total+heuristic(temp)
                n += 2
                temp[i][j] = 0
    return total/n


def isGameOver(board: list):
    for row in board:
        for square in row:
            if square == 0: return False

    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] : return False
            if board[j][i] == board[j+1][i] : return False
    return True


def goalTest(board:list) -> bool:
    return any(256 in row for row in board)


