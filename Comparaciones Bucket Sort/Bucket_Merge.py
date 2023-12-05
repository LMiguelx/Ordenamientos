# Importación de bibliotecas necesarias
import random
import time
import matplotlib.pyplot as plt

# Definición del algoritmo de Ordenamiento por Cubetas (Bucket Sort)
def bucket_sort(array):
    num_buckets = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_range = (max_value - min_value) / num_buckets

    # Inicialización de cubetas vacías
    buckets = [[] for _ in range(num_buckets)]

    # Distribuir elementos en las cubetas
    for i in range(len(array)):
        index = int((array[i] - min_value) // bucket_range)
        if index != num_buckets:
            buckets[index].append(array[i])
        else:
            buckets[num_buckets - 1].append(array[i])

    # Ordenar cada cubeta
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenar las cubetas ordenadas para obtener el arreglo final ordenado
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Definición de la función de combinación para Merge Sort
def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    # Agregar los elementos restantes de ambas listas
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged

# Definición del algoritmo de Ordenamiento por Mezcla (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    # Llamada recursiva para ordenar las sublistas izquierda y derecha
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)

    # Combinar las sublistas ordenadas
    return merge(sorted_left_array, sorted_right_array)

# Función para generar un arreglo aleatorio de un tamaño dado
def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    return time.time() - start_time

# Obtener la entrada del usuario para el tamaño del arreglo
array_size = int(input("Ingrese el tamaño del arreglo: "))

# Generar un arreglo aleatorio del tamaño especificado
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [bucket_sort, merge_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar los tiempos de ejecución gráficamente
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Bucket Sort y Merge Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()
