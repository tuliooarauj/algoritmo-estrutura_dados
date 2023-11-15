class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.end = None
        self._size = 0
    
    def append(self, element):
        node = Node(element)
        if self.head: #Checking if the line is empty
            
            node.prev = self.end
            node.prox = None
            self.end = node
        
        else:
            self.head = node #First insert
            self.end = self.head

        self._size +=1 

    def __len__(self):
        return self._size
            
    def pop(self):
        if self._size == 0:
            return 'Stack is empty'
        else:
            node = self.end.data
            self.end = self.end.prev #O topo agora é a próxima variável
            self._size -= 1
            return node
    
    def resolve_eqPolonesa(self, string):
        for i in string:
            if i >= '0' and i <= '9':
                self.append(i)
            elif i == '+' or i == '*' or i == '/' or i == '-':
                self.append(i)
            elif i == ')':

                last = float(self.pop())
                operator = self.pop()
                last_operand = float(self.pop())

                if operator == '+':
                    result = last_operand + last
                elif operator == '-':
                    result = last_operand - last
                elif operator == '*':
                    result = last_operand * last  
                elif operator == '/':
                    result = last_operand / last

                self.append(result)

        return result

if __name__ == '__main__':

    string = input()

    eq_pol = DoubleLinkedList()

    print(eq_pol.resolve_eqPolonesa(string))


    

