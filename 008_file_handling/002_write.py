# fp = open("introduction.txt", "w+")
# fp.write("Hello world!!\n")
# fp.write("I want to explore.")

# fp.seek(0)

# lines = fp.readlines()
# for line in lines:
#     print(line, end="")


with open("intoduction.txt", "w+") as fp, open("sample_file.txt", "r") as fp2:  # yo with garesi close gari rakna parena
    fp.write("Hello world!!\n")
    fp.write("I want to explore.")

    fp.seek(0)

    lines = fp.readlines()
    for line in lines:
        print(line, end="")
