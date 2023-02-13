class Solution:
    def trap(self, heights: list[int]) -> int:
        stack, rain, j = [], 0, 1000000
        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                j = stack.pop()
                if stack:
                    fill = min(heights[stack[-1]], heights[i])
                    rain += (fill-heights[j])*(i-j)
                    heights[j] = fill
                else:
                    j = 1000000
            stack.append(min(i, j))
            j = 1000000
        return rain


if __name__ == '__main__':
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"{heights}")
    print(Solution().trap(heights))
