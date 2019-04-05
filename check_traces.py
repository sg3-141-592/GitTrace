from colorama import init, Fore, Back, Style
import os

init()

# Find all of the requirements files
path = '.\\test\\'

files = []
trace_files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
        elif '.trace' in file:
            trace_files.append(os.path.join(r, file))

tags = dict()

# Get all the tags out of requirements files
for file in files:
    f = open(file, "r")
    print(Fore.LIGHTBLUE_EX + file)
    for line in f:
        # Drop out end of line characters
        line = line.replace('\n','')
        # Try and add tags to dictionary
        if line in tags:
            print(Fore.RED + "duplicate req: " + line)
        else:
            print(Fore.GREEN + "new req: " + line)
            # None represents no trace
            tags[line] = None

# Iterate through all of the link modules
for file in trace_files:
    f = open(file, "r")
    print(Fore.LIGHTBLUE_EX + file)
    for line in f:
        # Drop out end of line characters
        line = line.replace('\n','')
        # Split the traces
        trace = line.split('>')
        # Find the high level req
        if trace[0] in tags:
            if trace[1] in tags:
                # Create the trace
                print(Fore.LIGHTYELLOW_EX + "Tracing " + trace[0] + ":" + trace[1])
                tags[trace[0]] = trace[1]
            else:
                break
        else:
            print(Fore.RED + "Invalid trace " + trace[0] + ":" + trace[1])

# file = open("test\\req.txt","r")
# for line in file:
#     print(Fore.GREEN + line)
#     a = 1