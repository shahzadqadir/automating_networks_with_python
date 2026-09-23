import paramiko
import time

import credentials

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(
    hostname='10.10.99.11',
    username=credentials.cisco_username,
    password=credentials.cisco_password,
    allow_agent=False,
    look_for_keys=False,
)
conn = ssh_client.invoke_shell()
conn.send('show ip route\n')
time.sleep(1)
output = conn.recv(655011).decode().split('\n')
for line in output:
    print(line)
time.sleep(1)
conn.send('ping 10.0.0.2\n')
time.sleep(1)
output = conn.recv(655011).decode().split('\n')
for line in output:
    print(line)