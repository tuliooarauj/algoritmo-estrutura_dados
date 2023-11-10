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

        box.next = self.top #Antigo topo é o novo próximo elemento.

        self.top = box #Novo elemento é o atual topo.
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
        return next_peek.data
    
def main():

    stack = BoxStacking()
    
    n_stacks = int(input())

    i = 1

    while i <= n_stacks:

        while True: 

            n_box = int(input())

            if n_box == 0: #Fim da pilha
                pass

            else:
                
                box = Box(n_box)

                stack.push(box)










        i += 1

if __name__ == '__main__':
    main()
