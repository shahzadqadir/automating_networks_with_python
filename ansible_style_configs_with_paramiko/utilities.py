import jinja2
import yaml

def get_configs_from_template(tempalte_name: str, 
                               template_directory: str='./templates',
                               data: str='data'):
    templateLoader = jinja2.FileSystemLoader(template_directory)
    templateEnv = jinja2.Environment(loader=templateLoader)
    output = templateEnv.get_template(tempalte_name).render(data=data)
    return [line.strip() for line in output.split('\n') if line]


def load_device_data(hostname):
    with open(f'hosts_vars/{hostname}.yml') as file:
        return yaml.safe_load(file)