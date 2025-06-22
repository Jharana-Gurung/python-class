# Write a Python program to convert JSON data to Python object.

import json  
json_data = '{"name": "Jharana", "age": 10, "city": "Pokhara"}'

python_data = json.loads(json_data)

print("Converted to Python object:")
print(python_data)

# Write a Python program to convert Python object to JSON data.

import json  
person = {
    "name": "Soyana",
    "age": 25,
    "city": "Kathmandu"
}

json_data = json.dumps(person)

print("Converted to JSON:")
print(json_data)

# Write a Python program to convert JSON encoded data into Python objects.
import json  

json_text = '{"name": "John", "age": 30, "city": "New York"}'

python_data = json.loads(json_text)

print(python_data)

