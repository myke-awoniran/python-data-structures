class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if temp.value < value:
                if temp.left is None:
                    temp.left = new_node
                    return True




my_tree= BinarySearchTree()
print(my_tree.root)

