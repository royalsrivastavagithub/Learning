array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def linear_search(A,n,key):
    index = 0
    while index < n:
        if A[index] == key:
            print("index: " , index)
            break
        index = index + 1
    else:
        print("Not Found")


linear_search(array,10,2)