class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        visited = set()
        _max = x
        for ban in forbidden:
            _max = max(_max, ban)
            visited.add((ban, 1))
            visited.add((ban, 0))
        _max += a+b
        queue = [(0, 0, False)]
        while queue:
            bug, steps, state = queue[0]
            queue = queue[1:]
            if bug == x:
                return steps
            if bug > _max or bug < 0 or (bug, state) in visited:
                continue
            queue.append((bug+a, steps+1, False))
            if not state:
                queue.append((bug-b, steps+1, True))
            visited.add((bug, state))
        return -1


if __name__ == '__main__':
    forbidden, a, b, x = [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
                          154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98], 29, 98, 80
    print(f"{forbidden , a, b , x}")
    print('----------Answer Below----------')
    print(Solution().minimumJumps(forbidden, a, b, x))
