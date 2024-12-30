from typing import Any

class Stack:
    def __init__(self):
        self.stack = []
        self.size = len(self.stack)
    def update_size(self):
        self.size = len(self.stack)
    def get_size(self):
        return self.size
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, number: Any): # time: O(1)
        self.stack.append(number)
        self.update_size()
    def pop(self): # time: O(N)
        if self.size > 0:
            popped = self.stack.pop()
            self.update_size()
            return popped
        else:
            print("cannot pop empty stack")
    def peek(self):
        return self.stack[-1]
    def print(self):
        if self.size > 0:
            for i in range(0, self.size):
                print(self.stack[i])
        else:
            raise Exception('empty stack')

# stack = Stack()
# stack.pop()
# print(stack.get_size())
# stack.push(1)
# stack.push(2)
# print(stack.pop())
# stack.push(3)
# print(stack.get_size())
# stack.print()

'''
leetcode 20
valid parentheses
given a string s containing just the characters (, ), {, }, [, ], determine if the input string is valid
an input string is valid if
open brackets are closed by the same type of brackets
open brackets are closed in the correct order
every close bracket has a corresponding open bracket of the same type
input s = "()"
output = true
input s = "()[]{}"
output = true
input s = "(]"
output = false
input s = "([])"
output = true
'''
def valid_parentheses(parens):
    stack = Stack()
    openings = "([{"
    closings = ")]}"
    for i in range(0, len(parens)):
        current = parens[i]
        if current in openings:
            stack.push(current)
        elif current in closings and stack.get_size() == 0 or openings.index(stack.peek()) != closings.index(current):
            return False
        elif current in closings and openings.index(stack.peek()) == closings.index(current):
            stack.pop()
    return stack.get_size() == 0

s = "()[]{}"
print(valid_parentheses(s))

'''
converting decimal numbers to binary numbers
https://runestone.academy/ns/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html
'''
def decimal_to_base(number, base):
    digits = "0123456789ABCDEF"
    result = Stack()
    while number > 0:
        result.push(number % base)
        number = number // base
    binarystring = ''
    while not result.is_empty():
        binarystring = binarystring + digits[result.pop()]
    return binarystring
print(decimal_to_base(233, 2))
print(decimal_to_base(233, 16))

'''
infix, prefix, postfix
https://runestone.academy/ns/books/published/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html
'''
def infixToPostfix(infixExpr):
    prec = {}
    prec['**'] = 4
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    stack = Stack()
    result = []
    infixExpression = infixExpr.split()
    for i in range(0, len(infixExpression)):
        currentToken = infixExpression[i]
        if currentToken in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or currentToken in '0123456789':
            result.append(currentToken)
        elif currentToken == '(':
            stack.push(currentToken)
        elif currentToken == ')':
            topToken = stack.pop()
            while topToken != '(':
                result.append(topToken)
                topToken = stack.pop()
        else:
            while (not stack.is_empty()) and (prec[stack.peek()] >= prec[currentToken]):
                result.append(stack.pop())
            stack.push(currentToken)
    while not stack.is_empty():
        result.append(stack.pop())
    return ''.join(result)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix(" 5 * 3 ** ( 4 - 2 ) "))

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))

