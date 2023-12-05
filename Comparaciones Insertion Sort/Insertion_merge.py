import random
import time
import matplotlib.pyplot as plt

def insertion_sort(array):
    for i in range(1, len(array)):  # Itera sobre el array empezando desde el segundo elemento
        key = array[i]  # Guarda el valor actual para compararlo y posiblemente insertarlo en su lugar correcto
        j = i - 1  # Establece el índice del elemento anterior al valor actual
        while j >= 0 and key < array[j]:  # Busca el lugar adecuado para insertar el valor actual
            array[j + 1] = array[j]  # Desplaza los elementos mayores al valor actual hacia la derecha
            j -= 1  # Decrementa el índice para comparar con elementos anteriores
        array[j + 1] = key  # Inserta el valor actual en su posición correcta
    return array  # Devuelve el array ordenado

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
    return merge(sorted_left_array, sorted_right_array)  # Retorna la fusión ordenada de las dos mitades

def generate_random_array(size):
    return [random.randint(1, 100000) for _ in range(size)]  # Genera un array con números aleatorios entre 1 y 100,000

# Función que mide el tiempo de ejecución de una función de ordenamiento sobre un array dado
def measure_time(sort_function, array):
    start_time = time.time()  # Registra el tiempo de inicio
    sort_function(array.copy())  # Ejecuta la función de ordenamiento sobre una copia del array para no modificar el original
    return time.time() - start_time  # Devuelve el tiempo transcurrido durante la ejecución de la función de ordenamiento

array_size = int(input("Ingrese el tamaño del arreglo: "))
random_array = generate_random_array(array_size)

# Lista para almacenar los tiempos de ejecución de cada algoritmo
tiempos = []

# Algoritmos de ordenamiento a probar
Ordenamientos = [insertion_sort, merge_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Insertion Sort y Merge Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()