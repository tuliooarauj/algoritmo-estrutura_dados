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
         
if __name__ == "__main__":
    '''tree = BinaryTree(7)
    tree.root.left = TreeNode(18)
    tree.root.right = TreeNode(22)

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)'''

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