class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):  # initiate the linkedlist with a value on instantiation
        self.head = Node(value)
        self.tail = None

    def find_middle_node(self):
        # two pointer problem
        # one moves faster (2X) than the other i.e fast and slow pointer(1x)
        # when the fast pointer reaches the end of the list, the slow pointer is already at the middle of the list
        # why? let's see this examle, 1234567, fast pointer moves at 2, 4,6 (3 times), slow pointer moves at 1,2,3( 3 times)
        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        return slow_ptr

    def has_loop(self):
        fast_ptr = self.head
        slow_ptr = self.head

        while slow_ptr and fast_ptr and fast_ptr.next:
            if fast_ptr == slow_ptr:
                return True
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return False
