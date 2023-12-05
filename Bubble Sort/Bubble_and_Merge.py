import random
import time
import matplotlib.pyplot as plt

def bubble_sort(lista):
    n = len(lista)
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

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    middle = len(arr) // 2
    left_array = arr[:middle]
    right_array = arr[middle:]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    return merge(sorted_left_array, sorted_right_array)

def merge(left, right):
    merged = []  # Crea una lista vacía para almacenar la fusión de los dos arrays
    left_idx, right_idx = 0, 0  # Inicializa los índices para recorrer los arrays izquierdo y derecho

    # Combinación ordenada de los elementos de los arrays izquierdo y derecho
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:  # Compara los elementos del array izquierdo y derecho
            merged.append(left[left_idx])  # Agrega el elemento del array izquierdo a la lista fusionada
            left_idx += 1  # Incrementa el índice del array izquierdo
        else:
            merged.append(right[right_idx])  # Agrega el elemento del array derecho a la lista fusionada
            right_idx += 1  # Incrementa el índice del array derecho

    # Agrega los elementos restantes del array izquierdo y derecho a la lista fusionada
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    return merged  # Devuelve el array fusionado y ordenado

def merge_sort(arr):
    if len(arr) <= 1:  # Verifica si el array tiene 0 o 1 elemento (ya está ordenado)
        return arr
    
    middle = len(arr) // 2  # Encuentra el punto medio del array
    left_array = arr[:middle]  # Divide el array en dos partes: izquierda y derecha
    right_array = arr[middle:]

    # Aplica merge_sort recursivamente en las dos mitades del array
    sorted_left_array = merge_sort(left_array)
    sorted_right_array = merge_sort(right_array)

    # Combina y ordena las dos mitades utilizando la función merge
    return merge(sorted_left_array, sorted_right_array)  # Retorna la fusión ordenada de las dos mitades

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
Ordenamientos = [bubble_sort, merge_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Bubble Sort y Merge Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()