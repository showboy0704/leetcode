class Solution:
    def climbStairs(self, n: int) -> int:
        steps = []
        for stair in range(n):
            if stair+1 == 1:
                steps.append(1)
            elif stair+1 == 2:
                steps.append(2)
            else:
                steps.append(steps[stair-1]+steps[stair-2])
        return steps[n-1]


if __name__ == '__main__':
    n = 4
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().climbStairs(n))
