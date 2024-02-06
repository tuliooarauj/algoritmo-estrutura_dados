class Grafo():
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[0] * self.vertice for i in range(self.vertice)] #Matriz de adjacência

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 #grafo direcionado simples

        #self.grafo[v-1][u-1] = 1 grafo nao direcionado
    
    def adiciona_aresta_peso(self, u, v, peso):
        self.grafo[u-1][v-1] = peso

    def mostra_matrizAdj(self):
        for linha in range(self.vertice):
            print(self.grafo[linha])
            
g = Grafo(4)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,2)
#g.mostra_matrizAdj()

gp = Grafo(5)
gp.adiciona_aresta_peso(2,3,10)
gp.adiciona_aresta_peso(3,2,12)
gp.mostra_matrizAdj()