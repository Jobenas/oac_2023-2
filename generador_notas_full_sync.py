import random
import time


def genera_practicas():
    codigo_inicial = 20230001
    contenido = ""
    cabecera = "codigo,p1,p2,p3,p4\n"
    contenido += cabecera
    for i in range(200):
        codigo = codigo_inicial + i
        p1 = random.randint(0, 20)
        p2 = random.randint(0, 20)
        p3 = random.randint(0, 20)
        p4 = random.randint(0, 20)
        linea = f"{codigo},{p1},{p2},{p3},{p4}\n"
        contenido += linea
    with open("notas_practicas.csv", "w+") as f:
        f.write(contenido)


def genera_labs():
    codigo_inicial = 20230001
    contenido = ""
    cabecera = "codigo,l1,l2,l3,l4,l5\n"
    contenido += cabecera
    for i in range(200):
        codigo = codigo_inicial + i
        l1 = random.randint(0, 20)
        l2 = random.randint(0, 20)
        l3 = random.randint(0, 20)
        l4 = random.randint(0, 20)
        l5 = random.randint(0, 20)
        linea = f"{codigo},{l1},{l2},{l3},{l4},{l5}\n"
        contenido += linea
    with open("notas_laboratorios.csv", "w+") as f:
        f.write(contenido)


def genera_parcial():
    codigo_inicial = 20230001
    contenido = ""
    cabecera = "codigo,nota\n"
    contenido += cabecera
    for i in range(200):
        codigo = codigo_inicial + i
        parcial = random.randint(0, 20)
        linea = f"{codigo},{parcial}\n"
        contenido += linea
    with open("notas_parcial.csv", "w+") as f:
        f.write(contenido)


def genera_final():
    codigo_inicial = 20230001
    contenido = ""
    cabecera = "codigo,nota\n"
    contenido += cabecera
    for i in range(200):
        codigo = codigo_inicial + i
        final = random.randint(0, 20)
        linea = f"{codigo},{final}\n"
        contenido += linea
    with open("notas_final.csv", "w+") as f:
        f.write(contenido)

    
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
