class Solution:
    def backtrack(self, dim: int, s: str):
        if dim == len(s):
            self.results.append(''.join(self.result))
            return

        letters = [s[dim].upper(), s[dim].lower()] if s[dim].isalpha() else [s[dim]]
        for c in letters:
            self.result[dim] = c
            self.backtrack(dim+1, s)
            self.result[dim] = ''

    def letterCasePermutation(self, s: str) -> list[str]:
        self.result = ['']*len(s)
        self.results = []
        if s:
            self.backtrack(0, s)
        return self.results


if __name__ == '__main__':
    s = "a1b2"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().letterCasePermutation(s))
