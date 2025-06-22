import json

content = '{"name":  "Arjun", "age": 10, "country": " Nepal"}'
content_dict = json.loads(content)
content_key_with_values = content_dict.items()
for key, value in content_key_with_values:
    print(key, value)
