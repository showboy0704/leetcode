class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        index = 0
        opers = []
        for i in range(1, target[-1] + 1):
            opers.append("Push")
            if i != target[index]:
                opers.append("Pop")
            else:
                index += 1
        return opers


if __name__ == '__main__':
    target, n = [1, 3], 3
    print(f"{target, n}")
    print(Solution().buildArray(target, n))
