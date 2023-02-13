class Solution:
    def reverse(self, x: int) -> int:
        temp_x = abs(x)
        reverse_x = int(str(temp_x)[::-1])
        if x < 0:
            reverse_x = -reverse_x
        if reverse_x > (2**31)-1 or reverse_x < -2**31:
            reverse_x = 0
        return reverse_x


if __name__ == '__main__':
    x = 120
    print(f"{x}")
    print('-------------------------------------------------')
    print(Solution().reverse(x))
