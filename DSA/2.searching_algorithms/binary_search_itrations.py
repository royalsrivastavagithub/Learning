#only works with sorted order
import math
def binary_search(A,n,key):
    L = 0 
    R = n-1
    while L<=R:
        m = math.floor((L+R)/2)
        if key == A[m]:
            print(m)
        elif key < A[m]:
            R =  m-1
        elif key > A[m]:
            L = m+1
    return "NotFound"

