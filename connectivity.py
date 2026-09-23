import paramiko

class Connectivity:

    def __init__(self):
        self.connection = None
        self.is_authenticated = False


    def authenticate(self, 
                     hostname: str,
                     username: str, 
                     password: str):
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection = ssh_client.connect(hostname, username, password)
        self.is_authenticated = True

    def send_config_commands(self, commands: list[str]):
        results = []
        if not self.is_authenticated:
            self.authenticate(hostname=input('hostname: '),
                              username=input('username: '),
                              password=input('password: ')
                              )
        for line in commands:
            results.append(self.connection.send(f'{line}\n').recv(65501).decode('utf-8'))
        return results


if __name__ == "__main__":
    conn = Connectivity()
    conn.authenticate('10.10.99.1', 'script', 'cisco123')
    results = conn.send_config_commands(['configure terminal', 'interface loopback99', 'ip address 9.9.9.9 255.255.255.255'])
    print(results)
