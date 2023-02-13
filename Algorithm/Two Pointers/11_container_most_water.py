class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        i, j = 0, len(height)-1
        while i != j:
            if height[i] > height[j]:
                area = height[j]*(j-i)
                j -= 1
            elif height[i] < height[j]:
                area = height[i]*(j-i)
                i += 1
            else:
                area = height[i]*(j-i)
                i += 1

            if area > max_area:
                max_area = area
        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"{height}")
    print('-------------------------------------------------')
    print(Solution().maxArea(height))
