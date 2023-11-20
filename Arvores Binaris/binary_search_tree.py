class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str: #Retornando o dado do nó em string
        return str(self.data)

class BinaryTree:
    def __init__(self, data = None):
        if data:
            node = TreeNode(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self, node = None): #Encaminhamento em ordem
        if node is None:
            node = self.root #Partindo por padrão a partir da raiz
        if node.left:
            print('(', end='')
            self.simetric_traversal(node.left)
        print(node, end = '')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')

    def postorder_traversal(self, node = None):
        if node is None:
            node = self.root #Partindo por padrão a partir da raiz
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node, end='')

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
         
if __name__ == "__main__":
    pass