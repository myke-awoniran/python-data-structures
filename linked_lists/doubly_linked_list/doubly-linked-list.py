class Node:
    def __init__(self, value: None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return temp
        else:

            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = self.head
        else:
            self.head.next = None
            self.head = temp.next
            self.head.prev = None
        self.length -= 1
        return temp

    def get(self, index):
        if index >= self.length or index < 0:
            print('Index out of range')
            return None
        if self.length == 0:
            return None
        if index == 0:
            return self.head.value
        if index == self.length - 1:
            return self.tail.value
        temp= self.head
        for i in range(index):
            temp = temp.next
            if temp is None:
                return None
        return temp.value

    def set_value(self, index, value):
        if index >= self.length or index < 0:
            print('Index out of range')
            return False
        if index == 0:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            return True
        # if index == self.length - 1:
        #     temp = self.tail
        #     self.tail = Node(value)
        #     temp.next = self.tail
        #     self.tail.prev = temp
        #     # self.length += 1
        #     return True
        # else:
        temp = self.head
        for _ in range(index):
            temp= self.head
            if temp is None:
                return False

        temp.value = value
        self.length += 1
        return True







