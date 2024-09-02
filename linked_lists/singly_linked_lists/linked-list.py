class Node:
    def __init__(self, value, next: None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        new_node = Node(value, None)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #
    def append(self, value):
        new_node = Node(value, None)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def pop(self):
        # remove the last item of the list
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    # if the list is empty, return
    # if the list has only one Node, return the Node
    # if the list has more than one node

    def prepend(self, value):
        new_node = Node(value, None)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            current_head = self.head
            self.head = new_node
            self.head.next = current_head
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def insert(self, value, index):
        new_node = Node(value, None)
        if self.length == 0 or index == 0:
            return self.prepend(value)
        temp = self.get(index - 1)
        temp.next = new_node
        new_node.next = temp.next
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        # if length is not zero, what do we do
        # set the head to the currenthead.next
        # remove the head
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def get(self, index):
        # if value is not found in the list, return False
        # else return True
        if index < 0 or index > self.length:
            print('Index out of range')
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            if temp is None:
                return None
        return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

    def remove_value(self, value, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        pre = self.get(index - 1)
        if temp:
            pre.next = temp.next
            temp.next = None
            return temp.value

    #
    def find_middle_node(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp.next = after
        return


my_list = LinkedList(1)
my_list.append(2)
# my_list = LinkedList(1)
my_list.append(2)
# my_list = LinkedList(1)
my_list.append(2)
my_list.prepend(4)
# mid_value = my_list.find_middle_node()
# print(mid_value.value)
print(my_list.print_list())

my_list.reverse_list()
# my_list.pop_first()
# my_list.pop_first()
# my_list.pop_first()
#
# my_list.pop()
# my_list.pop()
# my_list.pop()
# print(my_list.print_list())
