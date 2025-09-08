def merge(A,left,mid,right):
    i = left
    j = mid + 1 
    k = left
    B = [0] * (right+1)
    while(i<=mid and j<=right):
        if A[i]< A[j]:
            B[k] = A[i]
            i = i + 1 
        else:
            B[k]= A[j]
            j = j+1
        k= k+1
    while i<=mid:
        B[k] = A[i]
        i = i + 1
        k = k+1

    while j <= right:
        B[k]= A[j]
        j= j+1
        k = k+1

    for x in range(left,right+1):
        A[x] = B[x]
        


def merge_sort(A,left,right):
    if left < right:
        mid = (left+right)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right)
        merge(A,left,mid,right)


array  = [3,6,4,7,5,8,2,9,1]
print("Original Array:",array)
merge_sort(array ,0 , len(array)-1)
print("Sorted Array: ",array)
