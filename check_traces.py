from colorama import init, Fore, Back, Style
import os

init()

# Find all of the requirements files
path = '.\\test\\'

files = []
for r, d, f in os.walk(path):
    for file in f:
        print(r)
        print(d)
        print(f)
        files.append(file)

#print(files)

# file = open("test\\req.txt","r")
# for line in file:
#     print(Fore.GREEN + line)
#     a = 1