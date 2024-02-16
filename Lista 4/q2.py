class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def push(self, vertice):
        node = Node(vertice)

        if self._size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
        self._size += 1

    def remove(self):
        if not self._size == 0:
            removed = self.head
            self.head = self.head.next

        self._size -=1

        return removed.data

class Grafo:
    def __init__(self, qtd_vertice) -> None:
        self.qtd_vertice = qtd_vertice
        self.grafo = [None] * self.qtd_vertice
    
    def adiciona_aresta(self, u, v, idx = 0):
        if not self.grafo[u]:
            self.grafo[u] = [None]
        
        for _ in self.grafo[u]:
            idx += 1

        if self.grafo[u][idx - 1] != None:
           
            self.grafo[u] += [None]

            for _ in range(idx):
               
                self.grafo[u][idx] = self.grafo[u][idx - 1]
                idx -= 1

            self.grafo[u][idx] = v

        else:
            self.grafo[u][idx - 1] = v
    
    def bfs(self, vertice_inicial = 0):

        visitado = [False] * self.grafo.vertice
        antecessor = [False] * self.grafo.vertice
        vertices = Queue()


        if not visitado[vertice_inicial]:
            vertices.push(vertice_inicial)
            visitado[vertice_inicial] = True

            while vertices._size > 0:
                
                vertice_visitado = vertices.remove()
                print(vertice_visitado)

                for u in self.grafo.mostra_adj(vertice_visitado):
                    if not visitado[u]:
                        visitado[u] = True
                        antecessor[u] = vertice_visitado
                        
                        vertices.push(u)

        visitado = []
        antecessor = []
    
    def mostra_grafo(self):
        i = 0
        for vertice in self.grafo:
            print('{}: '.format(i), end='')
            if vertice is not None:
                for element in vertice:
                    print(element,end=' ')
                print()
            else:
                print('Lista Vazia')
            i+=1
        
class Matriz():
    def __init__(self, qtd_linha, qtd_coluna) -> None:
        self.qtd_linha = qtd_linha
        self.qtd_coluna = qtd_coluna

        self.matriz = [[0] * qtd_coluna] * qtd_linha
        self.tam_matriz = qtd_coluna * qtd_linha

    def interpreta_labirinto(self, qtd_coluna):
        grafo = Grafo(self.tam_matriz)
        n_linha = 0
        for linha in self.matriz:
            n_coluna = 0
            for _ in linha:

                vertice_atual = (qtd_coluna * n_linha) + n_coluna

                if vertice_atual == 6:
                    pass
                
                if (n_coluna - 1) >= 0: #Conectado com a esquerda

                    conexao_0 = (self.matriz[n_linha][n_coluna - 1] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha][n_coluna - 1] == '2')
                    conexao_3 = (self.matriz[n_linha][n_coluna - 1] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_esquerda = (qtd_coluna * n_linha) + (n_coluna - 1)
                        grafo.adiciona_aresta(vertice_atual, vertice_esquerda)

                    
                if (n_coluna + 1) < self.qtd_coluna: #Conectado com a direita

                    conexao_0 = (self.matriz[n_linha][n_coluna + 1] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha][n_coluna + 1] == '2')
                    conexao_3 = (self.matriz[n_linha][n_coluna + 1] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_direita = (qtd_coluna * n_linha) + (n_coluna + 1)
                        grafo.adiciona_aresta(vertice_atual, vertice_direita)

                    
                if (n_linha - 1) >= 0: #Conectado com acima

                    conexao_0 = (self.matriz[n_linha - 1][n_coluna] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha - 1][n_coluna] == '2')
                    conexao_3 = (self.matriz[n_linha - 1][n_coluna] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_acima = (qtd_coluna * (n_linha - 1)) + n_coluna
                        grafo.adiciona_aresta(vertice_atual, vertice_acima)
                    
                    
                if (n_linha + 1) < self.qtd_linha: #Conectado com abaixo

                    conexao_0 = (self.matriz[n_linha + 1][n_coluna] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha + 1][n_coluna] == '2')
                    conexao_3 = (self.matriz[n_linha + 1][n_coluna] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_abaixo = (qtd_coluna * (n_linha + 1)) + n_coluna
                        grafo.adiciona_aresta(vertice_atual, vertice_abaixo)
                    
                n_coluna += 1
            n_linha += 1
    
        grafo.mostra_grafo()

def main():

    tam_matriz = input().split()
    qtd_linha = int(tam_matriz[0])
    qtd_coluna = int(tam_matriz[1])

    m = Matriz(qtd_linha, qtd_coluna)

    for i in range(qtd_linha):
        linha = input().split()
        m.matriz[i] = linha
    
    m.interpreta_labirinto(qtd_coluna)


    

if __name__ == '__main__':
    main()