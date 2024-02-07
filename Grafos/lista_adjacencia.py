class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0
    
    def insere(self, element):
        
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

class Grafo:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[]] * self.vertice

    def adiciona_aresta(self, u, v):
        if self.grafo[u-1] == []:
            self.grafo[u-1] = LinkedList()             
            self.grafo[u-1].insere(v)
        else:
            self.grafo[u-1].insere(v)

    def mostra_grafo(self):
        for vertice in self.grafo:
            print(vertice)


g = Grafo(3)

g.adiciona_aresta(1,2)
g.adiciona_aresta(1,3)
g.adiciona_aresta(2,1)
g.adiciona_aresta(2,3)

g.mostra_grafo()