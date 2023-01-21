def move_disk(n, start, end, helper):
    if n == 1:
        print(f"{start} -> {end}")
    else:
        move_disk(n-1, start, helper, end)
        print(f"{start} -> {end}")
        move_disk(n - 1, helper, end, start)

move_disk(3, "A", "B", "C")

