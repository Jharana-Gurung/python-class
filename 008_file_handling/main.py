import json

file_path = (r"C:\Users\grgay\OneDrive\Desktop\python-class\.vscode\extensions.json")
with open(file_path, "r") as fp:

    text_content = fp.read()
    content_dictionary = json.loads(text_content)
    print(content_dictionary["recommendations"][0])