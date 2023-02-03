def find_max_number(tab, n):
    max_num = tab[0]
    count = 1
    index = 0
    min_dist = n
    for i in range(1, n):
        if tab[i] == max_num:
            count += 1
            temp_dist = i - index
            index = i
            if temp_dist < min_dist:
                min_dist = temp_dist
        else:
            if tab[i] > max_num:
                max_num = tab[i]
                min_dist = n
                count = 1
                index = i

    if count == 1:
        min_dist = 0
    return max_num, count, min_dist


while True:
    value = input("Insert list of numbers (e.g. 9, 4, 9, 1, 7, 2, 9): ")

    tab1 = value.split(', ')
    n1 = len(tab1)
    for j in range(0, n1):
        tab1[j] = int(tab1[j])

    result = find_max_number(tab1, n1)
    max_num1 = result[0]
    count1 = result[1]
    min_dist1 = result[2]
    print(f"Max numbers is {max_num1} and it occurs {count1} times.")
    print(f"Min distance is {min_dist1}")


