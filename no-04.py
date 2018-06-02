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
                print ("{0:^3}|".format(" "),end="")

            try:
                print ("{0:^3}|".format(self.arrB[i]),end="")
            except IndexError:
                print ("{0:^3}|".format(" "),end="")

            try:
                print ("{0:^3}".format(self.arrC[i]))
            except IndexError:
                print ("{0:^3}".format(" "))

        print ("{0:=<11}".format(""))
        print ("{0:^3}|{1:^3}|{2:^3}".format("A", "B", "C"))

    def moveNumber(self, beg, end):
        number = beg.pop()
        end.append(number)
        if beg == self.arrA:
            a = "A"
        elif beg == self.arrB:
            a = "B"
        elif beg == self.arrC:
            a = "C"
        if end == self.arrA:
            b = "A"
        elif end == self.arrB:
            b = "B"
        elif end == self.arrC:
            b = "C"
        print ()
        print ("Moving {0:}   from peg {1:} -> peg {2:}\n".format(number, a, b))
        self.out()

    def move(self, n = None, beg = None, mid = None, end = None):
        move = self.move

        if n == None:
            n = self.number
            beg = self.arrA
            mid = self.arrB
            end = self.arrC

        if n>0:
            move(n-1, beg, end, mid)
            self.moveNumber(beg, end)
            move(n-1, mid, beg, end)

tower = Hanoi(3)
tower.move()
