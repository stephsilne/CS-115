# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("You won! You're not as bad as I thought!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print('I won! haHA!')

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    i = 0
    '''initializes i to zero for iterations'''
    print("Welcome to Nim! You'd better play optimally or you'll be crying to your mommy!")
    while True:
        '''while true, keep looping until a break hits'''
        try:
            num_piles = int(input('How many piles do you want to play with? '))
            '''prompts the user for the number piles that they want through a try and except clause'''
            break
            '''break out of the loop if the except clause of the loop is not called upon'''
        except ValueError:
            '''if a valueError occurs then, the except clause is prompted, printing the prompt below and relooping due to the True argument in the while loop'''
            print('not a valid choice. ')
            '''tells the user they have not submitted a valid choice, i.e. letter or a space'''

    piles = [0] * num_piles
    '''initiates piles to be an 'empty' list consisting 'num_piles' amount of elements'''
    while i < len(piles):
        '''while i = 0 is less than the length of piles'''
        try:
            piles[i] = int(input("How many in pile " + str(i) +  "? " ))
            '''prompt the user for how many coins in each pile, reassigning the ith pile by the integer value given as input'''
            i += 1
            '''increments i so that each element of piles is prompted for how many coins'''
        except ValueError:
            '''if a ValueError occurs, such that the input given is a space or letter, prints the prompt below'''
            print('not a valid choice')
                                        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    m = 0
    '''initializes m to zero for iterations'''
    while m < len(piles):
        '''while m is less than the length of piles'''
        print("pile " +  str(m) +  " = " + str(piles[m]))
        '''print the prompt that tells the user how many is in each pile'''
        m += 1
        '''increments m as to display each pile from 0 to len(piles)'''


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    while True:
        '''while True, as to keep looping the prompt'''
        try:
            get_p = int(input('Which pile? '))
            '''ask the user for input of which pile they want, establishes get_p as the int of this given string'''
            assert(0 <= get_p <= num_piles -1)
            '''assert that the number they enter is between 0 and num_piles - 1'''
            break
            '''breaks out of loop if no except clause is prompted'''
        except (AssertionError,ValueError):
            '''if the assertion is incorrect or a valueError is given by a user submitting a space or character,print the prompt below and relooop'''
            print('not a valid choice.')
            '''tells the user that they have not given a valid choice and reloops'''
            
    return get_p
    '''after the break in the loop, returns the value for which pile that was given'''


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    while True:
        '''while True, keep looping until a break hits'''
        try:
            get_n= int(input('How many? '))
            '''prompts the user for how many coins they want to remove, establishing get_n as the int of this given string'''
            assert(1 <= get_n <= piles[pnum])
            '''asserts that get_n is between 1 and the amount in the actual pile'''
            break
            '''breaks out of the loop if no except clause is prompted'''
        except (AssertionError,ValueError):
            '''if an AssertionError or ValueError are given by the prompted number of coins given as input, print the message below and reloop'''
            print('not a valid choice.')
            '''tells the user that the input given was invalid'''

    return get_n
    '''after the break out of the loop, return from memory get_n'''


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles
    
    nim_sum = 0
    '''establishes nim_sum to zero for iteration purposes'''
    for p in piles:
        '''for each pile in piles'''
        nim_sum ^= p
        '''compute the bitewise exclusive or of each pile, so that nim_sum is the bitewise exclusive or of each pile altogether'''
    return nim_sum
    '''returns the nim_sum(nim-sum)'''
               

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles
    
    for ind in range(len(piles)):
        '''for each index in the range from 0 to the length of piles'''
        if game_nim_sum()^piles[ind] < piles[ind]:
            '''if pilesum of piles[ind] is less than the amount in coins of the same pile'''
            return (ind,piles[ind] - (game_nim_sum()^piles[ind]))
            '''return the tuple containing the index or pile number, and the amount to remove: amt of coins minus the pilesum'''
    for i in range(len(piles)):
        '''if there is no optimal play, for each index in the range from 0 to the length of the list of piles'''
        if piles[i] != 0:
            '''as long as the pile is non zero'''
            return (i,1)
            '''return the tuple containing its piles index or the pile number, and 1'''
                        
                
def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    print('My turn....get ready to lose, you big baby!')
    '''tells the user it is the computers turn'''
    op = opt_play()
    '''establishes op as the function call to opt_play()'''
    piles[op[0]] = piles[op[0]]^game_nim_sum()
    '''updates the pile to equal the pilesum, simulating optimal play by the computer'''
    print('I removed ' + str(op[1]) + ' from pile ' + str(op[0]))
    '''tells the user it removed op[1] or how many coins it removed and from which pile'''
    
    

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
