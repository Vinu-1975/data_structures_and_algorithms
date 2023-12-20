def isSafe(board, row, col, n):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, n):
    # Base case: If all queens are placed
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if isSafe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solveNQUtil(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column col, return False
    return False


def solveNQ(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solveNQUtil(board, 0, n):
        print("Solution does not exist")
        return False

    # Solution found; print the board
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    return True


# Example usage
n = 4  # Change this value to N for an N-queens problem
solveNQ(n)


"""


Keyword arguments:
argument -- description
Return: return_description

isSafe: This function checks if a queen can be placed on board[row][col]. It checks for conflicts with other queens in the left row, upper left diagonal, and lower left diagonal.
solveNQUtil: A recursive utility function to solve the N-Queens problem. It places queens one by one in different columns.
solveNQ: This function sets up the board and calls solveNQUtil. It prints the solution if one exists.
"""
