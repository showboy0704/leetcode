class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0 and divisor > 0) or (
            dividend > 0 and divisor < 0)
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0
        if abs(divisor) == 1:
            if is_negative:
                dividend = -dividend
            if dividend > 2**31-1:
                dividend = 2**31-1
            elif dividend < -2**31:
                dividend = -2**31
            return dividend
        for shift in range(31, -1, -1):
            if dividend-(divisor << shift) >= 0:
                dividend = dividend-(divisor << shift)
                quotient = quotient+(1 << shift)

        if is_negative:
            return -quotient
        else:
            return quotient


if __name__ == '__main__':
    dividend = 10
    divisor = 3
    print(f"{dividend}, {divisor}")
    print(Solution().divide(dividend, divisor))
