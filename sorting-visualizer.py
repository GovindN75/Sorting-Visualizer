import random
import matplotlib.pyplot as plt
import matplotlib.animation as manim


def bubble_sort(array):
    if len(array) <= 1:
        return 
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            yield array

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
            yield array
        if min_index != i:
            array[i],array[min_index] = array[min_index], array[i]
            yield array

def insertion_sort(array):
    if len(array)==1:
        return 
    for i in range(1, len(array)):
        j=i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j-=1
            yield array

def quick_sort(array, i, j):
    if i > j:
        return
    pivot = array[j]
    pivot_index = i
    for x in range(i, j):
        if array[x] < pivot:
            array[x], array[pivot_index] = array[pivot_index], array[x]
            pivot_index += 1
        yield array
    array[j], array[pivot_index] = array[pivot_index], array[j]
    yield array

    yield from quick_sort(array, i, pivot_index - 1)
    yield from quick_sort(array, pivot_index + 1, j)

def merge_sort(array, left, right):
    if right <= left:
        return
    elif left < right:
        mid = (left+right)//2
        yield from merge_sort(array, left, mid)
        yield from merge_sort(array, mid+1, right)
        yield from merge(array, left, mid, right)
        yield array

def merge(array, left, mid, right):
    arr = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if array[i] < array[j]:
            arr.append(array[i])
            i+=1
        else:
            arr.append(array[j])
            j+=1
    if i > mid:
        while j <= right:
            arr.append(array[j])
            j+=1
    else:
        while i <= mid:
            arr.append(array[i])
            i+=1
    for i,val in enumerate(arr):
        array[left+i] = val
        yield array 


def count_sort(array):
    max_num = max(array)
    num = max_num + 1
    count = [0] * num
    for i in array:
        count[i] += 1
        yield array
    x = 0
    for i in range(num):
        for j in range(count[i]):
            array[x] = i
            x += 1
            yield array
        yield array

def heap_sort(array):
    num_elems = len(array)
    for i in range(num_elems, -1, -1):
        yield from heapify(array, num_elems, i)
    for i in range(num_elems-1, -1, -1):
        array[0], array[i] = array[i], array[0]
        yield array
        yield from heapify(array, i, 0)

def heapify(array, num, i):
    max_ind = i
    left = i*2 + 1
    right = i*2 + 2
    while left < num and array[left] > array[max_ind]:
        max_ind = left
    while right < num and array[right] > array[max_ind]:
        max_ind = right
    if max_ind != i:
        array[i], array[max_ind] = array[max_ind], array[i]
        yield array
        yield from heapify(array, num, max_ind)

num_elems = int(input("Enter num elements: "))
algorithm = int(input("Choose Algorithm: \n 1. Bubble Sort \n 2. Insertion Sort \n 3. Selection Sort \n 4. Quick Sort \n 5. Merge Sort \n 6. Heap Sort \n 7. Counting Sort \n"))
array = [i+1 for i in range(num_elems)]
random.shuffle(array)

if algorithm == 1:
    name = "Bubble Sort"
    alg = bubble_sort(array)
elif algorithm == 2:
    name = "Insertion Sort"
    alg = insertion_sort(array)
elif algorithm == 3:
    name = "Selection Sort"
    alg = selection_sort(array)
elif algorithm == 4:
    name = "Quick Sort"
    alg = quick_sort(array, 0, num_elems-1)
elif algorithm == 5:
    name = "Merge Sort"
    alg = merge_sort(array, 0, num_elems-1)
elif algorithm == 6:
    name = "Heap Sort"
    alg = heap_sort(array)
elif algorithm == 7:
    name = "Counting Sort"
    alg = count_sort(array)

figure, axis = plt.subplots()
axis.set_title(name)
bar = axis.bar(range(len(array)), array, align='edge')
axis.set_xlim(0, num_elems)
axis.set_ylim(0, int(num_elems * 1.1))
text = axis.text(0.02, 0.95, "", transform=axis.transAxes)

num_operations = [0]
def update_display(array, bar, num_operations):
    for bar, val in zip(bar, array):
        bar.set_height(val)
    num_operations[0] += 1
    text.set_text(f"Number of Operations: {num_operations[0]}")

anima = manim.FuncAnimation(figure, func=update_display, fargs=(bar, num_operations), frames=alg, interval=1, repeat=False)
plt.show()