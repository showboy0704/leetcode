def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary(lo, hi):
            if lo > hi:
                return lo
            mid = (lo+hi)//2
            if not isBadVersion(mid):
                return binary(mid+1, hi)
            else:
                return binary(lo, mid-1)
        return binary(1, n)


if __name__ == '__main__':
    n, bad = 5, 4
    print(f"{n, bad}")
    print('----------Answer Below----------')
    print(Solution().search(n, bad))
