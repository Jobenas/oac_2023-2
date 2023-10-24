import asyncio
import time


async def func1():
    print("Funcion 1 empezando")
    await asyncio.sleep(2)
    print("Funcion 1 terminando")

    return 1


async def func2():
    print("Funcion 2 empezando")
    await asyncio.sleep(3)
    print("Funcion 2 terminando")

    return 2

async def func3():
    print("Funcion 3 empezando")
    await asyncio.sleep(1)
    print("Funcion 3 terminando")

    return 3

async def main():
    r = await asyncio.gather(func1(), func2(), func3())

    print(r)


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
