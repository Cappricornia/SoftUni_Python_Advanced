# Directory Traversal

# build-in solution using os.walk() method

from os import walk

file_extensions = {}
for _, _, files, in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in file_extensions:
            file_extensions[extension] = []
            file_extensions[extension].append(file)

with open("report.txt", "w") as report:
    for ext, files in sorted(file_extensions.items()):
        report.write(f".{ext}\n")
        for file in sorted(files):
            report.write(f"---{file}\n")



