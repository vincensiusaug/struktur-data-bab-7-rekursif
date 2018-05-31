def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1

def nchoosek(n, k):
    return fact(n)/(fact(k)*fact(n-k))

print (nchoosek(5,2))
