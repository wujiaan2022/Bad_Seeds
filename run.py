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
        self.success_place = []      
    
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
                print("\nPlease guess a row number:") 
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
            self.success_place.append(guess_coord)       
            self.board[guess_row][guess_col] = "Y "            
            print("\nYou got it! Now your neighbor can plant more beautiful flowers.")
            scores["player"] += 1            
        else:
            self.board[guess_row][guess_col] = "X "
            print("\nYou missed, don't give up, keep going!")             

    def neighbor_rand_guess(self):
        rand_row = randint(0, self.size-1)
        rand_col = randint(0, self.size-1)
        rand_coord = [rand_row, rand_col]
        if rand_coord not in self.rand_place:
            self.rand_place.append([rand_row, rand_col])            
        if rand_coord in self.add_place:
            self.success_place.append(rand_coord)
            self.board[rand_row][rand_col] = "Y "
            print("\nYour neighbor did it! \nNow you can plant more beautiful flowers.")
            scores["computer"] += 1 
        else:
            self.board[rand_row][rand_col] = "X "
            "\nYour neighbor missed, but she/he will keep going!"
  
    
def new_game():
    """
    Starts a new game. Sets the board size and numbers of badd seeds, 
    resets the scores and initialises the baords.
    """
    size = 5
    num_bad_seeds = 4
    scores["neighbor"] = 0
    scores["player"] = 0
    print("-" * 20)
    print("Welcom! You and your neighbor will help each other to dig out bad seeds from your garden! Isn't that exciting!")
    print(f"Your garden size is {size}. \nNumber of bad seeds is {num_bad_seeds}")
    print("Top left coner is row: 0, col: 0")
    print("-" * 20)
    play_name = input("Please enter your name: \n")
    print("-" * 20)

    neighbor_board = Board(size, num_bad_seeds, "neighbor", type="neighbor")
    player_board = Board(size, num_bad_seeds, play_name, type="player")

    print("\nneighbor's garden")
    print()
    neighbor_board.add_seeds()     
    neighbor_board.print() 
    print(f"\n{play_name}'s garden")
    print() 
    player_board.add_seeds()   
    player_board.print()       

    while True: 
        neighbor_board.my_guess()   
        my_score = scores["player"]
        print(f"Your current score is: {my_score}")
        print("\nYour neighbor's garden")
        neighbor_board.print()      

        player_board.neighbor_rand_guess()
        neighbor_score = scores["computer"]
        print(f"Her/his current score is: {neighbor_score}")
        print(f"\n{play_name}'s garden")   
        player_board.print()   
        
        if scores["player"] <= 3 or scores["computer"] <= 3:
            a = input("Keep going? y or n ")
            a = a.lower()
            if a == "y":
                continue
            elif a == "n":
                break
        else:
            print("Game Over!")
            if my_score > neighbor_score:
                print("In this round you win!")
            elif my_score == neighbor_score:
                print("In this round you are even!")
            elif my_score < neighbor_score:
                print("In this round your neighber win!")
       
            


def game_round():
    while True:
        new_game()
        a = input("Would you like another round? y or n ")
        a = a.lower()
        if a == "y":
            continue
        elif a == "n":
            break
        else:
            print("Enter either y or n ")

game_round()




    

    
