def drawBoard(board):
    print("\n")
    for i in range(3):
        print(" {} | {} | {} ".format(board[i][0], board[i][1], board[i][2]))
        if i < 2:
            print("---|---|---")
    print("\n")

def checkWin(board, markWinningLine):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            if markWinningLine:
                board[i] = ['*']*3
            return 1 if board[i][0] == 'X' else -1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            if markWinningLine:
                for j in range(3):
                    board[j][i] = '*'
            return 1 if board[0][i] == 'X' else -1

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        if markWinningLine:
            board[0][0] = board[1][1] = board[2][2] = '*'
        return 1 if board[1][1] == 'X' else -1

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        if markWinningLine:
            board[0][2] = board[1][1] = board[2][0] = '*'
        return 1 if board[1][1] == 'X' else -1

    return 0

def playerMove(board):
    while True:
        x, y = map(int, input("Enter your move (row and column, separated by space): ").split())
        if 1 <= x <= 3 and 1 <= y <= 3 and board[x - 1][y - 1] == ' ':
            board[x - 1][y - 1] = 'X'
            break
        else:
            print("Invalid move. Try again.")
    drawBoard(board)

def aiMove(board):
    bestScore = -1000
    bestMove = [-1, -1]

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                moveScore = minimax(board, 0, False)
                board[i][j] = ' '
                if moveScore > bestScore:
                    bestScore = moveScore
                    bestMove = [i, j]

    board[bestMove[0]][bestMove[1]] = 'O'
    print("AI made a move:")
    drawBoard(board)

def minimax(board, depth, isMaximizingPlayer):
    result = checkWin(board, False)

    if result != 0:
        return result * (10 - depth)
    if depth == 9:
        return 0

    if isMaximizingPlayer:
        bestScore = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    bestScore = min(score, bestScore)
        return bestScore

def main():
    board = [[' ']*3 for _ in range(3)]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    drawBoard(board)

    while checkWin(board, False) == 0 and turn < 9:
        playerMove(board)
        turn += 1
        if checkWin(board, False) != 0 or turn == 9:
            break
        aiMove(board)
        turn += 1

    result = checkWin(board, True)
    drawBoard(board)
    if result == 1:
        print("Congratulations, you won!")
    elif result == -1:
        print("AI won, better luck next time!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
