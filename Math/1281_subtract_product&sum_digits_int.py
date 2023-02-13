class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product,_sum = 1,0
        for d in str(n):
            _sum += int(d)
            product *= int(d)
        return product-_sum


if __name__ == '__main__':
    n = 234
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().subtractProductAndSum(n))
