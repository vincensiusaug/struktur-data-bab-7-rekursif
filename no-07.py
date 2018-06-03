class Queens:
    board = []
    queen = "Q"
    empty = " "
    corner = "*"

    def __init__(self, size = 8):
        self.size = size
        self.make()

    def settings(self):
        self.queen = input("Masukan character untuk simbol queen = ")
        self.empty = input("Masukan character untuk simbol empty = ")

    def make(self):
        self.board = [[self.empty for y in range(self.size)] for x in range(self.size)]

    def show(self):
        print ("{0:^4}".format(self.corner), end = "")
        for i in range(self.size):
            print ("{0:^3}".format(i), end = "")
        print ("{0:^4}".format(self.corner))

        for y in range(self.size):
            print ("{0:>4}".format(y), end = "")
            for x in range(self.size):
                print ("{0:^3}".format(self.board[x][y]), end = "")

            print ("{0:<4}".format(y))

        print ("{0:^4}".format(self.corner), end = "")
        for i in range(self.size):
            print ("{0:^3}".format(i), end = "")
        print ("{0:^4}".format(self.corner))
    
    def attacked(self, x, y):
        board = self.board
        for i in range(self.size):
            if board [x][i] == self.queen:
                return True
        
        for i in range(self.size):
            if board [i][y] == self.queen:
                return True
        
        
        i = x - 1
        j = y - 1
        k = 0
        while k <= min(i, j):
            if board[i][j] == self.queen:
                return True
            else:
                i -= 1
                j -= 1
                k += 1
        
        i = x + 1
        j = y - 1
        k = 0
        while k <= min(self.size - i - 1, j):
            if board[i][j] == self.queen:
                return True
            else:
                i += 1
                j -= 1
                k += 1
        
        i = x - 1
        j = y + 1
        k = 0
        while k <= min(i, self.size - j - 1):
            if board[i][j] == self.queen:
                return True
            else:
                i -= 1
                j += 1
                k += 1

        i = x + 1
        j = y + 1
        k = 0
        while k <= min(self.size - i - 1, self.size - j - 1):
            if board[i][j] == self.queen:
                return True
            else:
                i += 1
                j += 1
                k += 1

        return False

    def safe(self, x = 0):
        board = self.board
        if x < self.size:
            for y in range(self.size):
                if not self.attacked(x, y):
                    if x == self.size - 1:
                        board[x][y] = self.queen
                        return True
                    else:
                        board[x][y] = self.queen
                    if self.safe(x+1):
                        return True
                    else:
                        board[x][y] = self.empty
            return False
        return False



test = Queens()
test.safe()
test.show()

