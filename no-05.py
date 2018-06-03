
def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1

def nchoosek(n, k):
    return fact(n)/(fact(k)*fact(n-k))

def n_table(n, k, f = 1):
    if f:
        print ()
        print ("|{0:=^16}|".format(""))
        print ("|{0:^3}|{1:^3}|{2:^8}|".format("N", "K", "Result"))
        print ("|{0:=^16}|".format(""))
    if n > 0:
        def k_table(k):
            if k > 0:
                if k >= n:
                    k_table(k-1)
                else:
                    print ("|{0:^3}|{1:^3}|{2:^8.0f}|".format(n, k, nchoosek(n, k)))
                    k_table(k-1)
        
        k_table(k)
        n_table(n-1, k, 0)
    else:
        print ("|{0:=^16}|".format(""))
        print ()

n_table(20,13)
