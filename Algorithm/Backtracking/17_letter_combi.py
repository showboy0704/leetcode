class Solution:
    phone = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: [
        'm', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    def backtrack(self, dim: int):
        if dim == len(self.digits):
            self.results.append(''.join(self.result))
            return

        for char in self.phone[int(self.digits[dim])]:
            self.result[dim] = char
            self.backtrack(dim+1)

    def letterCombinations(self, digits: str) -> list[str]:
        self.results = []
        if digits:
            self.digits = digits
            self.result = [None] * len(digits)
            self.backtrack(0)
        return self.results


if __name__ == '__main__':
    digits = "22"
    print(f"{digits}")
    print('----------Answer Below----------')
    print(Solution().letterCombinations(digits))
