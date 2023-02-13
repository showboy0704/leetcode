class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def backtrack(self, board, i, j, word):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian
        # check whether can find "word" along one direction
        result = self.backtrack(board, i+1, j, word[1:]) or self.backtrack(board, i-1, j, word[1:]) \
            or self.backtrack(board, i, j+1, word[1:]) or self.backtrack(board, i, j-1, word[1:])
        board[i][j] = tmp
        return result


if __name__ == '__main__':
    board = [["A", "B", "C"],["A", "B", "C"]]
    word = "ABA"
    print(f"{board,word}")
    print('----------Answer Below----------')
    print(Solution().exist(board, word))
