import napalm
import json

def main():
    driver = napalm.get_network_driver("iosxr")

    device = driver(hostname='10.10.99.6', username='script', password='cisco123')
    device.open()

    device.load_merge_candidate(filename='acl.cfg')

    difference = device.compare_config()

    if len(difference) > 0:
        print("Configuration changes detected.")
        print(difference)
        device.commit_config()
    else:
        print("No changes detected")
        device.discard_config()

    device.close()


if __name__ == "__main__":
    main()