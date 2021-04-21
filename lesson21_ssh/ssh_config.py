import paramiko


client = paramiko.SSHClient()


def ssh_connect():
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname="localhost",
        username="root",
        port=4422
    )


def ssh_close():
    client.close()
