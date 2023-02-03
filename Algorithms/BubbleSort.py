def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp


numbers = [1, 5, 8, 3, 7, 2, 6, 4]
bubble_sort(numbers)
print(numbers)
