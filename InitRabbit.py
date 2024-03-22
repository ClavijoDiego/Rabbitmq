import subprocess

def start_rabbitmq():
    rabbitmq_command = "rabbitmq-server"
    subprocess.Popen(rabbitmq_command, shell=True)

if __name__ == "__main__":
    start_rabbitmq()
