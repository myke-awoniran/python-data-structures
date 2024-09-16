class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if temp.value < value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # if root is none return False
        # temp= self.root
        # while temp is None:
        # update temp on each loop

        temp = self.root
        while temp:
            if temp.value < value:
                temp = temp.left
            elif temp.value > value:
                temp = temp.right
            else:
                return True
        return False




my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.contains(7))
print(my_tree.root.right.value)
