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

    def mostra(self):
        print(self.pai)
        print(self.rank)



uf = Union_find(5)

uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

uf.mostra()