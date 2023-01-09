from random import randint

INF = float('inf')


# 0 indexbased implementation
class MinPriorityQueue:
    '''
    Custom Mininum Priority Queue class
    '''

    def __init__(self, queue=[]):
        self.queue = queue

        if len(queue):
            self.heapify()

    def get_parent(self, i):
        return (i - 1) // 2 if i else 0

    def heapify(self):
        i = len(self.queue) - 1
        while i > 0:
            parent_idx = self.get_parent(i)

            parent_value = self.queue[parent_idx]
            if parent_value > self.queue[i]:
                self.queue[i], self.queue[parent_idx] = parent_value, self.queue[i]

            i = parent_idx

    def get_left(self, i):
        return 2*i + 1

    def get_right(self, i):
        return 2*i + 2

    def push(self, x):
        self.queue.append(x)
        self.heapify()

    def pop(self, debug=False):
        if not len(self.queue):
            raise Exception

        ret = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop()
        self.pop_heapify()

        if debug:
            self.print_heap()

        return ret

    def pop_heapify(self):
        i = 0
        n = len(self.queue)

        while i < n:
            left_child_idx, right_child_idx = self.get_left(
                i), self.get_right(i)

            if left_child_idx >= n or right_child_idx >= n:
                break

            left_child_value, right_child_value = self.queue[left_child_idx], self.queue[right_child_idx]
            index = right_child_idx

            if left_child_value < right_child_value:
                index = left_child_idx

            if self.queue[i] > min(left_child_value, right_child_value):
                self.queue[i], self.queue[index] = self.queue[index], self.queue[i]
                i = index
            else:
                break

    def print_heap(self):
        print(*self.queue)


def prims(matrix):
    '''
    This function return the MST for a connected Graph. 
    If there is Disconnected Graph then this algorithm returns one of the spanning tree present in that graph
    '''
    n = len(matrix)
    source = randint(0, n - 1)  # selecting random vertex
    # source = 0
    priority_queue = MinPriorityQueue()
    priority_queue.push((0, source, source))
    visited = set()
    tree = list()
    ret = 0

    while priority_queue.queue:
        cost, top, parent = priority_queue.pop()

        if top in visited:
            continue

        visited.add(top)
        tree.append((top, parent, cost))
        ret += cost

        for i in range(len(matrix[top])):
            if matrix[top][i] != 0 and matrix[top][i] != INF:
                # optimisation: Skipping the vertex which is already present in the tree.
                if i not in visited:
                    priority_queue.push((matrix[top][i], i, top))

    for child, parent, cost in tree:
        print(f'{parent} -> {child} = {cost}')
    return ret


def main():
    # matrix = [
    #     [0, 10, 12, 11, 3, 5],
    #     [10, 0, 9, 12, 2, 4.],
    #     [12, 9, 0, 8, 0, 0],
    #     [11, 12, 8, 0, 7, 0],
    #     [3, 2, 0, 7, 0, 6],
    #     [5, 4, 0, 0, 6, 0]
    # ]

    matrix = [
        [0, 4, INF, INF, INF, INF, INF, 8, INF],
        [4, 0, 8, INF, INF, INF, INF, 11, INF],
        [INF, 8, 0, 7, INF, 4, INF, INF, 2],
        [INF, INF, 7, 0, 9, 14, INF, INF, INF],
        [INF, INF, INF, 9, 0, 10, INF, INF, INF],
        [INF, INF, 4, 14, 10, 0, 2, INF, INF],
        [INF, INF, INF, INF, INF, 2, 0, 1, 6],
        [9, 11, INF, INF, INF, INF, 1, 0, 7],
        [INF, INF, 2, INF, INF, INF, 6, 7, 0],
    ]

    matrix = [
        [0, 2, INF, 1, 4, INF],
        [2, 0, 3, 3, INF, 7],
        [INF, 3, 0, 5, INF, 8],
        [1, 3, 5, 0, 9, INF],
        [4, INF, INF, 9, 0, INF],
        [INF, 7, 8, INF, INF, 0],
    ]

    # Disconnected Graph
    matrix = [
        [0, 2, 4, 1, INF, INF, INF],
        [2, 0, 2, 3, INF, INF, INF],
        [4, 2, 0, 5, INF, INF, INF],
        [1, 3, 5, 0, INF, INF, INF],
        [INF, INF, INF, INF, 0, 1, 3],
        [INF, INF, INF, INF, 1, 0, 2],
        [INF, INF, INF, INF, 3, 2, 0],
    ]

    # matrix = [[0, 2, 0, 6, 0],
    # 		[2, 0, 3, 8, 5],
    # 		[0, 3, 0, 0, 7],
    # 		[6, 8, 0, 0, 9],
    # 		[0, 5, 7, 9, 0]]

    # matrix = [
    #     [0, 3, 0, 3, 0],
    #     [3, 0, 0, 0, 4],
    #     [0, 0, 0, 2, 1],
    #     [3, 3, 2, 0, 0],
    #     [0, 4, 1, 0, 0]
    # ]

    print(prims(matrix))


if __name__ == "__main__":
    main()
