import json
with open('data.json', 'r') as f:
    data = json.load(f)


lst = []
for name in data['students']:
    lst.append(name['name'])
print(type(data['students']))
print(list(data['students']))
print(lst)