class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(start, end):
            mid = (start+end)//2
            if start > end:
                return mid
            if mid*mid == x:
                return mid
            elif mid*mid < x:
                return binary(mid+1, end)
            else:
                return binary(start, mid-1)
        return binary(0, x)


if __name__ == '__main__':
    x = 8
    print(f"{x}")
    print('----------Answer Below----------')
    print(Solution().mySqrt(x))
