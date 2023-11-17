class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str: #Retornando o dado do nó em string
        return str(self.data)

class BinaryTree:
    def __init__(self, data) -> None:
        node = TreeNode(data)
        self.root = node

         
if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = TreeNode(18)
    tree.root.right = TreeNode(22)

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)