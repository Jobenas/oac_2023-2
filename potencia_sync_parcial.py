import time


def potencia(n, div):
    res = 1

    rango = n // div

    for _ in range(rango):
        res *= n

    return res


if __name__ == '__main__':
    start = time.perf_counter()
    res1 = potencia(100_000, 2)
    res2 = potencia(100_000, 2)
    res = res1 * res2
    end = time.perf_counter()
    print(f"Tiempo de ejecucion es: {end - start} segundos")
