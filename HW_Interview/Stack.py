class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or stack.pop() != bracket_pairs[char]:
                return False

    return stack.is_empty()

def is_balanced_optimized(expression):
    stack = Stack()
    opening_brackets = "([{"
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in bracket_pairs.values():
            if stack.is_empty() or stack.pop() != char:
                return False

    return stack.is_empty()

# Testing
balanced_examples = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
]

unbalanced_examples = [
    "}{",
    "{{[(])]}}",
    "[[{())}]",
]

for example in balanced_examples:
    if is_balanced_optimized(example):
        print(f"{example} - Balanced")
    else:
        print(f"{example} - Not Balanced")

for example in unbalanced_examples:
    if is_balanced_optimized(example):
        print(f"{example} - Balanced")
    else:
        print(f"{example} - Not Balanced")
