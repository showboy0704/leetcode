from collections import Counter


class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        order_set = Counter()
        for k, val in items1+items2:
            order_set[k] += val
        return sorted(order_set.items())


if __name__ == '__main__':
    items1, items2 = [[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]
    print(f"{items1 , items2}")
    print('----------Answer Below----------')
    print(Solution().mergeSimilarItems(items1, items2))
