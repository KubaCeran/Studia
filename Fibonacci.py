def fibo_rec(number, level):
    global counter
    global level_fibo
    level_fibo = max(level_fibo, level)
    counter += 1
    if number <= 2:
        return 1
    else:
        result = fibo_rec(number - 2, level + 1) + fibo_rec(number - 1, level + 1)
        return result


counter = 0
level_fibo = 0

number = (input("Napisz, który element ciągu: "))

result = fibo_rec(int(number), 1)
print(f"F{number} -> {result} (liście drzewa)")
print(f"Funkcja fibo_rec() wywołana -> {counter} razy")
print(f"Glebia fibo_rec() -> {level_fibo} ")
