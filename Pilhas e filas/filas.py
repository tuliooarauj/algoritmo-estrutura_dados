class SolicitacaoImpressao:
    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa
        self.prox = None

class FilaImpressao:
    def __init__(self) -> None:
        self.inicio = None

    def adicionar_solicitacao(self, solicitacao):
        if self.inicio == None:
            self.inicio = solicitacao
            self.fim = solicitacao
        else:
            self.fim.prox = solicitacao
            self.fim = solicitacao

    def atender_solicitacao(self):
        if self.inicio == None:
            print('Não há cliente esperando\n')
        else:
            print('Atenda', self.inicio.nome_pessoa)
            self.inicio = self.inicio.prox

    def imprime_status(self):
        x = self.inicio

        if x is None:
            print('Fila vazia.\n')

        while x != None:
            print(x.nome_pessoa)
            x = x.prox

fila = FilaImpressao()

while True:
    opcao = input('\n\nDigite a opção do menu:\n1- Inserir\n2- Atender\n3- Mostrar status da fila\n\n')
    if opcao == '1':
        nome = input('Digite o nome do cliente: ')
        solicitacao = SolicitacaoImpressao(nome)
        fila.adicionar_solicitacao(solicitacao)
    
    elif opcao == '2':
        fila.atender_solicitacao()

    else:
        fila.imprime_status()