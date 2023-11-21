import time


def potencia(n):
    res = 1

    for _ in range(n):
        res *= n

    return res


if __name__ == '__main__':
    start = time.perf_counter()
    res = potencia(100_000)
    end = time.perf_counter()
    print(f"Tiempo de ejecucion es: {end - start} segundos")
