from Synttree import *
from auto import *

def create_token_queue(input):
    tokens = []
    id = ''
    for c in input:
        if c in ['(', ')', '.', '*', '+']:
            if id != '':
                tokens.append(id)
                id = ''
            tokens.append(c)
        else:
            id = id + c
    if id != '':
        tokens.append(id)
    return tokens

def create_postfix_token_queue(tokens):
    output_queue = []
    stack = []
    for token in tokens:
        if token == '(':
            stack.append('(')
        elif token == ')':
            while len(stack) > 0 and stack[-1] != '(':
                output_queue.append(stack.pop())
            stack.pop()
        elif token == '*':
            stack.append(token)
        elif token == '.':
            while len(stack) > 0 and stack[-1] == '*':
                output_queue.append(stack.pop())
            stack.append(token)
        elif token == '+':
            while len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '.'):
                output_queue.append(stack.pop())
            stack.append(token)
        else:
            output_queue.append(token)
    while len(stack) > 0:
        output_queue.append(stack.pop())
    return output_queue

def read_input(path):
    alph = []
    with open(path) as file:
        lines = file.readlines()
    for i in range(int(lines[0])):
        alph.append(lines[1 + i].strip())
    return alph, lines[int(lines[0]) + 1].strip()

def regex2DFA(path):
    ALPH, input = read_input(path)
    tokens = create_token_queue(input)
    post = create_postfix_token_queue(tokens)
    t = Tree(post)
    d = DFA(ALPH, t)
    print("Regex:", input)
    print("\nSyntax Tree (in-order traversal):")
    print(t)
    print("\nDFA Transitions:")
    print(d)

regex2DFA('input.txt')
