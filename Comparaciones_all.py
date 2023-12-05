import random
import time
import matplotlib.pyplot as plt

# Algoritmo de ordenamiento de burbuja
def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        # Variable para saber si se hizo algún intercambio
        intercambio = False
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j+1]:
                # Intercambiamos los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # Marcamos que se hizo un intercambio
                intercambio = True
        # Si no se hizo ningún intercambio en la iteración, la lista está ordenada
        if not intercambio:
            break
    return lista

# Algoritmo de Bucket Sort
def bucket_sort(array):
    # Crear un número de buckets igual al número de elementos en el arreglo
    num_buckets = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_range = (max_value - min_value) / num_buckets

    # Crear los buckets
    buckets = [[] for _ in range(num_buckets)]

    # Agregar elementos a los buckets
    for i in range(len(array)):
        index = int((array[i] - min_value) // bucket_range)
        if index != num_buckets:
            buckets[index].append(array[i])
        else:
            buckets[num_buckets - 1].append(array[i])

    # Ordenar cada bucket individualmente usando cualquier algoritmo de ordenamiento
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenar los buckets ordenados para obtener el arreglo ordenado final
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Algoritmo de Counting Sort
def counting_sort(array):
    max_num = max(array)
    count = [0] * (max_num + 1)
    output = [0] * len(array)

    # Contar la frecuencia de cada elemento en el arreglo
    for num in array:
        count[num] += 1

    # Calcular la posición final de cada elemento en el arreglo ordenado
    for i in range(1, max_num + 1):
        count[i] += count[i - 1]

    # Construir el arreglo ordenado utilizando la información de posición final
    for i in range(len(array) - 1, -1, -1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    return output

# Algoritmo de Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        # Mover elementos mayores que key a una posición adelante
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Algoritmo de Merge Sort
def mergeSort(arr):
    # Caso base: si el tamaño del arreglo es 1, ya está ordenado
    if len(arr) == 1:
        return arr
    
    # Dividir el arreglo en dos mitades
    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    # Llamadas recursivas para ordenar las dos mitades
    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    # Combinar las dos mitades ordenadas
    return merge(sorted_left_array, sorted_right_array)

# Función auxiliar para el Merge Sort
def merge(left_arr, right_arr):
    arr_resultado = []

    # Comparar y fusionar los elementos de las dos mitades ordenadas
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_resultado.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_resultado.append(left_arr[0])
            left_arr.pop(0)
    
    # Agregar los elementos restantes del subarreglo no vacío
    while len(left_arr) > 0:
        arr_resultado.append(left_arr[0])
        left_arr.pop(0)

    while len(right_arr) > 0:
        arr_resultado.append(right_arr[0])
        right_arr.pop(0)

    # Devolver el subarreglo ordenado resultante
    return arr_resultado

# Algoritmo de Quick Sort
def quicksort(arr):
    # Caso base: si el tamaño del arreglo es 1 o menor, ya está ordenado
    if len(arr) <= 1:
        return arr
    
    # Seleccionar el pivote como el elemento en la mitad del arreglo
    pivot = arr[len(arr) // 2]
    
    # Dividir el arreglo en tres partes: menores que el pivote, iguales al pivote, y mayores que el pivote
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Llamadas recursivas para ordenar las partes menores y mayores
    return quicksort(left) + middle + quicksort(right)

# Algoritmo de Selection Sort
def selection_sort(array):
    # Iterar sobre cada elemento del arreglo
    for i in range(len(array)):
        # Encontrar el índice del mínimo en la parte no ordenada del arreglo
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        # Intercambiar el elemento actual con el mínimo encontrado
        array[i], array[min_index] = array[min_index], array[i]
    
    # Devolver el arreglo ordenado
    return array

# Función para generar un arreglo aleatorio
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())  # Usar una copia para no afectar el arreglo original
    return time.time() - start_time

# Parámetro: tamaño del arreglo
array_size = int(input("Ingrese el tamaño del arreglo: "))

# Generar un arreglo de números aleatorios
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [bubblesort, bucket_sort, counting_sort, insertion_sort, mergeSort, quicksort, selection_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de diferentes algoritmos de ordenamiento')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')

plt.show()