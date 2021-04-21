from operator import itemgetter
import argparse
import re
import json
import itertools
import sys
import os


def main():
    parser = argparse.ArgumentParser(description='Process access.log')
    parser.add_argument('-f', dest='file', nargs='+', help='File(s) to analyze')
    parser.add_argument('-d', dest="directory", help='Path to directory with files')
    args = parser.parse_args()
    if args.file:
        for i in args.file:
            file_name = i.split('.')[0]
            read_file(i, output_file=f'result_{file_name}.json')
    elif args.directory:
        read_dir(args.directory)


def read_file(input_file, output_file):
    # Итоговый словарь со всеми значениями
    result = {"ALL_REQUESTS": 0,
              "POST": 0,
              "PUT": 0,
              "GET": 0,
              "DELETE": 0,
              "HEAD": 0,
              "TOP 10 IP": {},
              "TOP 10 CLIENT ERROR": [],
              "TOP 10 SERVER ERROR": [],
              "TOP 10 BYTES": []}
    # Счетчик количества запросов
    count_requests = 0
    # Список ip адресов
    ip_lst = []
    # Список с данными - ip, урлы, статусы, методы и байты
    requests_lst = []

    try:
        with open(input_file) as file:
            for line in file:
                # Поиск значений по регуляркам
                try:
                    method = re.search(r"(?i)(POST|GET|PUT|DELETE|HEAD)", line).group().upper()
                    ip_addr = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line).group(0)
                    status_code = re.search(r'\s\d{3}\s', line).group().strip()
                    url = re.search(r'(?i)(POST|GET|PUT|DELETE|HEAD)\s(.*)\s(HTTPS?|https?)', line).groups()[1]
                    bytes = re.search(r'\s(\d+|-)\s(\")', line).groups()[0].strip()
                except AttributeError:
                    sys.exit(f"Файл {input_file} не может быть обработан")
                # Увеличиваем значения счетчиков и добавляем значения в списки
                count_requests += 1
                result[method] += 1
                ip_lst.append(ip_addr)
                if bytes != "-" and ip_addr and status_code and url and method:
                    requests_lst.append([ip_addr, method, url, status_code, int(bytes)])
    except FileNotFoundError:
        sys.exit(f"Файл {input_file} не найден")
    except IsADirectoryError:
        sys.exit("Указана директория, а не файл")
    except TypeError:
        sys.exit("Не указан флаг -f и файл")

    # Создаем из списка ip отсортированный словарь из 10 ключей-значений
    ip_lst_to_dict = {data:ip_lst.count(data) for data in ip_lst}
    ip_dict_sorted = dict(sorted(ip_lst_to_dict.items(), key=lambda x: x[1], reverse=True))
    top_ip = dict(itertools.islice(ip_dict_sorted.items(), 10))
    # Создаем список из 10 словарей для клиентских ошибок
    top_client_error = [{"ip": data[0], "method": data[1], "url": data[2], "status": data[3]}
                        for data in requests_lst if data[3].startswith('4')][:10]
    # Создаем список из 10 словарей для серверных ошибок
    top_server_error = [{"ip": data[0], "method": data[1], "url": data[2], "status": data[3]}
                        for data in requests_lst if data[3].startswith('5')][:10]
    # Создаем список из 10 словарей для наибольшего количества переданных байт
    top_bytes = [{"ip": data[0], "method": data[1], "url": data[2], "bytes": data[4]}
                 for data in sorted(requests_lst, key=itemgetter(4), reverse=True)[:10]]
    # Добавляем полученные списки и словари в результирующий словарь
    result["ALL_REQUESTS"] = count_requests
    result["TOP 10 IP"] = top_ip
    result["TOP 10 CLIENT ERROR"] = top_client_error
    result["TOP 10 SERVER ERROR"] = top_server_error
    result["TOP 10 BYTES"] = top_bytes

    # Записываем результат в файл
    with open(output_file, "w") as file:
        json.dump(result, file, indent=4)


def read_dir(directory):
    try:
        os.path.isdir(directory)
    except NotADirectoryError:
        sys.exit("Указана не директория")
    files = os.listdir(directory)
    if len(files) == 0:
        sys.exit("Директория пустая")
    for i in files:
        if len(files) != 0 and i.endswith('.log'):
            file_name = i.split('.')[0]
            read_file(os.path.join(directory, i), f"result_{file_name}.json")
        elif len(files) != 0 and not i.endswith('.log'):
            print(f"{i} - не лог файл")


main()
