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
        self.board = [["o " for x in range(size)] for y in range(size)]
        self.num_bad_seeds = num_bad_seeds
        self.name = name
        self.type = type
        self.guess_place = []
        self.add_place = []  
        self.rand_place = []      
    
    def print(self):
        """
        print the board
        """
        for row in self.board:
            print(" ".join(row))
            print()
    
    def add_seeds(self):
        while len(self.add_place) < self.num_bad_seeds:
            add_row = randint(0, self.size-1)
            add_col = randint(0, self.size-1)
            add_coord = [add_row, add_col]
            if add_coord not in self.add_place:
                self.add_place.append([add_row, add_col])
                self.board[add_row][add_col] = "@ " 
                                  
    def my_guess(self): 

        while True:                  
            while True:
                print("Please guess a row number:") 
                try:
                    guess_row = int(input("Guess a number in 0,1,2,3,4  "))       
                    if guess_row < 5:            
                        break        
                    elif guess_row > 4:
                        print("\nYour number must be between 0 to 4.")                   
                except ValueError:                 
                    print("\nYou can only enter a interger number!")
                    
            while True:
                print("\nPlease guess a column number:")
                try:
                    guess_col = int(input("Guess a number in 0,1,2,3,4  "))        
                    if guess_col < 5:            
                        break        
                    elif guess_col > 4:
                        print("\nYour number must be between 0 to 4.")                   
                except ValueError:                 
                    print("\nYou can only enter a interger number!")

            guess_coord = [guess_row, guess_col]
            if guess_coord in self.guess_place:
                print("You have already guessed that place, \nplease choose a different coordinate.")        
            else:
                break
   
        guess_coord = [guess_row, guess_col]  
        self.guess_place.append(guess_coord) 
        if guess_coord in self.add_place:       
            self.board[guess_row][guess_col] = " Y "
            print("\nYou got it! Thank you neighbor! \nNow I can plant something nice.") 
        else:
            self.board[guess_row][guess_col] = " X "
            print("\nYou missed, but donot give up, \nkeep going!")
            self.score
        print(f"Your current score is {}")

    
    def neighbor_rand_guess(self):
        rand_row = randint(0, self.size-1)
        rand_col = randint(0, self.size-1)
        rand_coord = [rand_row, rand_col]
        if rand_coord not in self.rand_place:
            self.rand_place.append([rand_row, rand_col])            
        if rand_coord in self.add_place:
            self.board[rand_row][rand_col] = " Y " 
        else:
            self.board[rand_row][rand_col] = " X "



    



     
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

    neighbor_board.my_guess()
    player_board.neighbor_rand_guess() 
    print(f"{play_name}")   
    player_board.print()
    print("neighbor")
    neighbor_board.print()   
    
    
    
new_game()
    

    
