class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set([])
        num = 0
        for i in range(len(isConnected)):
            if i not in visited:
                to_visit = [i]
                while to_visit:
                    city = to_visit.pop()
                    if city not in visited:
                        visited.add(city)
                        to_visit += [city for city, path in enumerate(
                            isConnected[city]) if path and city not in visited]
                num += 1
        return num


if __name__ == '__main__':
    isConnected = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
    print(f"{isConnected}")
    print('----------Answer Below----------')
    print(Solution().findCircleNum(isConnected))
