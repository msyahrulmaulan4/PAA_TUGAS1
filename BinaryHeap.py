class Delivery:
    def __init__(self, delivery_number, priority):
        self.delivery_number = delivery_number
        self.priority = priority

class BinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, delivery):
        self.heap.append(delivery)
        self.size += 1
        self._sift_up(self.size - 1)

    def extract_min(self):
        if self.size == 0:
            return None
        min_delivery = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self._sift_down(0)
        return min_delivery

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index].priority < self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if left_child_index < self.size and self.heap[left_child_index].priority < self.heap[smallest].priority:
            smallest = left_child_index
        if right_child_index < self.size and self.heap[right_child_index].priority < self.heap[smallest].priority:
            smallest = right_child_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)

# Contoh penggunaan Binary Heap untuk sistem pengelolaan rute pengiriman barang
delivery_heap = BinaryHeap()

delivery1 = Delivery("ABC123", 3)
delivery2 = Delivery("DEF456", 1)
delivery3 = Delivery("GHI789", 2)

delivery_heap.insert(delivery1)
delivery_heap.insert(delivery2)
delivery_heap.insert(delivery3)

# Mengeluarkan pengiriman dengan prioritas terendah
min_delivery = delivery_heap.extract_min()
print("Delivery number:", min_delivery.delivery_number)  # Output: DEF456

min_delivery = delivery_heap.extract_min()
print("Delivery number:", min_delivery.delivery_number)  # Output: GHI789