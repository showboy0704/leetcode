def next_state(live: int, neighbors: int) -> int:
    if live:
        if 2 > neighbors or neighbors > 3:
            return 0
        elif 1 < neighbors < 4:
            return 1

    else:
        if neighbors == 3:
            return 1
        else:
            return 0


class Solution:
    def neighbors(self, i, j) -> int:
        result = 0
        for v in [-1, 0, 1]:
            for h in [-1, 0, 1]:
                m, n = i+v, j+h
                if (-1 < m < len(self.board)) and (-1 < n < len(self.board[0])) and (m, n) != (i, j):
                    result += self.board[m][n]
        return result

    def gameOfLife(self, board: list[list[int]]) -> None:
        self.board = board
        state_q = []
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                state = self.board[i][j]
                neighbors = self.neighbors(i, j)
                state_q.append([i, j, next_state(state, neighbors)])
                if state_q:
                    m, n, s = state_q[0]
                    if abs(i-m) > 1 and abs(j-n) > 1:
                        board[m][n] = s
                        state_q = state_q[1:]
        for state in state_q:
            m, n, s = state
            board[m][n] = s


if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
    print(f"{board}")
    print('----------Answer Below----------')
    print(Solution().gameOfLife(board))
