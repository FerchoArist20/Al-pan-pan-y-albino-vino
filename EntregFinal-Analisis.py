
import requests               # O(1)
import random                 # O(1)
import math                   # O(1)
from tkinter import *         # O(1)
from tkinter import messagebox  # O(1)

def merge_sort(arr):          # O(n log n)
    if len(arr) <= 1:         # O(1)
        return arr
    mid = len(arr) // 2       # O(1)
    left = merge_sort(arr[:mid])  # Recursión: T(n/2)
    right = merge_sort(arr[mid:])  # Recursión: T(n/2)
    return merge(left, right)   # O(n)

def merge(left, right):       # O(n)
    merged = []               # O(1)
    i = j = 0                 # O(1)
    while i < len(left) and j < len(right):  # O(n)
        if left[i] < right[j]:  # O(1)
            merged.append(left[i])  # O(1)
            i += 1                 # O(1)
        else:
            merged.append(right[j])  # O(1)
            j += 1                 # O(1)
    merged.extend(left[i:])    # O(n)
    merged.extend(right[j:])   # O(n)
    return merged              # O(1)

def counting_sort(arr):       # O(n + k)
    if len(arr) == 0:         # O(1)
        return arr
    min_value = min(arr)      # O(n)
    max_value = max(arr)      # O(n)
    count = [0] * (max_value - min_value + 1)  # O(k)
    for num in arr:           # O(n)
        count[num - min_value] += 1   # O(1)
    sorted_arr = []           # O(1)
    for i, freq in enumerate(count):  # O(k)
        sorted_arr.extend([i + min_value] * freq)  # O(1)
    return sorted_arr         # O(n)

def heapify(arr, n, i):       # O(log n)
    largest = i              # O(1)
    l = 2 * i + 1            # O(1)
    r = 2 * i + 2            # O(1)

    if l < n and arr[i] < arr[l]:  # O(1)
        largest = l           # O(1)

    if r < n and arr[largest] < arr[r]:  # O(1)
        largest = r           # O(1)

    if largest != i:         # O(1)
        arr[i], arr[largest] = arr[largest], arr[i]  # O(1)
        heapify(arr, n, largest)  # Recursión: T(n/2)

