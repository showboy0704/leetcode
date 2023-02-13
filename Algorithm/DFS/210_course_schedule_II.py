class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if not prerequisites:
            return [course for course in range(numCourses)]
        self.order=[]
        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0 for _ in range(numCourses)]
        for pair in prerequisites:
            x, y = pair
            self.graph[y].append(x)

        def dfs(pre: int):
            if self.visited[pre] == -1:
                return False
            if self.visited[pre] == 1:
                return True
            self.visited[pre] = -1
            for post in self.graph[pre]:
                if not dfs(post):
                    return False
            self.order.append(pre)
            self.visited[pre] = 1
            return True
        for pre in range(numCourses):
            if not dfs(pre):
                return []
        self.order.reverse()
        return self.order


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(f"{numCourses,prerequisites}")
    print(Solution().findOrder(numCourses, prerequisites))
