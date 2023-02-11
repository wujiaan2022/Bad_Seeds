from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    main board setting of size, player's name, numbers of bad seeds, 
    board type(player's board or neighbor's). Has methods for 
    adding bad seeds and guesses and print the board
    """
    def __init__(self, size, num_bad_seeds, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_bad_seeds = num_bad_seeds
        self.name = name
        self.type = type
        self.guess_place = []
        self.add_place = []   
    
    def print(self):
        """
        print the board
        """
        for row in self.board:
            print(" ".join(row))
    
    def add_seeds(self):
        while len(self.add_place) < self.num_bad_seeds:
            add_row = randint(0, self.size-1)
            add_col = randint(0, self.size-1)
            add_coord = [add_row, add_col]
            if add_coord not in self.add_place:
                self.add_place.append([add_row, add_col])
                self.board[add_row][add_col] = "@" 
                                  
    def make_guess(self):        
        print("Please guess a row number:")
        print()
        while True:
            try:
                guess_row = int(input("Guess a number in 0,1,2,3,4  "))       
                if guess_row < 5:            
                    break        
                elif guess_row > 4:
                    print("Your number must be between 0 to 4.")                   
            except ValueError:                 
                print("You can only enter a interger number!")

        print("Please guess a column number:")
        print()
        while True:
            try:
                guess_col = int(input("Guess a number in 0,1,2,3,4  "))        
                if guess_col < 5:            
                    break        
                elif guess_col > 4:
                    print("Your number must be between 0 to 4.")                   
            except ValueError:                 
                print("You can only enter a interger number!")
        self.guess_place.append([guess_row, guess_col])
        
 
     
def new_game():
    """
    Starts a new game. Sets the board size and numbers of badd seeds, 
    resets the scores and initialises the baords.
    """
    size = 5
    num_bad_seeds = 4
    scores["neighbor"] = 0
    scores["player"] = 0
    print("-" * 35)
    print("Welcom")
    print(f"Board size is {size}. Number of badd seeds is {num_bad_seeds}")
    print("Top left coner is row: 0, col: 0")
    print("-" * 35)
    play_name = input("Please enter your name: \n")
    print("-" * 35)

    neighbor_board = Board(size, num_bad_seeds, "neighbor", type="neighbor")
    player_board = Board(size, num_bad_seeds, play_name, type="player")
    print(f"{play_name}") 
    player_board.add_seeds()   
    player_board.print()
    print("neighbor")
    neighbor_board.add_seeds()     
    neighbor_board.print()

    neighbor_board.make_guess()
    if neighbor_board.guess_place[guess_row][guess_col] == neighbor_board.add_place[add_row][add_col]:
        neighbor_board.board[add_row, add_col] = "#"
    print("You got it! Now I can plant good seed.") 

    
    

    
new_game()
