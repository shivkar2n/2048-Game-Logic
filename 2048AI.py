# x1 - number of tiles
# x2 - maximum tile value
# x3 - number of adjacent tiles

def heuristic(x1: int, x2: int, x3: int) -> float:
    return 16/x1+x2/11+x3/8

def noOfTiles(board: list[list[int]]) -> int:
    return 16 - sum(row.count(0) for row in board)

def maxTileValue(board: list[list[int]]) -> int:
    return max([max(row) for row in board])

def numAdjTiles(board: list[list[int]], colWise: bool) -> int:
    noZeroBoard = board
    if colWise : 
        list(zip(*noZeroBoard[::-1])) # Rotate matrix
    n = 0
    for row in range(4):
        nums = [num for num in noZeroBoard[row] if num != 0]
        i = 0
        mergedNums = []
        while i < len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                mergedNums.append(2*nums[i])
                n +=1
                i += 2
            else:
                mergedNums.append(nums[i])
                i += 1
        mergedNums = mergedNums + [0] * (4-len(mergedNums))
        noZeroBoard[row] = mergedNums
    return n

    


# def DFS2048():
