def bin_search(array: list[int], target: int) -> bool:
    left, right = 0, len(array)-1
    mid = (left+right)//2
    while left <= right:
        if array[mid] < target:
            left = mid+1
            mid = (left+right)//2
        elif array[mid] > target:
            right = mid-1
            mid = (left+right)//2
        else:
            return True
    return False


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target>matrix[-1][-1] or target<matrix[0][0]:
            return False
        for row in matrix:
            if bin_search(row,target):
                return True
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
        3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 27
    print(f"{matrix,target }")
    print('----------Answer Below----------')
    print(Solution().searchMatrix(matrix, target))
