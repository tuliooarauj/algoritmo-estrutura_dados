class Box:
    def __init__(self, data):
        self.data = data
        self.next = None

class BoxStacking:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, element):

        box = Box(element)

        box.next = self.top #Older top is the new next element.

        self.top = box #New element is now top.
        self.size += 1
    
    def pop(self):    

        box_leaving = self.top.data
        self.top = self.top.next
        self.size -=1 

        return box_leaving
    
    def peek(self):
        peek = self.top
        
        if peek is None:
            pass
        else:
            return self.top.data
    
    def next_peek(self):

        next_peek = self.top.next

        if next_peek is None:
            pass
        else:
            return next_peek.data
    
def check_parity(n1, n2):
    
    if n1 is not None and n2 is not None:
        if (n1 % 2 == 0 and n2 % 2 == 0) or (n1 % 2 != 0 and n2 % 2 != 0):
            return True #Same parity

        else:
            return False #One is different
    else:
        pass

def box_ncount(n1, n2):

    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1
    
def main():

    stack = BoxStacking()
    
    n_stacks = int(input())

    i = 0
    j = 0

    while i < n_stacks:

        i += 1
        is_stacking = True

        while j != stack.size: #Zerando a pilha
            stack.pop()

        while is_stacking:   

            n_box = input()

            if n_box == '':
                pass
            else:
                n_box = int(n_box)
                parity_testing = True

                if n_box == 0: #End of stack
                    is_stacking = False

                else:

                    stack.push(n_box)

                    while parity_testing:

                        last_push = stack.peek()
                        secondLast_push = stack.next_peek()

                        parity_test = check_parity(last_push, secondLast_push)
                            
                        if parity_test:

                            stack.pop()
                            stack.pop()

                            new_box = box_ncount(last_push, secondLast_push)

                            stack.push(new_box)
                        
                        else:
                            parity_testing = False

        stack_size = stack.size
        stack_top = stack.peek()

        if stack_size == 0:
            stack_top = -1

        print(f'Pilha {i}: {stack_size} {stack_top}')

    
        

if __name__ == '__main__':
    main()
