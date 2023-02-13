class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if int(bin(num)[-1]) == 0:
                num = num >> 1
            else:
                num -= 1
            steps += 1
        return steps


if __name__ == '__main__':
    num = 14
    print(f"{num}")
    print('----------Answer Below----------')
    print(Solution().numberOfSteps(num))
