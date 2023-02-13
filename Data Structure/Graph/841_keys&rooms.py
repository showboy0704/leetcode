class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        locked = n-1
        visited = [True]+[False]*locked
        keys = [rooms[0]]
        while keys:
            for key in keys[0]:
                if visited[key]:
                    continue
                locked -= 1
                if locked == 0:
                    return True
                visited[key] = True
                keys.append(rooms[key])
            keys = keys[1:]

        return False


if __name__ == '__main__':
    rooms = [[1, 2], [1], [1, 3], [1]]
    print(f"{rooms}")
    print('----------Answer Below----------')
    print(Solution().canVisitAllRooms(rooms))
