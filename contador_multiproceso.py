import time
from multiprocessing import Process


CUENTA = 50_000_000

num_cuentas = 0


def cuenta(n):
    global num_cuentas
    num_cuentas += 1
    print(f"Numero de cuentas: {num_cuentas}, ID: {id(num_cuentas)}")
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    p1 = Process(target=cuenta, args=(CUENTA // 2, ))
    p2 = Process(target=cuenta, args=(CUENTA // 2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()
    print(f'Conteo de {CUENTA} en {fin - inicio} segundos')
