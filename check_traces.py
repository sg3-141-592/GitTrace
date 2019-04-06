from colorama import init, Fore, Back, Style
from git import Repo
import os

# Turn on terminal colours
init()

# Connect to the local git repository
print(Fore.WHITE + "-- Getting Changes --")
repo = Repo(".")
diff_index = repo.index.diff("HEAD")
# Added files
added = []
for diff_item in diff_index.iter_change_type('A'):
    added.append(diff_item.b_blob.path)
    print(Fore.GREEN + "A " + diff_item.b_blob.path)
# Added files
deleted = []
for diff_item in diff_index.iter_change_type('D'):
    deleted.append(diff_item.b_blob.path)
    print(Fore.RED + "D " + diff_item.b_blob.path)
# Modified files
modified = []
for diff_item in diff_index.iter_change_type('M'):
    modified.append(diff_item.b_blob.path)
    print(Fore.CYAN + "M " + diff_item.b_blob.path)
# Get the changes being commited


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

print(Fore.WHITE + "-- Importing Requirements --")

# Get all the tags out of requirements files
# System Requirements are level 0
# Software Requirements are level 1
for file in files:
    f = open(file, "r")
    print(Fore.LIGHTBLUE_EX + "A " + file)
    for line in f:
        # Drop out end of line characters
        line = line.replace('\n','')
        # Try and add tags to dictionary
        if line in tags:
            print(Fore.RED + "duplicate req: " + line)
            None
        else:
            #print(Fore.GREEN + "new req: " + line)
            # None represents no trace
            item = None
            if 'sys' in file:
                item = {'traceUp': None, 'level': 0}
            else:
                item = {'traceUp': None, 'level': 1}
            tags[line] = item

print(Fore.WHITE + "-- Importing Traceability --")

# Iterate through all of the link modules
for file in trace_files:
    f = open(file, "r")
    print(Fore.LIGHTBLUE_EX + "A " + file)
    for line in f:
        # Drop out end of line characters
        line = line.replace('\n','')
        # Split the traces
        trace = line.split('>')
        # Find the high level req
        if trace[0] in tags:
            if trace[1] in tags:
                # Create the trace
                #print(Fore.LIGHTYELLOW_EX + "Tracing " + trace[0] + ":" + trace[1])
                item = tags[trace[0]]
                item['traceUp'] = trace[1]
                tags[trace[0]] = item
            else:
                break
        else:
            print(Fore.RED + "invalid trace " + trace[0] + ":" + trace[1])


print(Fore.WHITE + "-- Summary --")
# Summarise Trace Status
# BOTTOM UP
untraced = []
for tag in tags:
    if tags[tag]['level'] == 1:
        if tags[tag]['traceUp'] == None:
            untraced.append(Fore.RED + "untraced req " + tag)

print(Fore.YELLOW + "untraced - " + str(len(untraced)))

# Return codes
exit(1)