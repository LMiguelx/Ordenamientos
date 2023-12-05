import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    n = len(lista) #almacenamos longitud de lista
    for i in range(n):
        #variable para saber si se hizo algún intercambio
        
        intercambio = False
        for j in range(0, n-i-1):
            # Si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j+1] :
                # Intercambiamos los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # Marcamos que se hizo un intercambio
                intercambio = True
        # Si no se hizo ningún intercambio en la iteración, la lista está ordenada
        if not intercambio:
            break
    return lista

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
    return [random.randint(1, 10000) for _ in range(size)]

def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())
    return time.time() - start_time

array_size = int(input("Ingrese el tamaño del arreglo: "))
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [bubble_sort, bucket_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Bubble Sort y Bucket Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()