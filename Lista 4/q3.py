class Grafo:
    def __init__(self, qtd_vertice) -> None:
        self.qtd_vertice = qtd_vertice
        self.grafo = [[0] * self.qtd_vertice for i in range(self.qtd_vertice)]
    
    def adiciona_aresta_peso(self, u, v, peso):
        self.grafo[u][v] = peso

    def dijkstra_linear(self, inicio):
        n = len(self.grafo)
        distance = [float('inf')]*n
        distance[inicio] = 0
        visited = [False]*n
        antecessor = [-1]*n

        v = inicio
        for _ in range(n):
            visited[v] = True

            for j in range(n):
                if self.grafo[v][j] != 0 and distance[j] > distance[v]+self.grafo[v][j]:
                    distance[j] = distance[v]+self.grafo[v][j]
                    antecessor[j] = v

            menor = float('inf')
            for j in range(n):
                if not visited[j] and distance[j] < menor:
                    v = j
                    menor = distance[j]

        return distance


def main():
    qrn = input().split()

    n_quadras = int(qrn[0])
    n_ruas = int(qrn[1])
    n_eventos = int(qrn[2])

    grafo = Grafo(n_quadras)

    for i in range(n_ruas):

        abm = input().split()
        
        ponto_a = int(abm[0])
        ponto_b = int(abm[1])
        min_percurso = int(abm[2])

        grafo.adiciona_aresta_peso(ponto_a, ponto_b, min_percurso)

    for j in range(n_eventos):

        evento = input().split()

        ponto_a = int(evento[1])
        ponto_b = int(evento[2])

        if evento[0] == '1':
            min_percurso = int(evento[3])
            grafo.adiciona_aresta_peso(ponto_a, ponto_b, min_percurso)
            
        elif evento[0] == '2':
            distancias = grafo.dijkstra_linear(ponto_a)
            if distancias[ponto_b] != float('inf'):
                print(distancias[ponto_b])
            else:
                print(-1)


if __name__ == '__main__':
    main()