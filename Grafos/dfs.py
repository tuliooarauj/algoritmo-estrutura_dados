from lista_adjacencia import *

def busca_profundidade(grafo):

    visitado = [False] * grafo.vertice
    antecessor = [-1] * grafo.vertice

    for j in range(grafo.vertice):
        if not visitado[j]:
            dfs(g, j, antecessor, visitado)

    for i in range(grafo.vertice):
        print(antecessor[i])
    
    visitado = []
    antecessor = []

def dfs(grafo, vertice, antecessor, visitado):
    visitado[vertice] = True
    
    for u in grafo.mostra_adj(vertice):
        if not visitado[u]:
            antecessor[u] = vertice
            dfs(grafo, u, antecessor, visitado)

g =  Grafo(3)    

g.adiciona_aresta(1,2)
g.adiciona_aresta(1,3)
g.adiciona_aresta(2,1)
g.adiciona_aresta(2,3)

g.mostra_adj(1)

g.mostra_grafo()