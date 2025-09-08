def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap>0:
        i = gap
        while i < n :
            temp = A[i]
            j = i - gap
            while j>=0 and A[j]>temp:
                A[j+gap] = A[j]
                j = j - gap
            A[j+gap] = temp
            i = i + 1 
        gap = gap//2
    return A


array  = [3,6,4,7,5,2,9,1]
print("Original Array:",array)
array = shell_sort(array)
print("Sorted Array: ",array)