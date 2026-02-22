class Solution:
    def solveSudoku(self, board):
        def is_valid(r, c, ch):
            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch:
                    return False
                box_r, box_c = 3 * (r // 3) + i // 3, 3 * (c // 3) + i % 3
                if board[box_r][box_c] == ch:
                    return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in '123456789':
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()


if __name__ == "__main__":
    test_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    Solution().solveSudoku(test_board)

    for row in test_board:
        print(row)