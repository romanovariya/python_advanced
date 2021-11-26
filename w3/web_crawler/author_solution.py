import json


in_filename = input()
with open(in_filename, 'r') as f:
    web_index = json.load(f)

web_pages = []
stack = [
    (site_domain, section)
    for site_domain, section in web_index.items()
]

while stack:
    site_domain, section = stack.pop()
    if section:
        for a, b in section.items():
            stack.append((f'{site_domain}/{a}', b))
    else:
        web_pages.append(site_domain)

print(*sorted(web_pages), sep='\n')