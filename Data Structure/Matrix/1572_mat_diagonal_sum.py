class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total = 0
        primary, second = 0, len(mat)-1
        for arr in mat:
            total += arr[primary]
            if primary != second:
                total += arr[second]
            primary += 1
            second -= 1
        return total


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"{mat}")
    print('----------Answer Below----------')
    print(Solution().diagonalSum(mat))
