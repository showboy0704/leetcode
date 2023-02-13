
def heapify_up(heap: list[tuple], element: tuple[int]) -> list[tuple]:
    if not heap:
        heap.append(element)
    else:
        n = len(heap)
        heap.append(element)
        parent = (n-1)//2
        while n > 0:
            if heap[n][0] < heap[parent][0]:
                heap[n], heap[parent] = heap[parent], heap[n]
            n = parent
            parent = (n-1)//2
    return heap


def heap_pop(heap: list[int]) -> tuple:
    heap[0], heap[-1] = heap[-1], heap[0]
    top = heap.pop()
    n = 0
    left, right = 2*n+1, 2*n+2
    while left < len(heap) or right < len(heap):
        less = left
        if left < len(heap) and right < len(heap):
            if heap[right][0] < heap[left][0]:
                less = right
        if heap[n][0] > heap[less][0]:
            heap[n], heap[less] = heap[less], heap[n]
        n = less
        left, right = 2*n+1, 2*n+2

    return heap, top

class Solution:

    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for row in range(min(n, k)):
            heap = heapify_up(heap, (matrix[0][row], 0, row))
        for _ in range(k):
            heap, top = heap_pop(heap)
            result, col, row = top
            if col+1 < n:
                col += 1
                heap = heapify_up(heap, (matrix[col][row], col, row))
                
        return result


if __name__ == '__main__':
    matrix, k = [[1,3,5],[6,7,12],[11,14,14]], 6
    print(f"{ matrix , k}")
    print('----------Answer Below----------')
    print(Solution().kthSmallest(matrix, k))
