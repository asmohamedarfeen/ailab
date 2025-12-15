def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n):
    def solve(row, board, solutions):
        if row == n:
            solutions.clear()
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve(row + 1, board, solutions)
    solutions = []
    solve(0, [0]*n, solutions)
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for i in range(n):
            row = ['.']*n
            row[sol[i]] = 'Q'
            print(' '.join(row))
        print('\n')

if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    
    print_solutions(solutions, n)