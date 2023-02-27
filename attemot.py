import random
import time
import matplotlib.pyplot as plt
from mergesort import merge_sort
from insertsort import insertion_sort

# Generate two random lists of integers
list1 = [random.randint(0, 100) for _ in range(1000)]
list2 = [random.randint(0, 100) for _ in range(1000)]

# Sort list1 using merge sort and time it
start_time = time.time()
merge_sort(list1)
merge_sort_time = time.time() - start_time

# Sort list2 using insertion sort and time it
start_time = time.time()
insertion_sort(list2)
insertion_sort_time = time.time() - start_time

# Plot a bar graph of the sorting times
labels = ['Merge Sort', 'Insertion Sort']
times = [merge_sort_time, insertion_sort_time]
plt.bar(labels, times)
plt.ylabel('Time (s)')
plt.title('Sorting Efficiency')
plt.show()
