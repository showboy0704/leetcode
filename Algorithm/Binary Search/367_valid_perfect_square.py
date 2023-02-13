class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binary(lo, hi, num):
            if lo > hi:
                return False
            mid = (lo+hi)//2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                return binary(mid+1, hi, num)
            else:
                return binary(lo, mid-1, num)
        return binary(0, num, num)


if __name__ == '__main__':
    num = 1
    print(f"{num}")
    print('----------Answer Below----------')
    print(Solution().isPerfectSquare(num))
