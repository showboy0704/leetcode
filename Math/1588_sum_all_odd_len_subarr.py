class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            left, right = i, n - i - 1
            total += arr[i] * (left // 2 + 1) * (right // 2 + 1)
            total += arr[i] * ((left + 1) // 2) * ((right + 1) // 2)
        return total


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(f"{arr}")
    print('----------Answer Below----------')
    print(Solution().sumOddLengthSubarrays(arr))
