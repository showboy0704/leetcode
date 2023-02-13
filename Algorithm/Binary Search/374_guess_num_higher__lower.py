'''
@param num, your guess
@return -1 if num is higher than the picked number
        1 if num is lower than the picked number
        otherwise return 0
'''
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left+right)//2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid-1
            else:
                left = mid+1


if __name__ == '__main__':
    n, pick = 10, 6
    print(f"{n, pick}")
    print('----------Answer Below----------')
    print(Solution().guessNumber(n))