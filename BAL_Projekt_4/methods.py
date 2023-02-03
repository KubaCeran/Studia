def find_max_number2(tab):
    n = len(tab)
    max_num = tab[0]
    count = 1
    for i in range(1, n):
        if tab[i] == max_num:
            count += 1
        else:
            if tab[i] > max_num:
                max_num = tab[i]
                count = 1
    return max_num, count


def find_distance(max_num, count, tab, n):
    if count == 1:
        return 0
    else:
        max_counter = 0
        index = 0
        min_dist = n
        for i in range(0, n):
            if tab[i] == max_num:
                temp_dist = i - index
                index = i
                max_counter += 1
                if max_counter > 1:
                    if temp_dist < min_dist:
                        min_dist = temp_dist
                        if max_counter == count:
                            return min_dist
        return min_dist


def find_max_number(tab, n):
    empty_tab = []
    if tab == empty_tab:
        return 0, 0, 0
    else:
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








