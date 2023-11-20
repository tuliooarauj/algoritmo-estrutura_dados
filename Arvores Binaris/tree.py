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

        

def postorder_example_tree():
    tree = BinaryTree()
    n1 = TreeNode('I')
    n2 = TreeNode('N')
    n3 = TreeNode('S')
    n4 = TreeNode('C')
    n5 = TreeNode('R')
    n6 = TreeNode('E')
    n7 = TreeNode('V')
    n8 = TreeNode('A')
    n10 = TreeNode('-')
    n9 = TreeNode('S')
    n0 = TreeNode('E')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n10
    n10.right = n8
    n8.right = n7

    tree.root = n0
    return tree

def inorder_traversal_example():
    tree = BinaryTree()
    n1 = TreeNode('a')
    n2 = TreeNode('+')
    n3 = TreeNode('*')
    n4 = TreeNode('b')
    n5 = TreeNode('-')
    n6 = TreeNode('/')
    n7 = TreeNode('c')
    n8 = TreeNode('d')
    n9 = TreeNode('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_traversal()
    print()

    '''
            '+'
        /    \
        'a'     '*'
                /   \ 
            'b'   '-'
                    /   \
                '/'  'e'
                /  \ 
            'c'  'd'
    '''

if __name__ == "__main__":

    tree = postorder_example_tree()
    print('Percurso em pós ordem:')
    tree.postorder_traversal()
    print(f'\nAltura: {tree.height()}')