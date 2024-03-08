class Union_find:
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
    nUsuarios_nConexoes = input().split()
    n_usuarios = int(nUsuarios_nConexoes[0])
    n_conexoes = int(nUsuarios_nConexoes[1])

    uf = Union_find(n_usuarios)

    for i in range(n_conexoes):
        conexao = input().split()
        usuario1 = int(conexao[0])
        usuario2 = int(conexao[1])

        uf.union(usuario1-1, usuario2-1)

    for l in range(n_usuarios):
        representante_l = uf.find(l)
        tamanho_l = uf.size[representante_l]
        if l == n_usuarios - 1:
            print(tamanho_l, end="")
        else:
            print(tamanho_l, end=" ")

    print()

if __name__ == "__main__":
    main()