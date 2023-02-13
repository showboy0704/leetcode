class Solution:
    def myAtoi(self, s: str) -> int:
        step, sign, result, digits = 1, 1, 0, []
        for char in s:
            if step == 1:
                if char == ' ':
                    pass
                elif char == '-':
                    step = 3
                    sign = -1
                elif char == '+':
                    step = 3
                elif char.isdigit():
                    step = 3
                    digits.append(char)
                else:
                    break
            elif step == 3:
                if char.isdigit():
                    digits.append(char)
                else:
                    break
        if digits:
            result = sign * int(''.join(digits))
        if result > (2**31)-1:
            result = (2**31)-1
        elif result < -2**31:
            result = -2**31
        return result


if __name__ == '__main__':
    s = "4193 with words"
    print(f"{s}")
    print('-------------------------------------------------')
    print(Solution().myAtoi(s))
