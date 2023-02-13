class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        n = len(arr)
        if n < 3:
            return True
        for i in range(1, n-1):
            if not arr[i-1]-arr[i] == arr[i]-arr[i+1]:
                return False
        return True


if __name__ == '__main__':
    arr = [3, 5, 1]
    print(f"{arr}")
    print(Solution().canMakeArithmeticProgression(arr))
