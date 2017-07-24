
def hanoiTowers(discNum, fromPole, withPole, toPole):
    '''
    The game "Towers of Hanoi" uses three poles. A number of discs
    is stacked in decreasing order from the bottom to the top of one
    pole, i.e. the largest disc at the bottom and the smallest one on top.

    The aim of the game is to move the tower of discs from one pole to another pole. 

    The following rules have to be obeyed:
    1. Only one disc may be moved at a time.
    2. Only the most upper disc from one of the poles can be moved in a move
    3. It can be put on another pole, if this pole is empty or if the most upper
       disc of this pole is larger than the one which is moved.

    Write a function that recieves an attribute discNum, and prints the series
    of moves required to move the discs from one pole to another, using three
    poles: one which has the discs at the beginning- fromPole, one which is used
    mainly to assist- withPole, and one which the discs should be moved to- toPole.

    Animation of this process can be seen here: http://towersofhanoi.info/Animate.aspx
    '''

def reverse(q):
    '''
    Write a function that takes a queue q and reverses the order 
    of the values in the same queue.

    Example:
    q ----> 1 -> 2 -> 3 -> 4
    after function:
    q ----> 4 -> 3 -> 2 -> 1
    
	Extra: don't use any other data structures!
    '''
