class Solution:
    def get_squares(self, n: int) -> list[int]:
        squares = list(self.squares.keys())
        for i in range(len(squares)):
            if (n-squares[i]) < 0:
                return squares[:i]

    def numSquares(self, n: int) -> int:
        self.squares = dict()
        for i in range(1, 101):
            self.squares[i*i] = 1

        height, cur_lvl_lim, next_lvl_lim = 1, 1, 0

        if n in self.squares:
            return height
        queue = [n]
        while queue:
            n = queue[0]
            queue = queue[1:]
            cur_lvl_lim -= 1
            next_squares = self.get_squares(n)
            next_lvl_lim += len(next_squares)
            for squ in next_squares:
                if (n-squ) in self.squares:
                    return height+1
                else:
                    queue.append((n-squ))
            if cur_lvl_lim == 0:
                cur_lvl_lim = next_lvl_lim
                next_lvl_lim = 0
                height += 1


if __name__ == '__main__':
    n = 1
    print(f"{n}")
    print('----------Answer Below----------')
    print(Solution().numSquares(n))
