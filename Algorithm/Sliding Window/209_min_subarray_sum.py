class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        left, right = 0, 0
        total = nums[left]
        lens=[]
        while left < len(nums)-1:
            if total >= target:
                if current_len == 1:
                    return 1
                lens.append(current_len)
                total -= nums[left]
                left += 1
                current_len -= 1
            else:
                if right < len(nums)-1:
                    right += 1
                    current_len += 1
                    total += nums[right]
                else:
                    lens.append(right-left + 1 + 1)
                    break
        return min(lens)


if __name__ == '__main__':
    target = 7
    nums = [1,1,1,1,7]
    print(f"{target,nums}")
    print(Solution().minSubArrayLen(target, nums))
