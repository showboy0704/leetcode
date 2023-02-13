class Solution:
    def dfs(self, i, j, board):
        if not(0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != 'O':
            return
        board[i][j] = 'T'
        neib_list = [[i+1, j], [i-1, j], [i, j-1], [i, j+1]]
        for x, y in neib_list:
            self.dfs(x, y, board)

    def solve(self, board):
        for i in range(len(board)):
            self.dfs(i, 0, board)
            self.dfs(i, len(board[0])-1, board)

        for j in range(len(board[0])):
            self.dfs(0, j, board)
            self.dfs(len(board)-1, j, board)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 'X' if board[i][j] != 'T' else 'O'


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
             ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(f"{board}")
    print('----------Answer Below----------')
    print(Solution().solve(board))
