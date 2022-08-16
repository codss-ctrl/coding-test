def solution(row, col, board):
    board = [list(x) for x in board]

    matched = True
    while matched:
        matched = []
        for i in range(row - 1):
            for j in range(col - 1):
                if board[i][j + 1] == \
                        board[i + 1][j + 1] == \
                        board[i + 1][j] == \
                        board[i][j] != '#':
                    matched.append([i, j])
        for i, j in matched:
            board[i][j] = board[i + 1][j] = board[i + 1][j + 1] = board[i][j + 1] = '#'

        for _ in range(row):
            for i in range(row - 1):
                for j in range(col):
                    if board[i + 1][j] == '#':
                        board[i + 1][j], board[i][j] = board[i][j], '#'
    return sum(x.count('#') for x in board)
