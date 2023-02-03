from methods import find_max_number
from random import randint
import time
import matplotlib.pyplot as plt

times = list()
list1 = [randint(0, 1000) for i in range(200000)]
for x in range(1, 220000, 20000):
    start_time = time.time()
    tab = list1[:x]
    n = len(tab)
    list2 = find_max_number(tab, n)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

x = [i for i in range(1, 220000, 20000)]

plt.xlabel("No. of elements")
plt.ylabel("Time required [s]")
plt.plot(x, times)
plt.show()



