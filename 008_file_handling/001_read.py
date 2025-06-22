fp = open(r"C:\Users\grgay\OneDrive\Desktop\python-class\008_file_handling\sample_file.txt", "r")
content = fp.read()
print(content)

fp.seek(26)

Another_content = fp.read()
print(Another_content)
