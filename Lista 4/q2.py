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
    
    def bfs(self, vertice_inicial):

        visitado = [False] * self.qtd_vertice
        antecessor = [-1] * self.qtd_vertice
        vertices = Queue()
        
        
        if not visitado[vertice_inicial]:
            vertices.push(vertice_inicial)
            visitado[vertice_inicial] = True

            while vertices._size > 0:
                
                vertice_visitado = vertices.remove()
                

                for u in self.mostra_adj(vertice_visitado):
                    if not visitado[u]:
                        visitado[u] = True
                        antecessor[u] = vertice_visitado
                        
                        vertices.push(u)

        return antecessor
    
    def mostra_adj(self, vertice):
        return self.grafo[vertice]
    
    def caminho(self, origem, destino, antecessor, qtd_passos = 0):
        if origem == destino:
            print(qtd_passos)

        elif antecessor[destino] == -1:
            print('Labirinto Impossivel')

        else:
            self.caminho(origem, antecessor[destino], antecessor, qtd_passos + 1)
        
        
class Matriz():
    def __init__(self, qtd_linha, qtd_coluna) -> None:
        self.qtd_linha = qtd_linha
        self.qtd_coluna = qtd_coluna
        self.origem = None
        self.destino = None
        self.matriz = [[0] * qtd_coluna] * qtd_linha
        self.tam_matriz = qtd_coluna * qtd_linha

    def interpreta_labirinto(self, qtd_coluna):
        grafo = Grafo(self.tam_matriz)
        n_linha = 0
        for linha in self.matriz:
            n_coluna = 0
            for element in linha:

                vertice_atual = (qtd_coluna * n_linha) + n_coluna

                if element == '2':
                    self.origem = vertice_atual
                elif element == '3':
                    self.destino = vertice_atual
                
                if (n_coluna - 1) >= 0: 

                    conexao_0 = (self.matriz[n_linha][n_coluna - 1] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha][n_coluna - 1] == '2')
                    conexao_3 = (self.matriz[n_linha][n_coluna - 1] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_esquerda = (qtd_coluna * n_linha) + (n_coluna - 1)
                        grafo.adiciona_aresta(vertice_atual, vertice_esquerda)

                    
                if (n_coluna + 1) < self.qtd_coluna: 

                    conexao_0 = (self.matriz[n_linha][n_coluna + 1] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha][n_coluna + 1] == '2')
                    conexao_3 = (self.matriz[n_linha][n_coluna + 1] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_direita = (qtd_coluna * n_linha) + (n_coluna + 1)
                        grafo.adiciona_aresta(vertice_atual, vertice_direita)

                    
                if (n_linha - 1) >= 0: 

                    conexao_0 = (self.matriz[n_linha - 1][n_coluna] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha - 1][n_coluna] == '2')
                    conexao_3 = (self.matriz[n_linha - 1][n_coluna] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_acima = (qtd_coluna * (n_linha - 1)) + n_coluna
                        grafo.adiciona_aresta(vertice_atual, vertice_acima)
                    
                    
                if (n_linha + 1) < self.qtd_linha:

                    conexao_0 = (self.matriz[n_linha + 1][n_coluna] == '0')
                    bloqueado = (self.matriz[n_linha][n_coluna] == '1')
                    conexao_2 = (self.matriz[n_linha + 1][n_coluna] == '2')
                    conexao_3 = (self.matriz[n_linha + 1][n_coluna] == '3')

                    if not bloqueado and (conexao_0 or conexao_2 or conexao_3):
                        vertice_abaixo = (qtd_coluna * (n_linha + 1)) + n_coluna
                        grafo.adiciona_aresta(vertice_atual, vertice_abaixo)
                    
                n_coluna += 1
            n_linha += 1

        return grafo

def main():

    tam_matriz = input().split()
    qtd_linha = int(tam_matriz[0])
    qtd_coluna = int(tam_matriz[1])

    m = Matriz(qtd_linha, qtd_coluna)

    for i in range(qtd_linha):
        linha = input().split()
        m.matriz[i] = linha
    
    grafo = m.interpreta_labirinto(qtd_coluna)

    v_antecessor = grafo.bfs(m.origem)

    grafo.caminho(m.origem, m.destino, v_antecessor)


if __name__ == '__main__':
    main()