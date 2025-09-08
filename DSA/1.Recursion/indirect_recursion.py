#indirect recursion

def funA(n):
    if n > 0:
        print(n, end=" ")
        funB(n-1)

def funB(n):
    if n > 0:
        print(n, end=" ")
        funA(n-1)

funA(10)
