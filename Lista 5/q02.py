class Grafo():
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[0] * self.vertice for i in range(self.vertice)]

    def adiciona_aresta_peso(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def min_chave(self, chave, visitado):
        minimo = float('inf')
        for v in range(self.vertice):
            if chave[v] < minimo and not visitado[v]:
                minimo = chave[v]
                minimo_indice = v
        return minimo_indice
    
    def mostra_mst(self, pai):
        custo_total = 0
        for i in range(1, self.vertice):
            custo_total += self.grafo[i][pai[i]] 
        print(custo_total)


    def prim(self):
        pai = [None] * self.vertice
        chave = [float('inf')] * self.vertice
        chave[0] = 0
        visitado = [False] * self.vertice

        pai[0] = -1

        for i in range(self.vertice):
            u = self.min_chave(chave, visitado)
            visitado[u] = True

            for v in range(self.vertice):
                if self.grafo[u][v] > 0 and not visitado[v] and self.grafo[u][v] < chave[v]:
                    pai[v] = u
                    chave[v] = self.grafo[u][v]
        
        self.mostra_mst(pai)

def main():
    nAeroportos_nTrechos = input().split()
    n_aeroportos = int(nAeroportos_nTrechos[0])
    n_trechos = int(nAeroportos_nTrechos[1])

    grafo = Grafo(n_aeroportos)

    for i in range (n_trechos):
        trecho = input().split()
        id_aeroportoA = int(trecho[0])
        id_aeroportoB = int(trecho[1])
        custo_AB = int(trecho[2])
        if ((grafo.grafo[id_aeroportoA][id_aeroportoB] == 0 and grafo.grafo[id_aeroportoB][id_aeroportoA] == 0) or
             (grafo.grafo[id_aeroportoA][id_aeroportoB] > custo_AB or grafo.grafo[id_aeroportoB][id_aeroportoA] > custo_AB)) and id_aeroportoA != id_aeroportoB:       
            
                grafo.adiciona_aresta_peso(id_aeroportoA, id_aeroportoB, custo_AB)
    
    
    grafo.prim()
        
if __name__ == "__main__":
    main()