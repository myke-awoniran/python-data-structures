# recursive binary tree
from trees.trees import Node, my_tree, BinarySearchTree


def __r_contains(self, current_node, value):
    if current_node is None:
        return False
    if current_node.value == value:
        return True
    if current_node.value > value:
        return self.__r_contains(current_node.left, value)
    if current_node.value < value:
        return self.__r_contains(current_node.right, value)


def __r_insert(self, current_node, value):
    if current_node is None:
        return Node(value)

    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value)

    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    return current_node


def r_contains(self, value):
    if self.root is None:
        self.root = Node(value)
    return self.__r_contains(self.root, value)


def r_insert(self, value):
    return self.__r_insert(self.root, value)

# def __delete(self, current_node,value):
#     if current_node is None:
# my_tree = BinarySearchTree()
