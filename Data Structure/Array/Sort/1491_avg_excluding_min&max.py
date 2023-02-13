class Solution:
    def average(self, salarys: list[int]) -> float:
        n = len(salarys)
        total, _min, _max = 0, 1000000, 1000
        for salary in salarys:
            total += salary
            _min = min(_min, salary)
            _max = max(_max, salary)
        return (total-_min-_max)/(n-2)


if __name__ == '__main__':
    salary = [4000, 3000, 1000, 2000]
    print(f"{salary}")
    print('----------Answer Below----------')
    print(Solution().average(salary))
