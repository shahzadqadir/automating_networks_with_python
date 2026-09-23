import yaml
import os
from netmiko import ConnectHandler
from utilities import load_device_data, get_configs_from_template


def main():
    hosts_vars = os.listdir('hosts_vars')

    with open('devices.yml') as file:
        devices = yaml.safe_load(file)

    for device in devices:
        if f"{device.get('hostname').lower()}.yml" in hosts_vars:
            data = load_device_data(hostname=device.get('hostname').lower())
            if 'ios' in device.get('platform'):
                commands = get_configs_from_template(tempalte_name='ios_vrf_configs.j2', data=data)
                connection = ConnectHandler(
                    host=device.get('ip_address'),
                    username='script',
                    password='cisco123',
                    device_type='cisco_ios'
                )
                connection.send_config_set(commands)
            elif 'xr' in device.get('platform'):
                commands = get_configs_from_template(tempalte_name='xr_vrf_configs.j2', data=data)
                connection = ConnectHandler(
                                    host=device.get('ip_address'),
                                    username='script',
                                    password='cisco123',
                                    device_type='cisco_ios'
                                )
                connection.send_config_set(commands)
            else:
                raise Exception("Platform not implemented yet.")


if __name__ == "__main__":
    main()