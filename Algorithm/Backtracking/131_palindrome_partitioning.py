def is_palin(s):
    if s:
        return s == s[::-1]


class Solution:
    def backtrack(self, dim: int):
        if dim == len(self.chars):
            self.results.append(self.result[:])
            return

        for length in range(1,len(self.chars)+1):
            sub_str = self.chars[dim:dim+length]
            if is_palin(sub_str):
                self.result.append(sub_str)
                self.backtrack(dim+length)
                self.result.pop()

    def partition(self, s: str) -> list[list[str]]:
        if len(s) == 1:
            return [[s]]
        self.chars, self.result, self.results = s, [], []
        self.backtrack(0)
        return self.results


if __name__ == '__main__':
    s = "cabac"
    print(f"{s}")
    print('----------Answer Below----------')
    print(Solution().partition(s))
