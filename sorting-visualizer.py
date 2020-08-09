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

num_elems = int(input("Enter num elements: "))
algorithm = int(input("Choose Algorithm: 1. Bubble Sort \n 2. Insertion Sort \n 3. Selection Sort \n 4. Quick Sort \n 5. Merge Sort \n 6. Radix Sort \n 7. Heap Sort \n 8. Shell Sort \n 9. Counting Sort \n"))
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
    name = "Radix Sort"
    alg = radix_sort(array)
elif algorithm == 7:
    name = "Heap Sort"
    alg = heap_sort(array)
elif algorithm == 8:
    name = "Shell Sort"
    alg = shell_sort(array)
elif algorithm == 9:
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