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
        return self.top.data