from multiprocessing import Pool
import time

proc = 4
tareas = 16

def potencia(n, div = tareas):
    res = 1

    rango = n // div

    for _ in range(rango):
        res *= n

    return res


if __name__ == '__main__':
    start = time.perf_counter()
    with Pool(processes=proc) as pool:
        res = pool.map(potencia, [100_000] * tareas)    
    end = time.perf_counter()
    print(f"Tiempo de ejecucion es: {end - start} segundos")
