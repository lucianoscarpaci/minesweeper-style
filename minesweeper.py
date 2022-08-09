import random
import re

#board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        # helper function
        self.board = self.create_board() #planting the bombs
        self.assign_values_in_board()

        # set to keep track of which locations are uncovered
        self.dug = set()
    
    def create_board(self):

        #make new board appear
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs
        bombs_in_board = 0
        while bombs_in_board < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # return random int N s.t. a <= N <= b
            row = loc // self.dim_size # we want num of times dim_size can go into loc
            col = loc % self.dim_size # we want remainder to tell us what index in row to loop in col

            if board[row][col] == '*':
                # this means a bomb is already planted
                continue

            board[row][col] = '*' #plant the bomb
            bombs_in_board += 1

        return board
    
    def assign_values_in_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_near_num_bombs(r, c)

    def get_near_num_bombs(self, row, col):
        #iterate through each of the positions and sum near num bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)
        near_num_bombs = 0
        #check outofbounds using max and min indexes
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    near_num_bombs += 1

        return near_num_bombs

    def dig(self, row, col):

        self.dug.add((row, col)) # keep track of digging

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put board in a string

        
#play the game
def start(dim_size=10, num_bombs=10):
    #create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        input_ln = re.split(',(\\s)*', input("Where do you dig? Input as row,col: "))
        row, col = int(input_ln[0]), int(input_ln[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Error")
            continue

    # if its valid dig
    safe = board.dig(row, col)
    if not safe:
        break # game over

    # check ways to end loop
    if safe:
        print("YOU WIN!")
    else:
        print("GAME OVER")
        # lets show the board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    start()