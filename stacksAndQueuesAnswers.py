from node import Stack, Queue
'''
For these exercises I used the classes implemented through Node,
rather than through python lists. It was just personal preference,
they can be solved either way.
'''

# ------------------- Stack answers -----------------------------
def isBalancedExpression(st):
    stack = Stack()
    value = ""
    for ch in st:
        if ch == "(" or ch == "[" or ch == "{":
            stack.push(ch)
        elif ch == ")" or ch == "]" or ch == "}":
            if stack.isEmpty():
                return False
            if stack.top() == oppositeBracket(ch):
                stack.pop()
            else:
                return False
    return True

def oppositeBracket(ch):
    #helpful function for "isBalancedExpression" function
    if ch == ")":
        return "("
    if ch == "]":
        return "["
    if ch == "}":
        return "{"


def switchStacks(s1, s2):
    s3 = Stack()
    size1 = s1.size()
    size2 = s2.size()
    while not s1.isEmpty():
        s3.push(s1.pop())
    while not s2.isEmpty():
        s3.push(s2.pop().getValue())

    for i in range(size2):
        s1.push(s3.pop().getValue())

    for i in range(size1):
        s2.push(s3.pop().getValue())

# ------------------- Queue answers ----------------------------
def reverse(q):
    s = Stack()
    while not q.isEmpty():
        s.push(q.dequeue().getValue())

    while not s.isEmpty():
        q.enqueue(s.pop().getValue())

def positiveAndNegative(q):
    negQ = Queue()
    posQ = Queue()

    item = None
    zero = False
    while not q.isEmpty():
        item = q.dequeue().getValue()
        if item < 0:
            negQ.enqueue(item)
        elif item > 0:
            posQ.enqueue(item)
        else:
            zero = True
    
    while not negQ.isEmpty():
        q.enqueue(negQ.dequeue().getValue())

    if zero:
        q.enqueue(0)
    while not posQ.isEmpty():
        q.enqueue(posQ.dequeue().getValue())
