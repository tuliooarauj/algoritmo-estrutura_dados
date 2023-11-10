class Box:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class BoxStacking:
    def __init__(self) -> None:
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

        return box_leaving.data
    
    def peek(self):

        top = self.top.data
        return top.data
    
    def next_peek(self):

        next_peek = self.top.next

        if next_peek is None:
            pass
        else:
            return next_peek.data.data
    
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
    is_stacking = True

    while i < n_stacks:

        i += 1

        while is_stacking:   

            n_box = int(input())

            if n_box == 0: #End of stack
                is_stacking = False

            else:
                
                box = Box(n_box)

                stack.push(box)

                last_push = stack.peek()
                secondLast_push = stack.next_peek()

                parity_test = check_parity(last_push, secondLast_push)

                if parity_test:

                    stack.pop()
                    stack.pop()

                    new_box = box_ncount(last_push, secondLast_push)

                    stack.push(new_box)
        

if __name__ == '__main__':
    main()
