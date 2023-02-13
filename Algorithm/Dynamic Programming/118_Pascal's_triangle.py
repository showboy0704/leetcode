class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[] for _ in range(numRows)]
        for n in range(numRows):
            result[n].append(1)
            if n == 1:
                result[n].append(1)
            elif n > 1:
                for i in range(n-1):
                    result[n].append(result[n-1][i]+result[n-1][i+1])
                result[n].append(1)

        return result


if __name__ == '__main__':
    numRows = 5
    print(f"{numRows}")
    print('----------Answer Below----------')
    print(Solution().generate(numRows))
