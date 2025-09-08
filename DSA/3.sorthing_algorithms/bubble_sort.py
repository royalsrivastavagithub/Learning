def bubble_sort(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if (A[i] < A[j]):
                A[i], A[j] = A[j], A[i]
    return A


arr = [7, 4, 6, 5, 3, 9, 1]
print("Original Array", arr)
arr = bubble_sort(arr)
print("Sorted Array", arr)
