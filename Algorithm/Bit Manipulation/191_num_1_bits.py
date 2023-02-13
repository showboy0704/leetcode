class Solution:
    def hammingWeight(self, n):
        count = 0
        for bit in bin(n)[2:]:
            if bit == '1':
                count += 1

        return count


if __name__ == '__main__':
    n = 11
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().hammingWeight(n))
