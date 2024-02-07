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

g =  Grafo(4)    

g.adiciona_aresta(0,1)
g.adiciona_aresta(0,2)
g.adiciona_aresta(1,2)
g.adiciona_aresta(2,0)
g.adiciona_aresta(2,3)
g.adiciona_aresta(3,3)

busca_profundidade(g, 2)