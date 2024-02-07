from lista_adjacencia import *

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def push(self, vertice):
        node = Node(vertice)

        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self._size += 1

    def remove(self):
        if not self._size == 0:
            removed = self.head
            self.head = self.head.next

        self._size -=1

        return removed


def bfs(grafo):

    visitado = [False] * grafo.vertice
    antecessor = [False] * grafo.vertice
    vertices = Queue()

    for i in range(grafo.vertice):
        if not visitado[i]:
            vertices.push(i)
            visitado[i] = True

            while vertices._size > 0:
                
                vertice_visitado = vertices.remove()

                for u in grafo.mostra_adj(vertice_visitado):
                    if not visitado[u]:
                        visitado[u] = True
                        antecessor[u] = vertice_visitado
                        
                        vertices.push(u)

    visitado = []
    antecessor = []

g =  Grafo(4)    

g.adiciona_aresta(0,1)
g.adiciona_aresta(0,2)
g.adiciona_aresta(1,2)
g.adiciona_aresta(2,0)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,3)

bfs(g)