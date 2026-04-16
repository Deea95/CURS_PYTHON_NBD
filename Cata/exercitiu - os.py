import os
print(os.getcwd())

file_path = os.path.join(os.path.dirname(__file__), "log.txt")

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        if "INFO" in line:
            print(line.strip())