import re

text_from_router = 'vrf definition POLICE'
pattern = r'vrf\s+definition\s+(?P<vrf_name>\S+)'
match = re.search(pattern, text_from_router)

if match:
    print(match.groupdict())