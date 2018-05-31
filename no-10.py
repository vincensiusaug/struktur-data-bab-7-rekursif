def power(x, n):
    if n>1:
        return x * power(x, n-1)
    else:
        return x

def user_out(arr):
    for i in range(len(arr)):
        print (arr[i],end="")
        if i<len(arr)-1:
            print ("^",end="")
    print ()

def program(arr, amount):
    user_out(arr)
    if amount>0:
        arr[amount-1] = power(arr[amount-1], arr[amount])
        arr.pop()
        return program(arr, amount-1)
    else:
        return arr[amount]


example = [3,3,2]
amount = len(example)-1
program(example,amount)
