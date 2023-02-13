class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary(lo, hi, mat, target):
            if lo > hi:
                return False
            mid = (lo+hi)//2
            r, c = mid//len(matrix[0]), mid % len(matrix[0])
            if mat[r][c] == target:
                return True
            elif mat[r][c] < target:
                return binary(mid+1, hi, mat, target)
            else:
                return binary(lo, mid-1, mat, target)
        return binary(0, len(matrix)*len(matrix[0])-1, matrix, target)


if __name__ == '__main__':
    matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
    print(f"{matrix, target}")
    print('----------Answer Below----------')
    print(Solution().searchMatrix(matrix, target))
