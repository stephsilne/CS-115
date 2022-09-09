#
# life.py - Game of Life lab
#
# Name: Stephaan Silne
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    '''creates and returns a new 2D list of height rows and width columns with all elements equaling 0'''
    A = []
    '''initializes A to be an empty list'''
    for row in range(height):
        '''for every row of the range of height'''
        A += [createOneRow(width)]
        '''increments A for every iteration of the list createOneRow(width)'''
    return A
    '''returns the final board A'''
    
def printBoard( A ):
    '''this function prints the 2d list-of-lists A without spaces, using (sys.stdout.write)'''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
        
def diagonalize(width,height):
    '''creates a newBoard of diagonal live cells in an otherwise empty board'''
    A = createBoard(width,height)
    '''initializes A to be an empty board of given width and height'''
    for row in range(height):
        '''for every iterated row of given height'''
        for col in range(width):
            '''for every iterated col of given width'''
            if row == col:
                '''if the row and col of a given cell are equal'''
                A[row][col] = 1
                '''that cell should be equal to 1'''
            else:
                A[row][col] = 0
                '''otherwise it should be left a dead cell (0)'''
    return A
    '''returns the final diagonliazed board'''

def innerCells(w,h):
    '''takes in a width w and height h and returns a 2d array of live cells except outer edges'''
    A = createBoard(w,h)
    '''sets A to be a board of the same width and height given'''
    for row in range(1,h-1):
        '''for every iterative row between the first and last row'''
        for col in range(1,w-1):
            '''for every iterative column between the first and last column'''
            A[row][col] = 1
            '''set each cell within these borders to equal 1'''
    return A
    '''returns the final board A'''

def randomCells(w,h):
    '''returns an array of randomly assigned 1's and 0's except the outer edge of the array'''
    A = createBoard(w,h)
    '''initializes A as a board of width w and height h'''
    for row in range(1,h-1):
        '''for every iterative row between the first and last row'''
        for col in range(1,w-1):
            '''for every iterative col between the first and last col'''
            A[row][col] = random.choice([0,1])
            '''each cell of A should be a random val; either 1 or 0'''
    return A
    '''returns the final board'''

def copy(A):
    '''deep copies a 2d array A to createa new array'''
    B = createBoard(len(A),len(A[0]))
    '''initializes B to be an empty board of the same width and length of A'''
    for row in range(1,len(A)-1):
        '''for every iterative row between the first and last row'''
        for col in range(1,len(A[0])-1):
            '''for every iterative column between the first and last column'''
            B[row][col] = A[row][col]
            '''each cell should equal each cell within A, creating a copy'''
    return B
    '''returns the new deep copy'''

def innerReverse(A):
    '''that takes an old 2d array (or "generation") and then creates a new (inverted) generation of the same shape and size'''
    R = copy(A)
    '''creates a copy of A, being R'''
    for row in range(1,len(R)-1):
        '''for every row between the first and last'''
        for col in range(1,len(R[0])-1):
            '''for every column between the first and last'''
            if R[row][col] == 1:
                '''if the cell equals 1'''
                R[row][col] = 0
                '''set the cell to equal 0'''
            else:
                R[row][col] = 1
                '''otherwise the cell should equal 1 if it is 0'''
    return R
    '''returns the final copy'''

def next_life_generation(A):
    '''makes a copy of A and then advances one generation of Conways game
        of life within the *inner cells* of that copy. the outer edges always
        stay 0'''
    N = copy(A)
    '''creates a copy of the given board'''
    for row in range(1,len(N)-1):
        '''for every row between the first and last row of the board'''
        for col in range(1,len(N[0])-1):
            '''for every column between the first and last column of the board'''
            if countNeighbors(row,col,A) < 2:
                '''if a cell has fewer than 2 live neighbors'''
                N[row][col] = 0
                '''that cell should die'''
            if countNeighbors(row,col,A) > 3:
                '''if a cell has greater than 3 live neighbors'''
                N[row][col] = 0
                '''that cell should die due to overcrowding'''
            if countNeighbors(row,col,A) == 3 and A[row][col] == 0:
                '''if the amount of neighbors are exactly 3 and the cell is dead'''
                N[row][col] = 1
                '''the cell should then become alive'''
    return N
    '''return the new generation of the board'''

def countNeighbors(row,col,A):
    '''returns the number of live nieghbors for a cell in board A at a particular col and row'''
    countNeighbors = 0
    '''sets the counter to zero'''
    for x in range(-1,2):
        '''for interator x from [-1,0,1]'''
        for y in range(-1,2):
            '''for iterator y from [-1,0,1]'''
            if x != 0 or y != 0:
                '''if both x and y do not equal zero'''
                countNeighbors += A[row +x][col+y]
                '''the counter should be incremented'''
    return countNeighbors
    '''returns the final count'''
                                        
