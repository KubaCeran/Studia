import math

def binary_search(table, value, left, right):
    global counter
    counter += 1
    table.sort()
    print(f"Wywolanie nr {counter}")
    print(f"szukam w przedziale: ({left+1}; {right+1})")
    print()

    if left > right:
        print("Nie znaleziono szukanej wartosci")

    else:
        index = math.floor((left + right) / 2)
        number = table[index]
        if number == value:
            print(f"Znaleziono szukana wartosc na pozycji {index+1}")
        else:
            if value > number:
                binary_search(table, value, index + 1, right)
            else:
                binary_search(table, value, left, index-1)


table = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]  # tutaj skopiuj tablice
value = 2  # tutaj wklej szukana liczbe
mini = 1  # zakres od
maxi = 15  # zakres do

counter = 0
binary_search(table, value, mini-1, maxi-1)
print(f"Ilość wywołań funkcji binary_search wynosi {counter}")