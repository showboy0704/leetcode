class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            n = sum([int(d)*int(d) for d in str(n)])
        return True


if __name__ == '__main__':
    n = 2
    print(f"{n }")
    print('----------Answer Below----------')
    print(Solution().isHappy(n))
