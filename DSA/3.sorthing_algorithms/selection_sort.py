def selection_sort(A):
    length = len(A)
    for i in range(length-1):
        position = i

        for j in range(i+1, length):
            if A[j] < A[position]:
                position = j

        if position != i:        
            temp = A[i]
            A[i] = A[position]
            A[position] = temp
            
    return A


array = [5,4,7,9,3]

print("Original Array:",array)
array = selection_sort(array)
print("Sorted Array: ",array)