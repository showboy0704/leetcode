class Trie:

    def __init__(self):
        self.words, self.prefix = set(), set()

    def insert(self, word: str) -> None:
        self.words.add(word)
        for i in range(len(word)+1):
            self.prefix.add(word[:i])

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix
