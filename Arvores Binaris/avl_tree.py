ROOT = 'root'

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str: #Retornando o dado do nó em string
        return str(self.data)
    
class avlTree():
    def __init__(self, data = None, tree_node = None):
        if tree_node:
            self.root = tree_node
        elif data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None
    
    def inOrder(self, node = None):
        if node is None:
            node = self.root
        
        if node.left:
            self.inOrder(node.left)
        
        print(node, end = ' ')

        if node.right:
            self.inOrder(node.right)

    def preOrder(self, node = None):
        if node is None:
            node = self.root
        
        print(node, end = ' ')

        if node.left:
            self.preOrder(node.left)

        if node.right:
            self.preOrder(node.right)
    
    def postOrder(self, node = None):
        if node is None:
            node = self.root
        
        if node.left:
            self.postOrder(node.left)
        
        if node.right:
            self.postOrder(node.right)

        print(node, end = ' ')

    def height(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return 0

        hleft = 0
        hright = 0
        
        if node.left:
            hleft = self.height(node.left)

        if node.right:
            hright = self.height(node.right)

        if hright > hleft:
            return hright + 1
        return hleft + 1
    
    def insert(self, root, value):
        
        if not root: 
            return TreeNode(value) 
        elif value < root.data: 
            root.left = self.insert(root.left, value) 
        else: 
            root.right = self.insert(root.right, value) 

        balance_factor = self.get_balance(root)

        #Left Left Case --> Right-rotate
        if balance_factor <= -2 and value < root.left.data: 
            return self.right_rotate(root)
        
        #Right Right Case --> Left-rotate
        if balance_factor >= 2 and value > root.right.data:
            return self.left_rotate(root)
        
        #Left Right Case --> Left-rotate -> Right rotate
        if balance_factor <= -2 and value > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        #Right Left Case --> Right-rotate -> Left rotate
        if balance_factor >= 2 and value < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    
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
            
        balance_factor = self.get_balance(node)

        #Left Left Case --> Right-rotate
        if balance_factor <= -2 and self.get_balance(node.left) >= 0: 
            return self.right_rotate(node)
        
        #Right Right Case --> Left-rotate
        if balance_factor >= 2 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        
        #Left Right Case --> Left-rotate -> Right rotate
        if balance_factor <= -2 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left) 
            return self.right_rotate(node)
        
        #Right Left Case --> Right-rotate -> Left rotate
        if balance_factor >= 2 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node
    
    def get_balance(self, node = None):
        if node is None:
            return 0
        
        hleft = self.height(node.left)
        hright = self.height(node.right)
        fb = hright - hleft

        return fb
    
    def left_rotate(self, node):
        aux = node.right
        aux2 = aux.left 

        aux.left = node
        node.right = aux2 #Nó que "desceu" recebe à direita a árvore à esquerda do nó que "subiu"

        self.root = aux
        return self.root #Nó que "subiu" é retornado como nova raiz

    def right_rotate(self, node):
        aux = node.left
        aux2 = aux.right

        aux.right = node
        node.left = aux2 # Nó que "desceu" recebe à esquerda a árvore à direita do nó que "subiu"

        self.root = aux
        return self.root #Nó que "subiu" é retornado como nova raiz


myTree = avlTree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
 
for num in nums:
    root = myTree.insert(root, num)
 
# Preorder Traversal
print("Preorder Traversal after insertion -")
myTree.preOrder(root)
print()

# Delete 
key = 89
root = myTree.remove(key, root)
 
# Preorder Traversal
print(f"Preorder Traversal after deletion of {key}-")
myTree.preOrder(root)
print()
