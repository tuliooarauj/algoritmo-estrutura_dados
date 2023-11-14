class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, element):
        
        if self.head: #Checking if the line is empty
            pointer = self.head
            while pointer.next: #pointer.next != from None
                pointer = pointer.next

            pointer.next = Node(element) #Pointer var arrives at the end of the line and insert the new element in pointer.next.

        else:
            self.head = Node(element) #First insert

        self._size +=1 

    def __len__(self):
        return self._size
    
    def _get_node(self, index):
        pointer = self.head
        i = 0
        while i < (index - 1): 
            i += 1
            if pointer:
                pointer = pointer.next # "Walking" trought the list untill arrives wanted index
            else:
                raise IndexError('list index out of range')
            
        return pointer

    def __getitem__(self, index): #Sobrecarga de operador, atribuir o operador natural [] para o comportamento de indexação.
        # a = lista[6]
        pointer = self._get_node(index)

        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, element):
        # lista[5] = 9
        pointer = self._get_node(index)

        if pointer: #Checking if there is element in pointer
            pointer.data = element
        else:
            raise IndexError('list index out of range')

    def index(self, element): #Linear search [O(n)]
        #Method to return the index of an element 
        pointer = self.head
        i = 0

        while pointer: #Searching element in list
            if pointer.data == element:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError('{} is not in list'.format(element))
    
    def insert(self, index, element):
        node = Node(element)
        if index == 0: #Head insert
            node.next = self.head #The new next element from new head is the former head
            self.head = node #New head is the new element
        else:
            pointer = self._get_node(index - 1)
            node.next = pointer.next
            pointer.next = node

        self._size += 1
            
    def remove(self, element):
        if self.head is None:
            raise ValueError('{} is not in list'.format(element))
        elif self.head.data == element:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            prev = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == element:
                    prev.next = pointer.next #Linking prev from element to next from element (1 - [2] - 3 --> 1 - 3)
                    pointer.next = None
                    self._size -= 1
                    return True
                else:
                    prev = pointer # "Walking" trought the list (pointer is always 1 position ahead prev)
                    pointer = pointer.next
            
            raise ValueError('{} is not in list'.format(element))
                
    def __repr__(self) -> str:
        r = ''
        pointer = self.head

        while pointer:
            r = r + str(pointer.data) + '->'
            pointer = pointer.next
        
        return r

if __name__ == '__main__':
    lista = LinkedList()

    lista.append(10)
    lista.append(20)
    lista.append(30)


