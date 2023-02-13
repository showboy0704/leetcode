class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = len(num)
        for i in range(len(num)):
            k += num[i]*10**(n-1-i)
        num = []
        while k > 0:
            num.append(k % 10)
            k //= 10

        return num[::-1]


if __name__ == '__main__':
    num, k = [1, 2, 0, 0], 34
    print(f"{num, k}")
    print('----------Answer Below----------')
    print(Solution().addToArrayForm(num, k))
