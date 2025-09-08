def insertion_sort(A):
    n = len(A)
    for i in range(n):
        current_value = A[i]
        position = i 
        while position > 0 and A[position-1] > current_value:
            A[position] = A[position-1]
            position = position -1
            A[position] = current_value
    
    return A

arr = [3,6,4,7,5,2,9,1]
print("Original Array:",arr)
arr = insertion_sort(arr)
print("Sorted Array:",arr)
