class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1

    def print_stack(self):
        top = self.top

        while top:
            print(top.value)
            top = top.next
        return

    def push(self, value):
        # create the node
        # add the top of the stack
        # change the head of the stack
        if self.height == 0:
            self.top = Node(value)
            self.height = 1
        else:
            new_top = Node(value)
            new_top.next = self.top
            self.top = new_top
        my_stack.height += 1
        return self.top.value

    def pop(self):
        # check if height of the stack is zero
        # remove the top element,
        # set the next element as the top
        # point the next of the 'next' element as NONE  to detach the pop top
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        my_stack.height -= 1
        return temp


my_stack = Stack(5)
my_stack.push(3)
my_stack.pop()
print(my_stack.print_stack())
