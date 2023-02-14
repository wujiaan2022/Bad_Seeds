# Help Neighbor-Bad Seeds

Bad seeds is a Python terminal game, a "episode" of the future series game "Help Neighbor", which runs in the Code Institute mock terminal on Heroko.

It's time to help each other instead of killiing or destroy each other. 
Future series could be "Help Ocean", "Help Forest", "Help Mankind", etc.

In this game, player and the neighbor (computer) will help each other to dig out the bad seeds in their garden. Each seed occupies one square on the board.

Here is the live version of my project.
 ![game on different size of screen](images/pp3_image_0.jpg)

 # How to play
 In thsi game, player enter the name, and two boards and the bad seeds are randomly generated. 
 Player can see the bad seeds on his/her side which indicate by a "#" sign, while computer side's bad seeds are hidden.
 Player will be prompt to guess where the bad seeds are by entering row and column number, then computer will randomly generate a coordinate.
 `Hit will be marked as "$"`, score will be incremented accordingly, while `miss will be shown as "X"`.
 Game will automatically stop when one side has dig out all the bad seeds.
 Then the winner will be annouced. Game over.

 # Feature

 ## Existing Feature
 - Random Boards generation
    - Bad Seeds are randomly placed on both player and computer's boards.
    - Computer side of guess coordinate is also randomly generated.
    - Make sure all the random set (row and column) are no duplicates.
    - Player cannot see where the computer's bad seeds are.

![Random board generation](./images/pp3_image_2.PNG)

- Input Validation
    - The guess row and col must be within the size of grid.
    - Input must be numbers.
    - Player cannot guess the same spot twice.

![Input Validation](./images/pp3_image_4.PNG)
- Data maitained in class instances

## Futue Feature
- Allow player to select board size and numbers of bad seeds.
- Allow player position the bad seeds themselves.

# Data Model 

- The code use a Board class as model and has two instances to hold the Player and the computer's boards. 
    - The Board class stores the board size, the number of bad seeds, name and type. 
    - Has methods to print board, creat randdom non repeating numbers for add seeds and computer guess.
    - Has player guess method in which input will be prompt and validated, miss and hit will be marked, and score will be incremented.
    - Has computer playing method which generates random non repeating coordinate, mark miss and hit, and add score.

## Testing

I have manually tested this project by doing the following:
- Passed the code through a PEP8 linter and confirmed there are no problems.
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same coordinate twice.
- Tested in my Local terminal and Code Institute Heroko terminal.

### Bugs
#### Solved Bugs
- I was stuck for two day in one part of validation code. it turned out it was a mistake, in which i appended the random sublist in a wrong main list.
- In one part of code, the game should have automatically stopped when one side's score equal to the number of bad seeds. But it didn't work out as i planed. So I changed the sequence of if else statment in the while loop, then it worked.
### Remaining Bugs
- No bugs remaining

### Validator Test
- PEP8
    - No errors were returned from https://pep8ci.herokuapp.com/
    - Note: error "173: E501 line too long (84 > 79 characters)" should not be a major problem

# Deployment 

This project was depoyed using Code Institute's mock termonal for Heroku. 
- Steps for deployment:
    - fork or clone this reposrcory
    - Create a new Heroku app
    - Set the buildbacks to `Python` and `NodeJS` in that order
    - link the Heroku app to the repository
    - Click on **Deploy** 

# Credits

- Code Institute for the deployment terminal 


