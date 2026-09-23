import yaml
import jinja2
from utilities import get_configs_from_template
from connectivity import Connectivity


import os

def load_device_data(hostname):
    with open(f'hosts_vars/{hostname}.yml') as file:
        return yaml.safe_load(file)

def main():

    hosts_vars = os.listdir('hosts_vars')

    with open('devices.yml') as file:
        devices = yaml.safe_load(file)

    connection = Connectivity()

    for device in devices:
        hostname = device.get("hostname").lower()
        if hostname in [device[:-4] for device in hosts_vars]:
            data = load_device_data(hostname)
            print(f"Printing configs for {hostname}")
            if 'ios' in device.get("platform"):
                commands = get_configs_from_template('ios_vrf_configs.j2', data=data)
            elif 'xr' in device.get("platform"):
                commands = get_configs_from_template('xr_vrf_configs.j2', data=data)
            else:
                raise Exception("Software platform not supported yet.")
            connection.authenticate(hostname=device.get("ip_address"), username='script', password='cisco123')
            results = connection.send_config_commands(commands)
            if results:
                for line in results:
                    print(line)
                print(f"{hostname} configured successfully.")

if __name__ == "__main__":
    main()