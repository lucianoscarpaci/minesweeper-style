import random

#board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        # helper function
        self.board = self.create_board() #planting the bombs

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

#play the game
def start(dim_size=10, num_bombs=10):
    pass