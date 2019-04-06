from colorama import init, Fore, Back, Style
import check_traces

# Turn on terminal colours
init()

before_path = ".\\test_before\\"
after_path = ".\\test_after\\"

before_trace = check_traces.get_traceability(before_path)

after_trace = check_traces.get_traceability(after_path)

# Display new tags
# Find number added
print(Fore.WHITE + "-- Tags Change --")
added = set(after_trace['tags']) - set(before_trace['tags'])
removed = set(before_trace['tags']) - set(after_trace['tags'])
print(Fore.GREEN + "A " + str(added))
print(Fore.RED + "D " + str(removed))

# Display changes to missing upwards tags
print(Fore.WHITE + "-- Upwards Traces Change --")
added = set(after_trace['noUpTrace']) - set(before_trace['noUpTrace'])
removed = set(before_trace['noUpTrace']) - set(after_trace['noUpTrace'])
print(Fore.GREEN + "A " + str(added))
print(Fore.RED + "D " + str(removed))

# Display changes to missing downwards tags
print(Fore.WHITE + "-- Downwards Traces Change --")
added = set(after_trace['noDownTrace']) - set(before_trace['noDownTrace'])
removed = set(before_trace['noDownTrace']) - set(after_trace['noDownTrace'])
print(Fore.GREEN + "A " + str(added))
print(Fore.RED + "D " + str(removed))