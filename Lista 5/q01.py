class Union_find:
    def __init__(self, n) -> None:
        self.pai = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, u):
        if not self.pai[u] == u:
            self.pai[u] = self.find(self.pai[u])
        
        return self.pai[u]

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)

        if not u == v:
            if self.rank[u] > self.rank[v]:
                self.pai[v] = u
    
            else:
                self.pai[u] = v
                if self.rank[u] == self.rank[v]:
                    self.rank[v] += 1


class Grafo():
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.grafo = [[0] * self.vertice for i in range(self.vertice)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 
        self.grafo[v-1][u-1] = 1 
    
    def mostra_adj(self, vertice):
        return self.grafo[vertice]
    

 

def main():
    nUsuarios_nConexoes = input().split()
    n_usuarios = int(nUsuarios_nConexoes[0])
    n_conexoes = int(nUsuarios_nConexoes[1])

    g = Grafo(n_usuarios)
    uf = Union_find(n_usuarios)

    for i in range(n_conexoes):
        conexao = input().split()
        usuario1 = int(conexao[0])
        usuario2 = int(conexao[1])

        g.adiciona_aresta(usuario1, usuario2)
    
    for j in range(n_usuarios):
        for k in range(n_usuarios):
            if g.mostra_adj(j)[k] == 1:
                uf.union(j, k)

    for l in range(n_usuarios):
        aparicoes = 0
        representante_l = uf.pai[l] 
        for m in uf.pai:
            if m == representante_l:
                aparicoes += 1

        if l != n_usuarios:
            print(aparicoes,end=' ')
        else:
            print(aparicoes,end='')

    print()


if __name__ == "__main__":
    main()