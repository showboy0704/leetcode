class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # bucket sort
        table = dict()
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        sort_buckets = sorted(table.items(), key=lambda item: item[1])
        return [b[0] for b in sort_buckets[::-1][:k]]


if __name__ == '__main__':
    nums, k = [1,1,1,2,2,3], 2
    print(f"{nums, k }")
    print('----------Answer Below----------')
    print(Solution().topKFrequent(nums, k))
