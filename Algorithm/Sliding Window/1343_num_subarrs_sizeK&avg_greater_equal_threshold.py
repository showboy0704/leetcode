class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count, total = 0, sum(arr[:k-1])
        for l in range(len(arr)-k+1):
            r = l+k
            total += arr[r-1]
            count += 1 if total >= threshold*k else 0
            total -= arr[l]
        return count


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(f"{arr,k,threshold}")
    print('----------Answer Below----------')
    print(Solution().numOfSubarrays(arr, k, threshold))
