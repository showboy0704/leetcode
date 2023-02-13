class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary(lo, hi, target):
            if lo > hi:
                return False
            mid = (lo+hi)//2
            if mid*mid == target:
                return True
            elif mid*mid < target:
                return binary(mid+1, hi, target)
            else:
                return binary(lo, mid-1, target)
        a = 0
        while a*a <= c:
            if c-a*a >= 0 and binary(0, c-a*a, c-a*a):
                return True
            a+=1
        return False


if __name__ == '__main__':
    c = 1000000000
    print(f"{c}")
    print('----------Answer Below----------')
    print(Solution().judgeSquareSum(c))
