ROOT = 'root'

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class avlTree():
    def __init__(self, data = None, tree_node = None):
        if tree_node:
            self.root = tree_node
        elif data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None
    
    def inOrder(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        if node.left:
            self.inOrder(node.left)
        
        print(node, end = ' ')

        if node.right:
            self.inOrder(node.right)

    def preOrder(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        print(node, end = ' ')

        if node.left:
            self.inOrder(node.left)

        if node.right:
            self.inOrder(node.right)
    
    def postOrder(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        if node.left:
            self.inOrder(node.left)
        
        if node.right:
            self.inOrder(node.right)

        print(node, end = ' ')

    def height(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        if node.left:
            hleft = self.postOrder(node.left)

        if node.right:
            hright = self.postOrder(node.right)

        if hright > hleft:
            return hright + 1
        return hleft + 1
    
    def insert(self, value):
        parent = None
        aux = self.root

        while aux:
            parent = aux # variavel parent sempre vai estar um elemento atrás da auxiliar
            
            if value < aux.data: #Processo de caminhada até chegar numa folha
                aux = aux.left
            else:
                aux = aux.right

        if parent is None: #Primeira inserção (Não entrou no while)
            self.root = TreeNode(value)
        elif value < parent.data: #Chegou até a folha e tá verificando onde inserir
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)

        balance_factor = self.get_balance(parent)

        #Left Left Case --> Right-rotate
        if balance_factor <= -2 and value < parent.left.data: 
            pass 

    def search(self, value, node = 0): # Busca por um valor começando pela raiz ou nó desejado
        if node == 0:
            node = self.root
        elif node is None: #Valor não encontrado
            return node
        elif node.data == value:
            return avlTree(node)

        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
    
    def min(self, node = ROOT):
        if node == ROOT:
            node = self.root

        while node.left:
            node = node.left
        return node.data
    
    def max(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node = ROOT):
        if node == ROOT:
            node = self.root

        #Busca do elemento por recursão, retornando sempre a sub-árvore a esquerda ou direita do nó inicial até encontrar o elemento a ser removido.
        #Substituir por None é o mesmo que remover

        if node is None:
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left)
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                substitute = self.min(node.right)
                node.data = substitute #Simples troca de valores e remoção da posição do antigo nó
                node.right = self.remove(substitute, node.right)
    
    def get_balance(self, node = None):
        if node is None:
            return 0
        
        fb = self.height(node.right) - self.height(node.left)

        return fb
    
    def left_rotate(self, node):
        aux = node.right
        aux2 = aux.left 

        aux.left = node
        node.right = aux2 #Nó que "desceu" recebe à direita a árvore à esquerda do nó que "subiu"

        return aux #Nó que "subiu" é retornado como nova raiz

    def right_rotate(self, node):
        aux = node.left
        aux2 = aux.right

        aux.right = node
        node.left = aux2 # Nó que "desceu" recebe à esquerda a árvore à direita do nó que "subiu"

        return aux #Nó que "subiu" é retornado como nova raiz
