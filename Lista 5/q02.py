class Heap():
    def __init__(self, array) -> None:
        self.array = array
        self.size = len(array)
        self.build_min_heap()

    def parent(self, idx):
        return idx // 2

    def left(self, idx):
        return (idx * 2) + 1

    def right(self, idx):
        return (idx * 2) + 2 

    def switch(self, array, elem1, elem2):
        aux = array[elem1]
        array[elem1] = array[elem2]
        array[elem2] = aux

    def min_heapify(self, array, idx):
        if not idx < 0:
            left_idx = self.left(idx)
            right_idx = self.right(idx)

            if left_idx <= self.size - 1 and array[left_idx][2] < array[idx][2]:
                menor = left_idx
            else:
                menor = idx
            
            if right_idx <= self.size - 1 and array[right_idx][2] < array[menor][2]:
                menor = right_idx
            
            if menor != idx:
                self.switch(array, idx, menor)
                self.min_heapify(array, menor)

    def build_min_heap(self):
        for idx in range((self.size // 2), -1, -1):
            self.min_heapify(self.array, idx - 1)


class Grafo():
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[0] * self.vertice for i in range(self.vertice)]

    def adiciona_aresta_peso(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def kruskal_mst(self):
        arestas = [None]

        for i in range(self.vertice):
            for j in range(i + 1, self.vertice):
                if self.grafo[i][j] != 0:

                    arestas[-1] = [i, j, self.grafo[i][j]]
                    arestas+=[None]

        heap = Heap(arestas[:-1])
        union_find = Union_find(self.vertice)
        peso_mst = 0
        idx = 0

        while idx < self.vertice - 1:
            u, v, peso = heap.array[0]
            heap.switch(heap.array, 0, heap.size - 1)
            heap.size -= 1
            heap.min_heapify(heap.array, 0)


            if union_find.find(u) != union_find.find(v):
                idx += 1
                peso_mst += peso
                union_find.union(u, v)

        return peso_mst


class Union_find():
    def __init__(self, n) -> None:
        self.pai = [i for i in range(n)]    
        self.size = [1] * n

    def find(self, u):
        if not self.pai[u] == u:
            self.pai[u] = self.find(self.pai[u])
        
        return self.pai[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return
        
        if self.size[u] < self.size[v]:
            self.pai[u] = v
            self.size[v] += self.size[u]
        else:
            self.pai[v] = u
            self.size[u] += self.size[v]


def main():
    nAeroportos_nTrechos = input().split()
    n_aeroportos = int(nAeroportos_nTrechos[0])
    n_trechos = int(nAeroportos_nTrechos[1])

    grafo = Grafo(n_aeroportos)

    for i in range(n_trechos):
        trecho = input().split()
        id_aeroportoA = int(trecho[0])
        id_aeroportoB = int(trecho[1])
        custo_AB = int(trecho[2])
        if ((grafo.grafo[id_aeroportoA][id_aeroportoB] == 0 and grafo.grafo[id_aeroportoB][id_aeroportoA] == 0) or
             (grafo.grafo[id_aeroportoA][id_aeroportoB] > custo_AB or grafo.grafo[id_aeroportoB][id_aeroportoA] > custo_AB)) and id_aeroportoA != id_aeroportoB:       
            grafo.adiciona_aresta_peso(id_aeroportoA, id_aeroportoB, custo_AB)
    
    mst = grafo.kruskal_mst()
    print(mst)
        
if __name__ == "__main__":
    main()