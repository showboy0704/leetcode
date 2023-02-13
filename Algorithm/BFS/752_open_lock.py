from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deads = {dead for dead in deadends}
        nums = [str(i) for i in range(10)]
        turned = set()
        if '0000' in deads:
            return -1
        queue = deque([('0000', 0)])
        while queue:
            num, turns = queue.popleft()
            if num == target:
                return turns
            for i in range(4):
                for digit in [int(num[i])+1, int(num[i])-1]:
                    turn = num[:i]+nums[digit % 10]+num[i+1:]
                    if turn not in deads and turn not in turned:
                        turned.add(turn)
                        queue.append((turn, turns+1))
        return -1


if __name__ == '__main__':
    deadends, target = ["0201", "0101", "0102", "1212", "2002"], "0202"
    print(f"{deadends, target}")
    print('----------Answer Below----------')
    print(Solution().openLock(deadends, target))
