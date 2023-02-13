class Solution:
    def __init__(self) -> None:
        self.results = []
        self.string = ''

    def backtrack(self, i, n, k, chars=['a', 'b', 'c']):
        if len(self.string) > 1 and self.string[i-1] == self.string[i-2]:
            return False
        if i == n:
            self.results.append(self.string)
            if len(self.results) == k:
                return True
            return False
        for char in chars:
            self.string += char
            if self.backtrack(i+1, n, k):
                return True
            self.string = self.string[:-1]
        return False

    def getHappyString(self, n: int, k: int) -> str:
        self.backtrack(0, n, k)
        if k > len(self.results):
            return ''
        return self.results[k-1]


if __name__ == '__main__':
    n, k = 10, 3
    print(f"{n , k}")
    print('----------Answer Below----------')
    print(Solution().getHappyString(n, k))
