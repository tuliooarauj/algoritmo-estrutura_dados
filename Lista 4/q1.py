class Grafo:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [None] * self.vertice
    
    def adiciona_aresta_naoDirecionado(self, u, v, idx = 0):
        if not self.grafo[u]: #Primeiro inserção no vertice
            self.grafo[u] = [None]
        
        for _ in self.grafo[u]:
            idx += 1

        if self.grafo[u][idx - 1] != None:
           
            self.grafo[u] += [None]

            for _ in range(idx):
               
                self.grafo[u][idx] = self.grafo[u][idx - 1]
                idx -= 1

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

            for _ in range(idx):

                self.grafo[v][idx] = self.grafo[v][idx - 1]
                idx -= 1

            self.grafo[v][idx] = u
        
        else: #Primeiro inserção no vertice
            self.grafo[v][idx - 1] = u

    def mostra_adj(self, vertice):
        return self.grafo[vertice]
    
    def busca_profundidade(self, v_inicial = 0):

        visitado = [False] * self.vertice
        antecessor = [-1] * self.vertice
        
        self.dfs(v_inicial, antecessor, visitado)

        visitado = []
        antecessor = []

    def dfs(self, vertice, antecessor, visitado):
        visitado[vertice] = True
        print(vertice)
        lista_adj = self.mostra_adj(vertice)
        if lista_adj:
            for u in lista_adj:
                if not visitado[u]:
                    antecessor[u] = vertice
                    self.dfs(u, antecessor, visitado)

