def out():
    for i in range (count-1,-1,-1):
        try:
            print ("{0:^3}".format(a[i]),end="")
        except IndexError:
            print ("{0:^3}".format("-"),end="")

        try:
            print ("{0:^3}".format(b[i]),end="")
        except IndexError:
            print ("{0:^3}".format("-"),end="")

        try:
            print ("{0:^3}".format(c[i]))
        except IndexError:
            print ("{0:^3}".format("-"))
    print ("{0:=<9}".format(""))

def move(beg, end):
    end.append(beg.pop())
    out()

def move_all(n, beg, mid, end):
    if n==1:
        move(beg, end)
    else:
        move_all(n-1, beg, end, mid)
        move_all(1, beg, mid, end)
        move_all(n-1, mid, beg, end)

a = [10,9,8,7,6,5,4,3,2,1]
b = []
c = []

count = len(a)

out()

move_all(count, a, b, c)
