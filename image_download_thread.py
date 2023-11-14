import time
import requests
from threading import Thread


urls =  [
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623210949/download21.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211125/d11.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623211655/d31.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212213/d4.jpg',
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623212607/d5.jpg' ,
    'https://media.geeksforgeeks.org/wp-content/uploads/20190623235904/d6.jpg',
]


def descarga(url) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False
    
    with open(f"./images/{url.split('/')[-1]}", 'wb') as file:
        file.write(response.content)

    return True


if __name__ == '__main__':
    inicio = time.perf_counter()
    threads = list()

    for idx in range(len(urls)):
        print(f"Descargando {urls[idx]}")
        thread = Thread(target=descarga, args=(urls[idx],))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
        
    fin = time.perf_counter()

    print(f"Tiempo de ejecución sincrono: {fin - inicio} segundos")
