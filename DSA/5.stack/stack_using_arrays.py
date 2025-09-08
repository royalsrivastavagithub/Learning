class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Length of stack:", len(s))
print("Top element of stack:", s.top())
print("Poped element from stack:", s.pop())
print("Is stack empty?", s.is_empty())
print("Poped element from stack:", s.pop())
print("Poped element from stack:", s.pop())
print("Is stack empty?", s.is_empty())
