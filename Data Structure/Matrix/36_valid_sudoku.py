class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        col_dicts = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        for i in range(9):
            row_dict = {}
            if i % 3 == 0:
                box_dicts = [{}, {}, {}]
            for j in range(9):
                ele = board[i][j]
                if row_dict.get(ele):
                    return False
                elif ele.isdigit():
                    row_dict[ele] = True
                if col_dicts[j].get(ele):
                    return False
                elif ele.isdigit():
                    col_dicts[j][ele] = True
                if box_dicts[j//3].get(ele):
                    return False
                elif ele.isdigit():
                    box_dicts[j//3][ele] = True
        return True
if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(f"{board}")
    print('----------Answer Below----------')
    print(Solution().isValidSudoku(board))
