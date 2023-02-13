class Solution:
    def __init__(self) -> None:
        self.table = {}
        self.num = ''

    def backtrack(self, n, pattern):
        if n > 0:
            if pattern[n-1] == 'I' and self.num[n-1] > self.num[n]:
                return False
            elif pattern[n-1] == 'D' and self.num[n-1] < self.num[n]:
                return False
            else:
                if n == len(pattern):
                    return True
        for i in range(len(pattern)+1):
            if not self.used[i]:
                self.num += str(i+1)
                self.used[i] = True
                if self.backtrack(n+1, pattern):
                    return True
                self.used[i] = False
                self.num = self.num[:-1]
        return False

    def smallestNumber(self, pattern: str) -> str:
        self.used = [False]*(len(pattern)+1)
        self.backtrack(-1, pattern)
        return self.num


if __name__ == '__main__':
    pattern = "IDIDID"
    print(f"{pattern}")
    print('----------Answer Below----------')
    print(Solution().smallestNumber(pattern))
