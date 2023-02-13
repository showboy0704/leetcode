class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        visited = set()
        stack = [(0, 0)]
        (jug1, jug2) = (jug2, jug1) if jug1 > jug2 else (jug1, jug2)
        while stack:
            cap1, cap2 = stack.pop()
            if cap1+cap2 == target:
                return True
            if (cap1, cap2) not in visited:
                visited.add((cap1, cap2))
                stack.extend([(cap1, jug2), (jug1, cap2), (jug1, jug2)])
                stack.extend([(cap1, 0), (0, cap2)])
                if cap1 <= jug2-cap2:
                    stack.append((0, cap1+cap2))
                else:
                    stack.append((cap1-(jug2-cap2), jug2))
                if cap2 <= jug1-cap1:
                    stack.append((cap1+cap2, 0))
                else:
                    stack.append((jug1, cap2-(jug1-cap1)))

        return False


if __name__ == '__main__':
    jug1, jug2, target = 8, 5, 4
    print(f"{jug1 , jug2, target}")
    print('----------Answer Below----------')
    print(Solution().canMeasureWater(jug1, jug2, target))
