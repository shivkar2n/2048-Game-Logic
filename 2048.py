from random import random, randint

def createBoard():
    row = [0]*4
    board = [row[:] for i in range(4)]

    loc1 = [randint(0,3), randint(0,3)]
    loc2 = [randint(0,3), randint(0,3)]

    while loc2 == loc1:
        loc2 = [randint(0,3), randint(0,3)]

    if random() <= 0.1:
        board[loc1[0]][loc1[1]] = 4
    else:
        board[loc1[0]][loc1[1]] = 2

    if random() <= 0.1:
        board[loc2[0]][loc2[1]] = 4
    else:
        board[loc2[0]][loc2[1]] = 2

    return board
    
def game(board):
    while not any(2048 in row for row in board):
        board = turn(board)
        print('\n', *board, sep='\n')

def insertNewNumber(board):
    loc = [randint(0,3), randint(0,3)]
    while board[loc[0]][loc[1]] != 0:
        loc = [randint(0,3), randint(0,3)]
    if random() <= 0.1:
        board[loc[0]][loc[1]] = 4
    else:
        board[loc[0]][loc[1]] = 2
    return board

def turn(board):
    move = str(input('Enter move: '))
    changed = False
    while not changed:
        if move == 's':
            board, changed, = move_down(board)    
        elif move == 'w':
            board, changed = move_up(board)
        elif move == 'a':
            board, changed = move_left(board)
        elif move == 'd':
            board, changed = move_right(board)    
        
    board = insertNewNumber(board)
    return board

def move_down(board):
    board = transpose(board)
    board, changed = move_right(board)
    board = transpose(board)
    return (board, changed)

def move_up(board):
    board = transpose(board)
    board, changed = move_left(board)
    board = transpose(board)
    return (board, changed)
    
def move_left(board):
    changed = False
    for row in range(4):
        nums = [num for num in board[row] if num != 0]
        i = 0
        merged_nums = []
        while i < len(nums):
            if i < len(nums)-1 and nums[i] == nums[i+1]:
                merged_nums.append(2*nums[i])
                i += 2
            else:
                merged_nums.append(nums[i])
                i += 1
        merged_nums = merged_nums + [0] * (4-len(merged_nums))
        if board[row] != merged_nums: 
            changed = True
            board[row] = merged_nums
    return (board, changed)

def move_right(board):
    changed = False
    for row in range(4):
        nums = [num for num in board[row] if num != 0]
        i = len(nums)-1
        merged_nums = []
        while i >= 0:
            if i > 0 and nums[i] == nums[i-1]:
                merged_nums.insert(0,2*nums[i])
                i -= 2
            else:
                merged_nums.insert(0,nums[i])
                i -= 1
        merged_nums = [0] * (4-len(merged_nums)) + merged_nums
        if board[row] != merged_nums: 
            changed = True
            board[row] = merged_nums
    return (board, changed)

def transpose(board):
    return [[board_row[col] for board_row in board] for col in range(4)]

board = createBoard()
print(*board, sep = '\n')
print()
game(board)