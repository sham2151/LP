from typing import List

class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        # Base case: all queens placed
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            # Check if safe
            if (
                leftrow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                # Place queen
                board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                # Move to next column
                self.solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)

                # Backtrack
                board[row] = board[row][:col] + "." + board[row][col + 1:]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]

        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)

        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)

        return ans


# Example usage
if __name__ == "__main__":
    n = 4
    sol = Solution()
    solutions = sol.solveNQueens(n)

    print(f"Total solutions for {n}-Queens:", len(solutions))
    for s in solutions:
        for row in s:
            print(row)
        print()