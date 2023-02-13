class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited = [False]*len(arr)
        stack = [start]
        while stack:
            i = stack.pop()
            if 0 <= i < len(arr) and not visited[i]:
                if arr[i] == 0:
                    return True
                visited[i] = True
                stack.extend([i+arr[i], i-arr[i]])
        return False


if __name__ == '__main__':
    arr, start = [4, 2, 3, 0, 3, 1, 2], 5
    print(f"{arr , start}")
    print('----------Answer Below----------')
    print(Solution().canReach(arr, start))
