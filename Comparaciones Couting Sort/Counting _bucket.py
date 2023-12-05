import random
import time
import matplotlib.pyplot as plt

def counting_sort(array):
    max_num = max(array)
    count = [0] * (max_num + 1)
    output = [0] * len(array)

    for num in array:
        count[num] += 1

    for i in range(1, max_num + 1):
        count[i] += count[i - 1]

    for i in range(len(array) - 1, -1, -1):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1

    return output

def bucket_sort(array):
    num_buckets = len(array)
    max_value = max(array)
    min_value = min(array)
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for i in range(len(array)):
        index = int((array[i] - min_value) // bucket_range)
        if index != num_buckets:
            buckets[index].append(array[i])
        else:
            buckets[num_buckets - 1].append(array[i])

    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]

def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    return time.time() - start_time

array_size = int(input("Ingrese el tamaño del arreglo: "))
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [counting_sort, bucket_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Counting Sort y Bucket Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()