class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        self.first = Node(value)
        self.last = self.first
        self.length = 1

    def enqueue(self, value):
        # adding an element to the last of a list
        # is O(1) while removing add to the last is O(n)
        # let's look at adding from the first of the list
        # This takes adding O(1) adding to first of a queue
        # removing from the first of a queue takes 0(1) as well
        # hence  we will take the constant times of two scenarios
        # that is enqueue will happen at the end of the list
        # dequeue will happen at the start of a list
        new_node = Node(value)
        if self.length==0:
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True



    def dequeue(self):
        if self.length==0:
            return None
        # remove from the first of the list
        # set the next element of the list to next Node
        # set the next of the removed first to NONE
        temp= self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp.value



