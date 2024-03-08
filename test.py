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

n = 5
unionFind = Union_find(n)
 
# Perform union operations
unionFind.union(0, 1)
unionFind.union(2, 3)
unionFind.union(0, 4)
 
# Print the representative of each element after unions
for i in range(n):
    print("Element {}: Representative = {}".format(i, unionFind.find(i)))


    