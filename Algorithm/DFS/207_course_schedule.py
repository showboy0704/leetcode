class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites:
            return True

        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0 for _ in range(numCourses)]
        for pair in prerequisites:
            x, y = pair
            self.graph[x].append(y)

        def dfs(pre: int):
            if self.visited[pre] == -1:
                return False
            if self.visited[pre] == 1:
                return True
            self.visited[pre] = -1
            for post in self.graph[pre]:
                if not dfs(post):
                    return False
            self.visited[pre] = 1
            return True
        for pre in range(numCourses):
            if not dfs(pre):
                return False
        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(f"{numCourses,prerequisites}")
    print(Solution().canFinish(numCourses, prerequisites))
