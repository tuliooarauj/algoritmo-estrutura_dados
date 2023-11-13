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

    def __getitem__(self, index): #Sobrecarga de operador, atribuir o operador natural [] para o comportamento de indexação.
        # a = lista[6]
        pointer = self.head
        i = 0
        while i < index:
            i += 1
            if pointer: #!= from None
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, index, element):
        # lista[5] = 9
        pointer = self.head
        i = 0
        while i < index:
            i += 1
            if pointer: #!= from None
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
        
        if pointer:
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


    
lista = LinkedList()

'''lista.append(10)
lista.append(15)
print(len(lista))
print(lista[0])
print(lista[1])
lista[1] = 1000
print(lista[1])
lista.append(240200000000)
print(lista[2])
print(f'Indice do elemento 10: {lista.index(10)}')
print(f'Indice do elemento 240200000000: {lista.index(240200000000)}')'''
