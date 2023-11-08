class Stack:
    def __init__(self):
        self.top = -1
        self.stack = ['','','','','','']
    
    def stack_empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, element):
        self.top += 1
        self.stack[self.top] = element

    def pop(self):
        if self.stack_empty():
            return 'stack underflow'
        
        self.top -= 1
        
        return self.stack[self.top + 1]

pilha = Stack()

pilha.push(4)
pilha.push(1)
pilha.push(3)
x = pilha.pop()
pilha.push(8)
y = pilha.pop()

print(pilha.stack[:pilha.top +1])