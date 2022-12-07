#!python3
"""
Tic Tac Toe
Create a tic tac toe game that is enclosed entirely within a class instances.  The basic shell has been created, as well as the main block that will be used to execute the class method that runs the game.
This Tic Tac Toe game will be between 2 human players taking turns at the keyboard.
You need to create the methods and class variables that you will use.
There should be no code added outside of the class template definition.
The class property "moves" has been included.  This is a dictionary that will contain data that could be used in future machine learning applications to create a smart computer player. All moves will be recorded in order and then the winner will be recorded at the end of the game as either 0 (first player), 1 (second player) or -1 (if a tie)


One idea would be to create a board like so:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

or you could also use the keypad to help choose positions:

7 | 8 | 9
---------
4 | 5 | 6
---------
1 | 2 | 3

To enhance your display, you can access unicode symbols
╩ for example: https://altcodeunicode.com/
"""

class tictactoe:
    # class variables 
    record = {
        'winner' : None,
        'moves' : []
    }


    # class methods
    def run(self):
        pass

    def __init__(self):
        self.run()

game = tictactoe()