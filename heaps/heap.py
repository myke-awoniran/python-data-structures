class MapHeap:
    def __init__(self):
        self.heap = []

    def __left_child(self, i: int) -> int:
        return 2 * i + 1

    def __right_child(self, i: int) -> int:
        return 2 * i + 2

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        # return True
    # def remove(self, value):


my_heap = MapHeap()

my_heap.insert(99)
my_heap.insert(79)
my_heap.insert(70)
my_heap.insert(71)
my_heap.insert(72)
my_heap.insert(73)
my_heap.insert(74)
print(my_heap.heap)
