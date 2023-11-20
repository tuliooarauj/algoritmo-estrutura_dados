from fila import Fila

ROOT = 'root'

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str: #Retornando o dado do nó em string
        return str(self.data)

class BinaryTree:
    def __init__(self, data = None, tree_node = None):
        if tree_node: #Permitir a possibilidade de criação de uma árvore ou sub-árvore dado que já existe um nó.
            self.root = None
        elif data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None

    def inorder_traversal(self, node = None): #Encaminhamento em ordem
        if node is None:
            node = self.root #Partindo por padrão a partir da raiz
        if node.left:
            #print('(', end='')
            self.inorder_traversal(node.left)
        print(node, end = ' ')
        if node.right:
            self.inorder_traversal(node.right)
            #print(')', end='')

    def postorder_traversal(self, node = None):
        if node is None:
            node = self.root #Partindo por padrão a partir da raiz
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end=' ')

    def height(self, node = None):
        if node is None:
            node = self.root #Partindo por padrão a partir da raiz
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1 
        return hleft + 1
    
    def levelorder_traversal(self, node = ROOT):
        if node == ROOT:
            node = self.root

        queue = Fila()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=' ')
    
class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        parent = None
        x = self.root

        while x:
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right

        if parent is None:
            self.root = TreeNode(value)
        elif value < parent.data:
            parent.left = TreeNode(value)
        else:
            parent.right = TreeNode(value)
    
    def search(self, value, node = 0):
        if node == 0:
            node = self.root
        elif node is None:
            return node
        elif node.data == value:
            return BinarySearchTree(node)
        
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
         
if __name__ == "__main__":
    pass