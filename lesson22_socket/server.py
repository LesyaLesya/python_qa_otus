import socket
import json


# Хост и порт, по которому сервер будет слушать сообщения
HOST = "127.0.0.1"
PORT = 30000
# Заголовки, которые сервер вернет с ответом
RESPONSE_HEADERS = "HTTP/1.1 200 OK\r\nContent-Length: 1024\r\nConnection: close\r\nContent-Type: application/json\n\n"


# Получение заголовков запроса и их преобразование к json
def headers_parser(data):
    all_data = data.split('\r\n')
    headers = []
    headers_dict = {}
    for i in all_data:
        if ":" in i:
            headers.append(i)
    for i in headers:
        key, value = i.split(": ")
        headers_dict[key] = value
    json_obj = json.dumps(headers_dict)
    return json_obj


with socket.socket() as sock:
    # Привязка сокета к хосту и порту
    sock.bind((HOST, PORT))
    print(f"Started socket on: {HOST}:{PORT}")
    # Команда сокету на прослушивание сообщений
    sock.listen(1)
    # Бесконечный цикл, чтобы соединение не закрывалось
    while True:
        # Команда сокету принимать подключения
        conn, addr = sock.accept()
        print(f"Got connection: {conn} {addr}")
        # Получение и обработка данных
        data = conn.recv(1024).decode('utf-8')
        print(f"Got data: {data} from {addr}")
        if not data:
            conn.close()
        # Отправка ответа клиенту - заголовки запроса в виде JSON
        conn.send(f"{RESPONSE_HEADERS} {headers_parser(data)}".encode("utf-8"))
        conn.close()
