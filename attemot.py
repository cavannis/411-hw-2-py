import random
import time
import matplotlib.pyplot as plt
from merge_sort import merge_sort
from insertion_sort import insertion_sort

# Generate lists of integers of increasing size
sizes = [10, 20, 30, 40, 50, 75, 100, 200, 300, 400, 500, 750, 1000]
lists = [[random.randint(0, 100) for _ in range(size)] for size in sizes]

# Sort each list using merge sort and insertion sort and time the operations
merge_sort_times = []
insertion_sort_times = []
for lst in lists:
    start_time = time.time()
    merge_sort(lst)
    merge_sort_times.append(time.time() - start_time)

    start_time = time.time()
    insertion_sort(lst)
    insertion_sort_times.append(time.time() - start_time)

# Plot a scatter plot of the sorting times versus the input size
plt.scatter(sizes, merge_sort_times, label='Merge Sort')
plt.scatter(sizes, insertion_sort_times, label='Insertion Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Sorting Efficiency')
plt.legend()
plt.show()
