class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i-j
            stack.append(i)
        return answer


if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    print(f"{temperatures}")
    print('----------Answer Below----------')
    print(Solution().dailyTemperatures(temperatures))
