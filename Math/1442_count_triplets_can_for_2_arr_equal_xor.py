class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n, count = len(arr), 0
        for i in range(n-1):
            prefix = [arr[i]]
            for k in range(i+1, n):
                prefix.append(prefix[-1] ^ arr[k])
                if prefix[-1] == 0:
                    count += k-i
        return count


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7]
    print(f"{arr}")
    print('----------Answer Below----------')
    print(Solution().countTriplets(arr))
