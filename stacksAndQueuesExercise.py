#Stack exercises
def isBalancedExpression(st):
    '''
    Write a function that recieves a string that contains
    parenthesis, brackets and curly brackets. the function will 
    return True or False whether or not the different types
    of brackets are balanced, meaning opening and closing
    in the correct order.

    Example:
    "([{4[2]}abc])" ----> True 
    "[de{3{(])8}]" ----> False
    '''

def switchStacks(s1, s2):
    '''
    Given two stacks, s1 and s2, write a function that switches between
    the contents of each stack, moving the values in s1 to s2 and vice versa.
    The order must remain the same.
    '''

#Queue exercises
def reverse(q):
    '''
    Write a function that takes a queue q and reverses the order 
    of the values in the same queue.

    Example:
    q ----> 1 < 2 < 3 < 4
    after function:
    q ----> 4 < 3 < 2 < 1
    '''

def positiveAndNegative(q):
    '''
    Write a function that takes a queue q and returns it so that 
    all of the negative numbers are concentrated, in their original order,
    at the beginning of the queue, and the positive numbers are concentrated
    at the end of the queue, also in their original order. The number 0, 
    if exists in the queue, will appear in the middle once 
    (regardless of the number of times it appears in the queue).

    Example:
    q ----> -2 < 6 < 0 < -1 < 9 < -3 < 7
    after function:
    q ----> -2 < -1 < -3 < 0 < 6 < 9 < 7
    '''