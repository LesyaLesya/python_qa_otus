from lesson21_ssh.ssh_config import ssh_connect, ssh_close, client
import subprocess


def test_1_restart_service():
    # Коннектимся по ssh к контейнеру
    ssh_connect()
    # Выполняем команду на рестарт сервиса
    stdin, stdout, stderr = client.exec_command('/etc/init.d/rsyslog restart')
    output = stdout.read() + stderr.read()

    if "Starting enhanced syslogd" in output.decode():
        print('Service rsyslog was successfully restarted')
        assert True
    else:
        assert False, "Service was not restarted"
    ssh_close()


def test_2_restart_container():
    # Получаем id контейнера по его имени
    get_container_id = "docker ps -aqf 'name=21_opencart_1'"
    exec_command_get_id = subprocess.Popen \
        (get_container_id, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    container_id = (exec_command_get_id.communicate()[0]).decode()
    print("ID of container: ", container_id)

    # Получаем время запуска контейнера до рестарта
    get_time_before_restart = "docker inspect --format='{{.State.StartedAt}}' " + container_id
    exec_command_get_time_1 = subprocess.Popen \
        (get_time_before_restart, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time_before_restart = (exec_command_get_time_1.communicate()[0]).decode()
    print("Time before restart: ", time_before_restart)

    # Перезапускаем контейнер
    restart_container = f"docker restart {container_id}"
    exec_rcommand_restart = subprocess.Popen\
        (restart_container, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    restart_result = exec_rcommand_restart.communicate()[0]
    print("Restart: ", restart_result.decode())

    # Получаем время запуска контейнера после рестарта
    get_time_after_restart = "docker inspect --format='{{.State.StartedAt}}' " + container_id
    exec_command_get_time_2 = subprocess.Popen \
        (get_time_after_restart, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time_after_restart = (exec_command_get_time_2.communicate()[0]).decode()
    print("Time after restart: ", time_after_restart)

    if time_after_restart != time_before_restart:
        print("Container was successfully restarted")
        assert True
    else:
        assert False, "Container was not successfully restarted"
