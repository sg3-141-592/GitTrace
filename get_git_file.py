from colorama import init, Fore
from git import Repo

def analyseTrace(analyse_staging):
    # Turn on terminal colours
    init()

    # Connect to git repo in current directory
    repo = Repo(".")

    # List of blobs to analyse
    blobs = []

    if analyse_staging == False:
        # Pulling data from last commit, take blobs from tree
        commit = repo.head.commit.tree
        # Can likely get rid of this for something simpler
        for item in commit.traverse():
            # Filter out tree items
            if item.type != 'tree':
                blobs.append(item)
    else:
        # Pulling data from staging area, take blobs from index
        for item in list(repo.index.iter_blobs()):
            blobs.append(item[1])

    req_files = []
    trace_files = []
    test_files = []

    # Traverse through all the data
    for item in blobs:
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

    for fileBlob in req_files:
        fileContents = fileBlob.data_stream.read().decode('ascii')
        for line in fileContents.split('\n'):
            # Check if key already exists
            if line in tags:
                print(Fore.RED + "duplicate req: " + line)
            else:
                #print(Fore.GREEN + "new req: " + line)
                # None represents no trace
                item = None
                if 'sys' in fileBlob.path:
                    item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 0}
                else:
                    item = {'traceUp': None, 'traceDown': None, 'tests': [], 'level': 1}
                tags[line] = item

    # Iterate through all of the link modules
    for fileBlob in trace_files:
        fileContents = fileBlob.data_stream.read().decode('ascii')
        # print(Fore.LIGHTBLUE_EX + "A " + file)
        for line in fileContents.split('\n'):
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
    for fileBlob in test_files:
        fileContents = fileBlob.data_stream.read().decode('ascii')
        tests[fileBlob] = {'traces': []}
        # print(Fore.LIGHTBLUE_EX + "A " + file)
        for line in fileContents.split('\n'):
            # Append the traceability
            tests[fileBlob]['traces'].append(line)
            # Apply the verification links in the other direction
            if line in tags:
                tags[line]['tests'].append(fileBlob)
            else:
                print(Fore.RED + "invalid verification trace " + line)

    # print(Fore.WHITE + "-- Summary --")
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

    return {'noUpTrace': noUpTrace,
            'noDownTrace': noDownTrace,
            'noTest': noTest,
            'tags': tags}