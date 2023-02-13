class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break

        return True


if __name__ == '__main__':
    words, order = ["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
    print(f"{words , order}")
    print('----------Answer Below----------')
    print(Solution().isAlienSorted(words, order))
