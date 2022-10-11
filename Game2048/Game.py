from random import random, randint

class Game_2048:
    def __init__(self):
        row = [0]*4
        self.board = [row[:] for i in range(4)]
        self.score = 0

        loc1 = [randint(0,3), randint(0,3)]
        loc2 = [randint(0,3), randint(0,3)]

        while loc2 == loc1:
            loc2 = [randint(0,3), randint(0,3)]

        if random() <= 0.1:
            self.board[loc1[0]][loc1[1]] = 4
        else:
            self.board[loc1[0]][loc1[1]] = 2

        if random() <= 0.1:
            self.board[loc2[0]][loc2[1]] = 4
        else:
            self.board[loc2[0]][loc2[1]] = 2

    def game(self):
        print(*self.board,sep='\n')
        while True:
            self.turn()

            if self.board == 0:
                print('\nYou lose!')
                break
            print('\n', *self.board, sep='\n')
            print(f"Score: {self.score}\n")
            if any(2048 in row for row in self.board):
                print('\nYou win!')
                break

    def insertNewNumber(self, board):
        if any(0 in row for row in board):
            temp = board.copy()
            loc = [randint(0,3), randint(0,3)]
            while temp[loc[0]][loc[1]] != 0:
                loc = [randint(0,3), randint(0,3)]
            if random() <= 0.1:
                temp[loc[0]][loc[1]] = 4
            else:
                temp[loc[0]][loc[1]] = 2
            return temp

    def turn(self):
        moves = {
            'w' : self.move_up(self.board[:]),
            'a' : self.move_left(self.board[:]),
            's' : self.move_down(self.board[:]),
            'd' : self.move_right(self.board[:])
        }

        move = 'x'
        while move not in moves.keys():
            move = str(input('Enter move: '))

        if all(self.board==move_board for move_board in moves.values()):
            self.board = 0
        else:
            self.board = self.insertNewNumber(moves[move])

    def move_down(self, copy):
        return self.transpose(self.move_right(self.transpose(copy)))

    def move_up(self, copy):
        return self.transpose(self.move_left(self.transpose(copy)))

    def move_left(self, copy):
        for row in range(4):
            nums = [num for num in copy[row] if num != 0]
            i = 0
            merged_nums = []
            while i < len(nums):
                if i < len(nums)-1 and nums[i] == nums[i+1]:
                    merged_nums.append(2*nums[i])
                    self.score += 2*nums[i]
                    i += 2
                else:
                    merged_nums.append(nums[i])
                    i += 1
            merged_nums = merged_nums + [0] * (4-len(merged_nums))
            copy[row] = merged_nums
        return copy

    def move_right(self, copy):
        for row in range(4):
            nums = [num for num in copy[row] if num != 0]
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
            copy[row] = merged_nums
        return copy

    def transpose(self, copy):
        return [[board_row[col] for board_row in copy] for col in range(4)]

    def getBoard(self):
        return self.board


