class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, pair):
        self.heap.append(pair)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index][0] < self.heap[smallest][0]
        ):
            smallest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index][0] < self.heap[smallest][0]
        ):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


def shortest_path(graph, start, end):

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = MinHeap()
    priority_queue.push((0, start))

    while not priority_queue.is_empty():
        current_distance, current_vertex = priority_queue.pop()

        if current_vertex == end:
            return distances[end]

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.push((distance, neighbor))

    return -1


N, M = map(int, input().split())
graph = {i: {} for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

shortest_path_length = shortest_path(graph, 1, N)
print(shortest_path_length)
