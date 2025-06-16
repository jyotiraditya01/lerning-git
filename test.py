import json

# converting JSON string to Python dictionary
with open('data.json', 'r') as f:
    data = json.load(f)

# Adding a new student to the JSON data
data['students'].append({
    "id": 3,
    "name": "Mike",
    "age": 25,
    "city": "San Francisco"
})
# 

# new_json = json.dumps(data, indent=4)
# new_json = json.loads(new_json)

print(data) 

a=10
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)
