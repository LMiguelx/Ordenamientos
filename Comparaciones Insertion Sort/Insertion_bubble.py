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

# Función que implementa el algoritmo de ordenamiento burbuja
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

# Función que genera un array aleatorio de un tamaño especificado
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
Ordenamientos = [insertion_sort, bubble_sort]

# Medir el tiempo de ejecución para cada algoritmo
for algoritmo in Ordenamientos:
    tiempo = measure_time(algoritmo, random_array)
    tiempos.append(tiempo)
    print(f"{algoritmo.__name__}: {tiempo:.3f} segundos")

# Visualizar gráficamente los tiempos de ejecución
nombres_algoritmos = [algoritmo.__name__ for algoritmo in Ordenamientos]
plt.bar(nombres_algoritmos, tiempos)
plt.title('Tiempo de ejecución de Insertion Sort y Bubble Sort')
plt.xlabel('Algoritmo')
plt.ylabel('Tiempo (segundos)')
for i, tiempo in enumerate(tiempos):
    plt.text(i, tiempo, f'{tiempo:.3f} s', ha='center', va='bottom')
plt.show()