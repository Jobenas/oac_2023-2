import random
import time


def genera_practicas():
    with open("notas_practicas.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,p1,p2,p3,p4\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            p1 = random.randint(0, 20)
            p2 = random.randint(0, 20)
            p3 = random.randint(0, 20)
            p4 = random.randint(0, 20)
            linea = f"{codigo},{p1},{p2},{p3},{p4}\n"
            f.write(linea)


def genera_labs():
    with open("notas_laboratorios.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,l1,l2,l3,l4,l5\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            l1 = random.randint(0, 20)
            l2 = random.randint(0, 20)
            l3 = random.randint(0, 20)
            l4 = random.randint(0, 20)
            l5 = random.randint(0, 20)
            linea = f"{codigo},{l1},{l2},{l3},{l4},{l5}\n"
            f.write(linea)


def genera_parcial():
    with open("notas_parcial.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,nota\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            parcial = random.randint(0, 20)
            linea = f"{codigo},{parcial}\n"
            f.write(linea)


def genera_final():
    with open("notas_final.csv", "w+") as f:
        codigo_inicial = 20230001
        cabecera = "codigo,nota\n"
        f.write(cabecera)
        for i in range(200):
            codigo = codigo_inicial + i
            final = random.randint(0, 20)
            linea = f"{codigo},{final}\n"
            f.write(linea)

    
def main():
    genera_practicas()
    genera_labs()
    genera_parcial()
    genera_final()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Tiempo de ejecución: {end - start} segundos")
