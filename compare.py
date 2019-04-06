from colorama import init, Fore, Back, Style
import check_traces

# Turn on terminal colours
init()

before_path = ".\\test_before\\"
after_path = ".\\test_after\\"

before_trace = check_traces.get_traceability(before_path)

after_trace = check_traces.get_traceability(after_path)

# Compare up trace
# Find number added
added = set(after_trace['noUpTrace']) - set(before_trace['noUpTrace'])
removed = set(before_trace['noUpTrace']) - set(after_trace['noUpTrace'])
print(Fore.GREEN + "A " + str(added))
print(Fore.RED + "D " + str(removed))