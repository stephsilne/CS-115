''' Tic-tac-toe board quiz

Put your name and pledge here.  Then follow the rest of the instructions.

NOTE: By default, print adds a 'new-line' character after what it prints.
If you want to print but not go to the next line, use this special syntax:
print(something, end=' ').

QUESTION 1: what gets printed by the following function? Try it!
'''
def testPrint():
    print(1, end=' ') 
    print(2)
    print(3, end=' ')
    print(4)
    print() # causes a line break
    print(5)
'''
TO-DO: ANSWER 1 goes here, in this comment:





  
'''

'''
QUESTION 2: this is about tic-tac-toe boards, using '1' and '2' to represent the 
two players. First, have a look at this data
'''
empty_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board1 = [['1', ' ', '2'], ['1', ' ', ' '], ['2', ' ', ' ']]
boardFull = [['1', '1', '2'], ['2', '2', '1'], ['1', '2', '1']]
'''
You will write code print a board, so that board1 will print like this:
 1 |   | 2
-----------
 2 |   | 
-----------
 1 |   |  
and boardFull will print like this:
 1 | 1 | 2
-----------
 2 | 2 | 1
-----------
 1 | 2 | 1 
'''

def printBoard(board):
    '''print a board in the above format'''
    for row in range(0, 3):
        print(' ', end='')
        # TO-DO: write a for-loop to print the row



        
        print()
        # TO-DO: write an if-statement to print a horizontal line if needed

        

 
        

def test():
    printBoard(empty_board)
    print() # empty line between tests
    printBoard(board1)
    print()
    printBoard(boardFull)
    



