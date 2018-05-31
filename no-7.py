def make(size):
    board = [[0 for y in range(size)] for x in range(size)]
    for x in range(size):
        for y in range(size):
            board[x][y] = "-"
    return board

def safe(board, x, y):
    if board[x][y] not in ("*","Q"):
        return True
    False

def diagonal1(board, x, y, size):
    if x >= 0 and y >= 0 and x < size and y < size:
        if board[x][y] != "Q":
            board[x][y] = "*"
        board = diagonal1(board, x+1, y+1, size)
    return board

def diagonal2(board, x, y, size):
    if x >= 0 and y >= 0 and x < size and y < size:
        if board[x][y] != "Q":
            board[x][y] = "*"
        board = diagonal2(board, x-1, y+1, size)
    return board

def diagonal3(board, x, y, size):
    if x >= 0 and y >= 0 and x < size and y < size:
        if board[x][y] != "Q":
            board[x][y] = "*"
        board = diagonal3(board, x+1, y-1, size)
    return board

def diagonal4(board, x, y, size):
    if x >= 0 and y >= 0 and x < size and y < size:
        if board[x][y] != "Q":
            board[x][y] = "*"
        board = diagonal4(board, x-1, y-1, size)
    return board

def place(board, xx, yy, size):
    board[xx][yy] = "Q"
    for x in range(size):
        if board[x][yy] == "Q":
            continue
        else:
            board[x][yy] = "*"
    for y in range(size):
        if board[xx][y] == "Q":
            continue
        else:
            board[xx][y] = "*"

    board = diagonal1(board, xx, yy, size)
    board = diagonal2(board, xx, yy, size)
    board = diagonal3(board, xx, yy, size)
    board = diagonal4(board, xx, yy, size)
    return board

    


def show(board, size):
    for y in range(size):
        for x in range(size):
            print (board[x][y],end=" ")
        print ()

def queen(size):
    board = make(size)
    for y in range(size):
        for x in range(size):
            if safe(board, x, y):
                board = place(board, x, y, size)
    show(board, size)

queen(8)
