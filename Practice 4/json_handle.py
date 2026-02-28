import json

user_data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "skills": ["Python", "Data Science"]
}

json_string = json.dumps(user_data, indent=4)
print(json_string)

parsed_data = json.loads(json_string)
print(parsed_data['name'])

with open('user.json', 'w') as f:
    json.dump(user_data, f, indent=4)

with open('sample-data.json', 'r') as f:
    data = json.load(f)
    print(data)