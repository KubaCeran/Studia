def merge_sort(arr, level):
    global counter_sort
    global level_sort
    counter_sort += 1
    level_sort = max(level_sort, level)

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, level + 1)
        merge_sort(R, level + 1)
        merge(arr, L, R, level)


def merge(arr, L, R, level):
    global counter_merge
    global level_merge
    counter_merge += 1
    level_merge = max(level_merge, level)

    i = j = k = 0
    n1 = len(L)
    n2 = len(R)

    # Copy data to temp arrays L[] and R[]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


numbers = [5, -2, 11, 7, 10, -5]  # tu wklej tablice

counter_sort = 0
counter_merge = 0
level_sort = 0
level_merge = 0

merge_sort(numbers, 1)
print(f"Ilość wywołań rekurecyjnych procedury sortującej wynosi {counter_sort}")
print(f"Ilość poziomów wywołań rekurecyjnych procedury sortującej wynosi {level_sort}")
print(f"Ilość wywołań procedury scalania wynosi {counter_merge}")
print(f"Ilość poziomów wywołań procedury scalania wynosi {level_merge}")
print(numbers)
