class Solution:
    def __init__(self) -> None:
        self.table = {}
        self.tiles = ''

    def backtrack(self, tiles, result=0):
        if self.tiles:
            if self.tiles in self.table:
                return result
            else:
                self.table[self.tiles] = True
                result += 1
                if len(self.tiles) == len(tiles):
                    return result
        for i in range(len(tiles)):
            if not self.used[i]:
                self.tiles += tiles[i]
                self.used[i] = True
                result = self.backtrack(tiles, result)
                self.used[i] = False
                self.tiles = self.tiles[:-1]
        return result

    def numTilePossibilities(self, tiles: str) -> int:
        self.used = [False]*len(tiles)
        return self.backtrack(tiles)


if __name__ == '__main__':
    tiles = "AAB"
    print(f"{tiles}")
    print('----------Answer Below----------')
    print(Solution().numTilePossibilities(tiles))
