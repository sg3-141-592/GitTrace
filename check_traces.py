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


# Find all of the requirements files
path = '.\\test_after\\'

req_files = []
trace_files = []
test_files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            req_files.append(os.path.join(r, file))
        elif '.trace' in file:
            trace_files.append(os.path.join(r, file))
        elif '.tst' in file:
            test_files.append(os.path.join(r, file))

tags = dict()

print(Fore.WHITE + "-- Importing Requirements --")

# Get all the tags out of requirements files
# System Requirements are level 0
# Software Requirements are level 1
for file in req_files:
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
                item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 0}
            else:
                item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 1}
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
                # Link the other way
                item = tags[trace[1]]
                item['traceDown'] = trace[0]
            else:
                print(Fore.RED + "invalid trace " + trace[0] + ":" + trace[1])
        else:
            print(Fore.RED + "invalid trace " + trace[0] + ":" + trace[1])

tests = dict()

# Get all of the tests
for file in test_files:
    f = open(file, "r")
    tests[file] = {'traces': []}
    print(Fore.LIGHTBLUE_EX + "A " + file)
    for line in f:
        # Drop out end of line characters
        line = line.replace('\n','')
        # Append the traceability
        tests[file]['traces'].append(line)
        # Apply the verification links in the other direction
        if line in tags:
            tags[line]['tests'].append(file)
        else:
            print(Fore.RED + "invalid verification trace " + line)

print(Fore.WHITE + "-- Summary --")
# Summarise Trace Status
# BOTTOM UP
noUpTrace = []
for tag in tags:
    if tags[tag]['level'] == 1:
        if tags[tag]['traceUp'] == None:
            noUpTrace.append(tag)
# TOP DOWN
noDownTrace = []
for tag in tags:
    if tags[tag]['level'] == 0:
        if tags[tag]['traceDown'] == None:
            noDownTrace.append(tag)
# UNTESTED REQUIREMENTS
noTest = []
for tag in tags:
    if len(tags[tag]['tests']) == 0:
        noTest.append(tag)

print(Fore.YELLOW + "| missing upward traces\t\t| " + str(len(noUpTrace)) + "\t|")
print(Fore.YELLOW + "| missing downwards traces\t| " + str(len(noDownTrace)) + "\t|")
print(Fore.YELLOW + "| untested requirement\t\t| " + str(len(noTest)) + "\t|")

# Return codes
exit(1)