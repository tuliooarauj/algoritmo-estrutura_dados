class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack():
    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def push(self, element):
        
        node = Node(element)

        node.next = self.top #Atribuir a variável node.next ao antigo topo
        self.top = node #Atribuir ao novo topo a nova variável que está chegando
        self._size += 1

    def pop(self):
        if self._size == 0:
            return 'Stack is empty'
        else:
            node = self.top.data
            self.top = self.top.next #O topo agora é a próxima variável
            self._size -= 1
            return node.data
    
    def peek(self):
        #retorna o valor do topo
        if self._size == 0:
            return 'Stack is empty'
        else:
            top = self.top.data
            return top.data
        
    def next_peek(self):
        #retorna o após ao topo
        next_peek = self.top.next.data
        return next_peek.data
        

stack = Stack()

while True:
    opcao = input('\n\nDigite a opção do menu:\n1- Inserir\n2- Remover\n3- Mostrar último valor da pilha\n\n')
    if opcao == '1':
        dado = input('Digite o dado: ')
        solicitacao = Node(dado)
        stack.push(solicitacao)
    
    elif opcao == '2':
        print(stack.pop())

    elif opcao == '4':
        print(stack.next_peek())

    else:
        print(stack.peek())
