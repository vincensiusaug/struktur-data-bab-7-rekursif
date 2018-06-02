class Hanoi:
    def __init__(self, n):
        self.number = n
        self.arrA = list(range(n,0,-1))
        self.arrB = []
        self.arrC = []
        self.out()

    def out(self):
        for i in range (self.number-1,-1,-1):
            try:
                print ("{0:^3}|".format(self.arrA[i]),end="")
            except IndexError:
                print ("{0:^3}|".format("-"),end="")

            try:
                print ("{0:^3}|".format(self.arrB[i]),end="")
            except IndexError:
                print ("{0:^3}|".format("-"),end="")

            try:
                print ("{0:^3}".format(self.arrC[i]))
            except IndexError:
                print ("{0:^3}".format("-"))

        print ("{0:=<11}".format(""))

    def moveNumber(self, beg, end):
        number = beg.pop()
        end.append(number)
        if beg == self.arrA:
            a = 1
        print ()
        print ("{0:} - {1:} -> {2:}".format(number, beg, end))
        self.out()

    def move(self, n = None, beg = None, mid = None, end = None):
        move = self.move

        if n == None:
            n = self.number
        if beg == None:
            beg = self.arrA
        if mid == None:
            mid = self.arrB
        if end == None:
            end = self.arrC

        if n==1:
            self.moveNumber(beg, end)
        else:
            move(n-1, beg, end, mid)
            move(1, beg, mid, end)
            move(n-1, mid, beg, end)

tower = Hanoi(3)
tower.move()
