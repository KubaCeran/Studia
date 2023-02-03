def fibo_tab(number):
    global counter_func
    numbers = list()
    for i in range(0, number):
        if i < 2:
            numbers.append(1)
        else:
            numbers.append(numbers[i - 2] + numbers[i - 1])
            counter_func += 1
    return numbers


counter_func = 0

number = int((input("Napisz, który element ciągu: ")))
result = fibo_tab(number)
print(f"F{number} -> {result[number - 1]}")
print(f"Funkcja wyliczająca tę wartość wywołana została {counter_func} razy \n")

print("Cały ciąg:")
for k in range(0, len(result)):
    print(f"F{k+1} -> {result[k]}")
