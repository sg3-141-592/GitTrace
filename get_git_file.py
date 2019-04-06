from colorama import init, Fore
from git import Repo

# Turn on terminal colours
init()

# Connect to git repo
repo = Repo(".")
tree = repo.head.commit.tree # Current commit, not staging!

for (path, stage), entry in repo.index.entries.items():
    print(path)
    print(stage)
    print(entry)

req_files = []
trace_files = []
test_files = []

# Traverse through all the data
for item in tree.traverse():
    # Filter out the tree items
    if item.type != 'tree':
        if '.txt' in item.name:
            req_files.append(item)
        if '.trace' in item.name:
            trace_files.append(item)
        if '.tst' in item.name:
            test_files.append(item)

# Get all the tags out of requirements files
# System Requirements are level 0
# Software Requirements are level 1
tags = dict()

# for fileBlob in req_files:
#     fileContents = fileBlob.data_stream.read().decode('ascii')
#     for line in fileContents.split('\n'):
#         # Check if key already exists
#         if line in tags:
#             print(Fore.RED + "duplicate req: " + line)
#         else:
#             #print(Fore.GREEN + "new req: " + line)
#             # None represents no trace
#             item = None
#             if 'sys' in fileBlob.path:
#                 item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 0}
#             else:
#                 item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 1}
#             tags[line] = item
