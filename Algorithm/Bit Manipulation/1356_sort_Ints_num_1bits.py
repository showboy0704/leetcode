class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda a: [bin(a).count('1'), a])


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(f"{arr}")
    print('----------Answer Below----------')
    print(Solution().sortByBits(arr))
