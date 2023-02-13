class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        subords = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] > -1:
                subords[manager[i]].append(i)
        times = set()
        queue = [(headID, 0)]
        while queue:
            _id, _time = queue[0]
            times.add(_time)
            for subord in subords[_id]:
                queue.append((subord, _time+informTime[_id]))
            queue = queue[1:]

        return max(times)


if __name__ == '__main__':
    n, headID, manager, informTime = 6, 2, [
        2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]
    print(f"{n , headID , manager , informTime}")
    print('----------Answer Below----------')
    print(Solution().numOfMinutes(n, headID, manager, informTime))
