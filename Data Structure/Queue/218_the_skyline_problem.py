import heapq


class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        sorted_buildings = sorted(
            [(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for _, r, _ in buildings])
        result, max_heap = [[0, 0]], [(0, float('inf'))]
        for l, h, r in sorted_buildings:
            while l >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if h:
                heapq.heappush(max_heap, (h, r))
            if result[-1][1] != -max_heap[0][0]:
                result.append([l, -max_heap[0][0]])
        return result[1:]


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [
        5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(f"{buildings}")
    print('----------Answer Below----------')
    print(Solution().getSkyline(buildings))
