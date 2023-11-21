from itertools import repeat
from multiprocessing import cpu_count, Pool
import numpy as np
import time

M = 5_000
N = 5_000


def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]

    return suma



if __name__ == "__main__":
    resultado = list()

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N,))
    
    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    with Pool(processes=cpu_count()) as pool:
        resultado = pool.starmap(mult_vector_vector, args)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion sincrono: {fin - inicio} segundos")
