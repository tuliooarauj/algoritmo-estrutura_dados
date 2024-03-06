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

        return removed.data


class Grafo():
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[0] * self.vertice for i in range(self.vertice)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 
        self.grafo[v-1][u-1] = 1 

    def mostra_matrizAdj(self):
        for linha in range(self.vertice):
            print(self.grafo[linha])
    
    def mostra_adj(self, vertice):
        return self.grafo[vertice]

    def bfs(grafo, vertice_inicial = 0):

        visitado = [False] * grafo.vertice
        antecessor = [False] * grafo.vertice
        vertices = Queue()

        if not visitado[vertice_inicial]:
            vertices.push(vertice_inicial)
            visitado[vertice_inicial] = True
            n_visitados = 0

            while vertices._size > 0:
                
                vertice_visitado = vertices.remove()
                n_visitados += 1

                adj = grafo.mostra_adj(vertice_visitado)
                for u in range(len(adj)):
                    if adj[u] == 1 and not visitado[u]:
                        visitado[u] = True
                        antecessor[u] = vertice_visitado
                        
                        vertices.push(u)
        
        print(n_visitados,end=' ')

    

def main():
    nUsuarios_nConexoes = input().split()
    n_usuarios = int(nUsuarios_nConexoes[0])
    n_conexoes = int(nUsuarios_nConexoes[1])

    g = Grafo(n_usuarios)

    for i in range(n_conexoes):
        conexao = input().split()
        usuario1 = int(conexao[0])
        usuario2 = int(conexao[1])

        g.adiciona_aresta(usuario1, usuario2)
    
    for j in range(n_usuarios):
        g.bfs(j)


if __name__ == "__main__":
    main()