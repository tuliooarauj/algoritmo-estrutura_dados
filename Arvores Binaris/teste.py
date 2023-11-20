import random
from  binary_search_tree import BinarySearchTree

values = random.sample(range(1, 1000), 42)

bst = BinarySearchTree()

for v in values:
    bst.insert(v)

bst.inorder_traversal()