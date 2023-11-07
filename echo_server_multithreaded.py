import socket
from threading import Thread

SOCK_BUFFER = 1024

num_clientes = 0

def client_handler(conn, client_address):
    global num_clientes
    print(f"Cliente conectado desde {client_address[0]}:{client_address[1]}")
    num_clientes += 1
    print(f"Numero de clientes conectados: {num_clientes}")

    try:
        while True:
            data = conn.recv(SOCK_BUFFER)

            if data:
                print(f"recibi {data}")
                conn.sendall(data)
            else:
                print(f"no hay mas datos de {client_address[0]}:{client_address[1]}")
                break
    except ConnectionResetError:
        print(f"Cliente {client_address[0]}:{client_address[1]} desconectado abruptamente")
    finally:
        conn.close()
        print(f"Conexion con {client_address[0]}:{client_address[1]} cerrada")
        num_clientes -= 1


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    print("Empezando a escuchar clientes...")
    sock.listen(1)

    while True:
        connection, c_address = sock.accept()

        t = Thread(target=client_handler, args=(connection, c_address))
        t.start()
