class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits)-1
        while i >= 0:
            digits[i] = (digits[i]+1) % 10
            if digits[i] == 0:
                i -= 1
            else:
                break
        if i == -1:
            digits = [1]+digits
        return digits


if __name__ == '__main__':
    digits = [1, 0, 9, 9, 9]
    print(f"{digits}")
    print('----------Answer Below----------')
    print(Solution().plusOne(digits))
