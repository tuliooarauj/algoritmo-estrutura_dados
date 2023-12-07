ROOT = 'root'

class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

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
        
        if node.data == self.max():
            print(node.data, end='')
        else:
            print(node.data, end=',')

        if node.right:
            self.inOrder(node.right)

    def preOrder(self, node = None):
        if node is None:
            node = self.root
        #melhor procurar pro elemento do inicio 
        if node == self.root:
            print(node.data, end='')
        else:
            print(','+ str(node.data), end = '')
        
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

        if node == self.root:
            print(node.data, end='')
        else:
            print(node.data, end = ',')

    def height(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        if node is None:
            return 0
        
        return node.height
    
    def insert(self, node, value):

        if not node: 
            return TreeNode(value) 
        elif value < node.data: 
            node.left = self.insert(node.left, value) 
        else: 
            node.right = self.insert(node.right, value)

        node.height = 1 + self.biggest(self.height(node.left), self.height(node.right))

        balance_factor = self.get_balance(node)

        #Left Left Case --> Right-rotate
        if balance_factor <= -2 and value < node.left.data: 
            return self.right_rotate(node)
        
        #Right Right Case --> Left-rotate
        if balance_factor >= 2 and value > node.right.data:
            return self.left_rotate(node)
        
        #Left Right Case --> Left-rotate -> Right rotate
        if balance_factor <= -2 and value > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        #Right Left Case --> Right-rotate -> Left rotate
        if balance_factor >= 2 and value < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node 
    
    def search(self, value, node = 0): 
        if node == 0:
            node = self.root
        if node is None: 
            return node
        elif node.data == value:
            return avlTree(node)

        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)
    
    def level_search(self, value, node = 0, level = 0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        elif node.data == value:
            return level
        if value < node.data:
            return self.level_search(value, node.left, level + 1)
        return self.level_search(value, node.right, level + 1)
    
    def min(self, node = ROOT):
        if node == ROOT:
            node = self.root

        if node is None or node.left is None:
            return node.data
        
        return self.min(node.left)
    
    def biggest(self, elem1, elem2):
        if elem1 > elem2:
            return elem1
        return elem2
    
    def max(self, node = ROOT):
        if node == ROOT:
            node = self.root
        
        while node.right:
            node = node.right
        return node.data

    def remove(self, value, node = ROOT):
        
        if node == ROOT:
            node = self.root

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
                node.data = substitute 
                node.right = self.remove(substitute, node.right)
        
        node.height = 1 + self.biggest(self.height(node.left), self.height(node.right))
            
        balance_factor = self.get_balance(node)

        #Left Left Case --> Right-rotate
        if balance_factor <= -2 and self.get_balance(node.left) <= 0: 
            return self.right_rotate(node)
        
        #Right Right Case --> Left-rotate
        if balance_factor >= 2 and self.get_balance(node.right) >= 0:
            return self.left_rotate(node)
        
        #Left Right Case --> Left-rotate -> Right rotate
        if balance_factor <= -2 and self.get_balance(node.left) > 0:
            node.left = self.left_rotate(node.left) 
            return self.right_rotate(node)
        
        #Right Left Case --> Right-rotate -> Left rotate
        if balance_factor >= 2 and self.get_balance(node.right) < 0:
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
        node.right = aux2 

        node.height = 1 + self.biggest(self.height(node.left), self.height(node.right))
        aux.height = 1 + self.biggest(self.height(aux.left), self.height(aux.right))

        self.root = aux
        return self.root 

    def right_rotate(self, node):
        aux = node.left
        aux2 = aux.right

        aux.right = node
        node.left = aux2 

        node.height = 1 + self.biggest(self.height(node.left), self.height(node.right))
        aux.height = 1 + self.biggest(self.height(aux.left), self.height(aux.right))

        self.root = aux
        return self.root

def main():
    tree = avlTree()
    solicitation = None

    while solicitation != 'FIM':
        
        solicitation = input()

        if not solicitation == 'FIM':
            
            solicitation = solicitation.split()

            if solicitation[0] == 'ADICIONA':
                value = int(solicitation[1])
                already_in = tree.search(value)

                if not already_in:
                    tree.root = tree.insert(tree.root, value)

            elif solicitation[0] == 'REMOVE':
                value = int(solicitation[1])
                is_removable = tree.search(value)

                if is_removable:
                    tree.root = tree.remove(value, tree.root) 
                else:
                    print('Valor {} inexistente'.format(value))

            elif solicitation[0] == 'NIVEL':
                value = int(solicitation[1])
                result = tree.level_search(value)

                if result is None:
                    print('Valor {} inexistente'.format(value))
                else:
                    print('Nivel de {}: {}'.format(value, result))

            elif solicitation[0] == 'PRINT':
                if solicitation[1] == 'PREORDEM':
                    if not tree.root == None:
                        print('[', end='')
                        tree.preOrder(tree.root)
                        print(']')

                elif solicitation[1] == 'EMORDEM':
                    if not tree.root == None:
                        print('[', end='')
                        tree.inOrder(tree.root)
                        print(']')

                elif solicitation[1] == 'POSORDEM':
                    if not tree.root == None:
                        print('[', end='')
                        tree.postOrder(tree.root)
                        print(']')

if __name__ == '__main__':
    main()