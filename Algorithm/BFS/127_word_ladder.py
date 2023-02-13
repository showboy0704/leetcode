from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = {word for word in wordList}
        n=len(beginWord)
        visited = set()
        queue = deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(n):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt_word = word[:i]+c+word[i+1:]
                    if nxt_word in words and nxt_word not in visited:
                        visited.add(nxt_word)
                        queue.append((nxt_word, steps+1))
        return 0


if __name__ == '__main__':
    beginWord , endWord , wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
    print(f"{beginWord , endWord , wordList}")
    print('----------Answer Below----------')
    print(Solution().ladderLength(beginWord , endWord , wordList))
