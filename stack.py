class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

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