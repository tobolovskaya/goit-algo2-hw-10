import random
import time
import matplotlib.pyplot as plt

# Детермінований QuickSort

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right) if arr else []

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Вимірювання часу
import time
import random
import matplotlib.pyplot as plt

def measure_time(sort_function, arr):
    start = time.time()
    sort_result = sort_func(arr.copy())
    return time.time() - start

sizes = [10_000, 50_000, 100_000, 500_000]
randomized_times = []
deterministic_times = []

for size in sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]

    start = time.time()
    randomized_quick_sort(arr.copy())
    randomized_time = time.time() - start

    start = time.time()
    deterministic_quick_sort(arr.copy())
    deterministic_time = time.time() - start

    randomized_times.append(randomized_time)
    deterministic_times.append(deterministic_time)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {randomized_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд\n")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, label='Randomized QuickSort', marker='o')
plt.plot(sizes, deterministic_times, label='Deterministic QuickSort', marker='o')

plt.title("Порівняння алгоритмів QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Час виконання, с")
plt.legend()
plt.grid(True)
plt.show()
