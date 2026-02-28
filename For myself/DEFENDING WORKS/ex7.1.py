import json

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Convert to JSON string here:
json_data = json.dumps(car,indent=5)

print(json_data)