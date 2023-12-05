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

# Definición del algoritmo de Ordenamiento Rápido (Quick Sort)
def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr

    # Seleccionar el pivote como el elemento en la mitad del arreglo
    pivot = arr[len(arr) // 2]

    # Dividir el arreglo en tres partes: menor, igual y mayor que el pivote
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Llamadas recursivas para ordenar las partes izquierda y derecha
    return Quick_Sort(left) + middle + Quick_Sort(right)

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
Ordenamientos = [bucket_sort, Quick_Sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar los tiempos de ejecución gráficamente
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Bucket Sort y Quick Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()
