class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n = high-low+1
        if n % 2 and high % 2:
            if high % 2:
                return n//2+1
            else:
                return n//2
        else:
            return n//2


if __name__ == '__main__':
    low, high = 3, 7
    print(f"{low , high}")
    print('----------Answer Below----------')
    print(Solution().countOdds(low, high))
