import paramiko
from time import sleep

class Connectivity:

    def __init__(self):
        self.connection = None
        self.is_authenticated = False


    def authenticate(self, 
                     hostname: str,
                     username: str, 
                     password: str):
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(hostname=hostname, username=username, password=password)
        self.is_authenticated = True

    def send_config_commands(self, commands: list[str]):
        results = []
        if not self.is_authenticated:
            self.authenticate(hostname=input('hostname: '),
                              username=input('username: '),
                              password=input('password: ')
                              )
        remote_connection = self.connection.invoke_shell()
        for command in commands:
            remote_connection.send(command + '\n')
            sleep(1)
            results.append(remote_connection.recv(65501).decode())
        remote_connection.close()
        self.connection = None
        self.is_authenticated = False
        return results


if __name__ == "__main__":
    conn = Connectivity()
    conn.authenticate('10.10.99.1', 'script', 'cisco123')
    results = conn.send_config_commands(['configure terminal', 'interface loopback99', 'ip address 9.9.9.9 255.255.255.255'])
    if results:
        for line in results:
            print(line.strip())
        print("Configurations completed successfully.")
    
