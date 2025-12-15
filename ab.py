from random import choice
from math import inf

# Initialize board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        for cell in row:
            print(f'| {chars[cell]} |', end='')
        print('\n' + '---------------')
    print('===============')


def Clearboard(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = 0


def winningPlayer(board, player):
    conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in conditions


def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)


def printResult(board):
    if winningPlayer(board, 1):
        print("X has won!\n")
    elif winningPlayer(board, -1):
        print("O has won!\n")
    else:
        print("Draw\n")


def blanks(board):
    empty = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                empty.append([x, y])
    return empty


def boardFull(board):
    return len(blanks(board)) == 0


def setMove(board, x, y, player):
    board[x][y] = player


def playerMove(board):
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2]
    }

    while True:
        try:
            move = int(input("Enter a number between 1-9: "))
            if move < 1 or move > 9:
                print("Invalid Move!")
            elif moves[move] not in blanks(board):
                print("Cell already occupied!")
            else:
                x, y = moves[move]
                setMove(board, x, y, 1)
                Gameboard(board)
                break
        except ValueError:
            print("Enter a valid number!")


def getScore(board):
    if winningPlayer(board, 1):
        return 10
    elif winningPlayer(board, -1):
        return -10
    else:
        return 0


def abminimax(board, depth, alpha, beta, player):
    best_row = -1
    best_col = -1

    if depth == 0 or gameWon(board):
        return [best_row, best_col, getScore(board)]

    for cell in blanks(board):
        setMove(board, cell[0], cell[1], player)
        score = abminimax(board, depth - 1, alpha, beta, -player)

        if player == 1:
            if score[2] > alpha:
                alpha = score[2]
                best_row, best_col = cell
        else:
            if score[2] < beta:
                beta = score[2]
                best_row, best_col = cell

        setMove(board, cell[0], cell[1], 0)

        if alpha >= beta:
            break

    return [best_row, best_col, alpha if player == 1 else beta]


def o_comp(board):
    if len(blanks(board)) == 9:
        x, y = choice([0, 1, 2]), choice([0, 1, 2])
    else:
        x, y, _ = abminimax(board, len(blanks(board)), -inf, inf, -1)

    setMove(board, x, y, -1)
    Gameboard(board)


def x_comp(board):
    if len(blanks(board)) == 9:
        x, y = choice([0, 1, 2]), choice([0, 1, 2])
    else:
        x, y, _ = abminimax(board, len(blanks(board)), -inf, inf, 1)

    setMove(board, x, y, 1)
    Gameboard(board)


def makeMove(board, player):
    if player == 1:
        playerMove(board)
    else:
        o_comp(board)


def pvc():
    while True:
        try:
            order = int(input("Play first or second? (1/2): "))
            if order in [1, 2]:
                break
            else:
                print("Choose 1 or 2")
        except ValueError:
            print("Enter a number")

    Clearboard(board)
    currentPlayer = 1 if order == 1 else -1

    Gameboard(board)

    while not (boardFull(board) or gameWon(board)):
        makeMove(board, currentPlayer)
        currentPlayer *= -1

    printResult(board)


# Driver Code
print("=================================================")
print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
print("=================================================")
pvc()
