import random
from  binary_search_tree import BinarySearchTree

random.seed(77)

values = random.sample(range(1, 1000), 42)

bst = BinarySearchTree()

for v in values:
    bst.insert(v)

bst.inorder_traversal()

items = [188, 203, 513, 330, 677, 9000]
print()
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, ' não encontrado')
    else:
        print(r.root.data, ' encontrado')