def heap_sort(arr):           # O(n log n)
    n = len(arr)              # O(1)
    for i in range(n // 2 - 1, -1, -1):  # O(n)
        heapify(arr, n, i)     # O(log n)

    for i in range(n - 1, 0, -1):  # O(n)
        arr[i], arr[0] = arr[0], arr[i]  # O(1)
        heapify(arr, i, 0)     # O(log n)

def partition(arr, low, high):  # O(n)
    i = low - 1               # O(1)
    pivot = arr[high]         # O(1)
    for j in range(low, high):  # O(n)
        if arr[j] < pivot:    # O(1)
            i += 1           # O(1)
            arr[i], arr[j] = arr[j], arr[i]  # O(1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # O(1)
    return i + 1              # O(1)

def quick_sort(arr, low, high):  # O(n log n) on average, O(n^2) worst case
    if low < high:             # O(1)
        pi = partition(arr, low, high)  # O(n)
        quick_sort(arr, low, pi - 1)   # Recursión: T(n/2)
        quick_sort(arr, pi + 1, high)  # Recursión: T(n/2)

def counting_sort_radix(arr, exp):  # O(n + k)
    n = len(arr)              # O(1)
    output = [0] * n          # O(n)
    count = [0] * 10         # O(k)

    for i in range(n):       # O(n)
        index = arr[i] // exp   # O(1)
        count[index % 10] += 1  # O(1)

    for i in range(1, 10):    # O(k)
        count[i] += count[i - 1]  # O(1)

    i = n - 1                 # O(1)
    while i >= 0:             # O(n)
        index = arr[i] // exp    # O(1)
        output[count[index % 10] - 1] = arr[i]  # O(1)
        count[index % 10] -= 1   # O(1)
        i -= 1                 # O(1)

    for i in range(n):       # O(n)
        arr[i] = output[i]   # O(1)

def radix_sort(arr):         # O(d * (n + k))
    max_value = max(arr)     # O(n)
    exp = 1                  # O(1)
    while max_value // exp > 0:   # O(d)
        counting_sort_radix(arr, exp)  # O(n + k)
        exp *= 10            # O(1)

def bubble_sort(arr):        # O(n^2)
    n = len(arr)              # O(1)
    for i in range(n - 1):    # O(n)
        for j in range(0, n - i - 1):  # O(n)
            if arr[j] > arr[j + 1]:   # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)

def get_random_names(num_names):   # O(num_names)
    response = requests.get(f'https://randomuser.me/api/?results={num_names}&inc=name')  # O(1)
    data = response.json()       # O(1)
    names = []                   # O(1)
    for result in data['results']:   # O(num_names)
        first_name = result['name']['first']  # O(1)
        last_name = result['name']['last']    # O(1)
        full_name = f"{first_name} {last_name}"  # O(1)
        names.append(full_name)   # O(1)
    return names                 # O(1)

def calculate_combinations(n, r):   # O(1)
    return math.comb(n, r)       # O(1)

def calculate_permutations(n, r):   # O(1)
    return math.perm(n, r)       # O(1)

def calculate_variations(n, r):   # O(1)
    return math.perm(n, r)       # O(1)

def sort_names():
    num_names = int(entry_num_names.get())   # O(1)
    names = get_random_names(num_names)      # O(num_names)

    selected_sort = sort_var.get()          # O(1)

    if selected_sort == "MergeSort":        # O(n log n)
        sorted_names = merge_sort(names.copy())   # O(n log n)
    elif selected_sort == "CountingSort":   # O(n + k)
        name_lengths = [len(name) for name in names]   # O(num_names)
        sorted_name_lengths = counting_sort(name_lengths.copy())   # O(num_names + max_length)
        sorted_names = [name for _, name in sorted(zip(name_lengths, names))]   # O(num_names)
    elif selected_sort == "HeapSort":       # O(n log n)
        names_heap = names.copy()            # O(num_names)
        heap_sort(names_heap)                # O(n log n)
        sorted_names = names_heap            # O(1)
    elif selected_sort == "QuickSort":      # O(n log n) on average, O(n^2) worst case
        names_quick = names.copy()           # O(num_names)
        quick_sort(names_quick, 0, len(names_quick) - 1)   # O(n log n) on average, O(n^2) worst case
        sorted_names = names_quick           # O(1)
    elif selected_sort == "RadixSort":      # O(d * (n + k))
        name_lengths_radix = [len(name) for name in names]   # O(num_names)
        radix_sort(name_lengths_radix)        # O(d * (n + k))
        sorted_names = [name for _, name in sorted(zip(name_lengths_radix, names))]   # O(num_names)
    elif selected_sort == "BubbleSort":     # O(n^2)
        names_bubble = names.copy()           # O(num_names)
        bubble_sort(names_bubble)              # O(n^2)
        sorted_names = names_bubble            # O(1)

    combinations = calculate_combinations(num_names, 3)    # O(1)
    permutations = calculate_permutations(num_names, 3)    # O(1)
    variations = calculate_variations(num_names, 3)        # O(1)

    messagebox.showinfo("Resultados",   # O(1)
                        f"Ordenamiento: {selected_sort}\n\n"
                        f"Nombres Ordenados:\n{sorted_names}\n\n"
                        f"Combinaciones: {combinations}\n"
                        f"Permutaciones: {permutations}\n"
                        f"Variaciones: {variations}")

# Crear ventana y configuración  # O(1)
window = Tk()                     # O(1)
window.title("Interfaz de Ordenamiento")   # O(1)
window.geometry("400x250")         # O(1)

# Etiqueta y entrada para el número de nombres  # O(1)
label_num_names = Label(window, text="Número de Nombres:")   # O(1)
label_num_names.pack()              # O(1)
entry_num_names = Entry(window)      # O(1)
entry_num_names.pack()               # O(1)

# Opciones de selección de ordenamiento  # O(1)
sort_var = StringVar()               # O(1)
sort_var.set("MergeSort")            # O(1)

label_sort = Label(window, text="Ordenamiento:")   # O(1)
label_sort.pack()                      # O(1)

rb_merge = Radiobutton(window, text="MergeSort", variable=sort_var, value="MergeSort")   # O(1)
rb_merge.pack()                        # O(1)

rb_counting = Radiobutton(window, text="CountingSort", variable=sort_var, value="CountingSort")   # O(1)
rb_counting.pack()                     # O(1)

rb_heap = Radiobutton(window, text="HeapSort", variable=sort_var, value="HeapSort")   # O(1)
rb_heap.pack()                        # O(1)

rb_quick = Radiobutton(window, text="QuickSort", variable=sort_var, value="QuickSort")   # O(1)
rb_quick.pack()                        # O(1)

rb_radix = Radiobutton(window, text="RadixSort", variable=sort_var, value="RadixSort")   # O(1)
rb_radix.pack()                        # O(1)

rb_bubble = Radiobutton(window, text="BubbleSort", variable=sort_var, value="BubbleSort")   # O(1)
rb_bubble.pack()                        # O(1)

# Botón para ordenar nombres y mostrar resultados  # O(1)
button_sort = Button(window, text="Ordenar", command=sort_names)   # O(1)
button_sort.pack()                   # O(1)

window.mainloop()                    # O(1)


#Complejidad de O(n**n)

