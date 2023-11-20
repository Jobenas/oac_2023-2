import time
from threading import Thread

CUENTA = 50_000_000


def cuenta(n, nombre):
    while n > 0:
        n -= 1
        if n % 100_000 == 0:
            print(f"{nombre}")


if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(CUENTA // 2, "t1"))
    t2 = Thread(target=cuenta, args=(CUENTA // 2, "t2"))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()
    print(f'Conteo de {CUENTA} en {fin - inicio} segundos')
