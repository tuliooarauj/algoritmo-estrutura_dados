from lista_adjacencia import *

def busca_profundidade(grafo, v_inicial = 0):

    visitado = [False] * grafo.vertice
    antecessor = [-1] * grafo.vertice
    
    dfs(g, v_inicial, antecessor, visitado)

    visitado = []
    antecessor = []

def dfs(grafo, vertice, antecessor, visitado):
    visitado[vertice] = True
    print(vertice)
    lista_adj = grafo.mostra_adj(vertice)
    if lista_adj:
        for u in lista_adj:
            if not visitado[u]:
                antecessor[u] = vertice
                dfs(grafo, u, antecessor, visitado)

g =  Grafo(6)    

g.adiciona_aresta_naoDirecionado(0,2)
g.adiciona_aresta_naoDirecionado(0,3)
g.adiciona_aresta_naoDirecionado(0,4)
g.adiciona_aresta_naoDirecionado(0,5)
g.adiciona_aresta_naoDirecionado(2,3)
g.adiciona_aresta_naoDirecionado(3,4)
g.adiciona_aresta_naoDirecionado(3,5)

busca_profundidade(g)

'''6 
0 2 1
0 3 1
0 4 1
0 5 1
2 3 1
3 4 1
3 5 0'''