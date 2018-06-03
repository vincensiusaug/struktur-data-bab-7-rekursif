class Queens:
    board = []
    queen = "Q"
    attack = "*"
    empty = " "
    corner = " "

    def __init__(self, size = 8):
        self.size = size
        self.make()

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

    def place(self, x, y):
        board = self.board
        board[x][y] = self.queen

        for i in range(self.size):
            if i != y:
                board[x][i] = self.attack
        for i in range(self.size):
            if i != x:
                board[i][y] = self.attack

        def lt(x, y):
            x -= 1
            y -= 1
            if x >= 0 and y >= 0 and x < self.size and y < self.size:
                board[x][y] = self.attack
                lt(x, y)
        def rt(x, y):
            x += 1
            y -= 1
            if x >= 0 and y >= 0 and x < self.size and y < self.size:
                board[x][y] = self.attack
                rt(x, y)
        def lb(x, y):
            x -= 1
            y += 1
            if x >= 0 and y >= 0 and x < self.size and y < self.size:
                board[x][y] = self.attack
                lb(x, y)
        def rb(x, y):
            x += 1
            y += 1
            if x >= 0 and y >= 0 and x < self.size and y < self.size:
                board[x][y] = self.attack
                rb(x, y)
        
        lt(x, y)
        rt(x, y)
        lb(x, y)
        rb(x, y)

    def attacked(self, y, x):
        if self.board[x][y] == self.attack:
            return True
        else:
            return False

    def safe(self, y, x):
        size = self.size
        board = self.board
        for y in range(size):
            pass


test = Queens(20)
test.place(4, 6)
test.show()

