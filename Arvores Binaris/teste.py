import random
from  binary_search_tree import BinarySearchTree

random.seed(77)

def random_tree(size = 42):

    values = random.sample(range(1, 1000), size)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def example_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

def extended_tree():
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree

bst = extended_tree()
bst.inorder_traversal()

#Teste de remoção
print('\n------')
v = 61
bst.remove(v)
print(bst.height())

print(f'Após remover {v}')
bst.inorder_traversal()
print('\n')
bst.levelorder_traversal()
print(bst.height())

print('\n------')
print('Máximo: ', bst.max())
print('Mínimo: ', bst.min())

'''for item in items:
    r = bst.search(item)
    if r is None:
        print(item, ' não encontrado')
    else:
        print(r.root.data, ' encontrado')'''
