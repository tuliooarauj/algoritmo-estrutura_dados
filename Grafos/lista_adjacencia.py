class Grafo:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [None] * self.vertice

    def adiciona_aresta(self, u, v, idx = 0):
        if not self.grafo[u]:
            self.grafo[u] = [None]

        if self.grafo[u][idx] != None:
           
           self.grafo[u] += [None]
           idx += 1
           self.grafo[u][idx] = v

        else:
            self.grafo[u][idx] = v

    def adiciona_aresta_naoDirecionado(self, u, v, idx = 0):
        if not self.grafo[u]: #Primeiro inserção no vertice
            self.grafo[u] = [None]
        
        for element in self.grafo[u]:
            idx += 1

        if self.grafo[u][idx - 1] != None:
           
           self.grafo[u] += [None]
           self.grafo[u][idx] = v

        else: #Primeiro inserção no vertice
            self.grafo[u][idx - 1] = v



        if not self.grafo[v]: #Primeiro inserção no vertice
            self.grafo[v] = [None]

        idx = 0
        for element in self.grafo[v]:
            idx += 1

        if self.grafo[v][idx - 1] != None:
           
           self.grafo[v] += [None]
           self.grafo[v][idx] = u
        
        else: #Primeiro inserção no vertice
            self.grafo[v][idx - 1] = u



    def mostra_grafo(self):
        i = 0
        for vertice in self.grafo:
            print(i,': ', vertice)
            i+=1

    def mostra_adj(self, vertice):
        return self.grafo[vertice]
    
'''
g = Grafo(3)

g.adiciona_aresta(0,1)
g.adiciona_aresta(0,2)
g.adiciona_aresta(1,2)


print(g.mostra_adj(0))

g.mostra_grafo()'''