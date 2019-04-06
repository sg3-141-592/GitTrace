from colorama import init, Fore, Back, Style
import get_git_file

# Turn on terminal colours
init()

# Analyse the traceability
before_trace = get_git_file.analyseTrace(analyse_staging=False)
after_trace = get_git_file.analyseTrace(analyse_staging=True)

# Display new tags
# Find number added
def report_trace(key):
    # Calculate differences
    added = set(after_trace[key]) - set(before_trace[key])
    removed = set(before_trace[key]) - set(after_trace[key])
    # Check if there are any changes
    if len(added) > 0 or len(removed) > 0:
        print(Fore.WHITE + "-- " + key)
        if len(added) > 0:
            print(Fore.RED + "New untraced: " + str(added))
        if len(removed) > 0:
            print(Fore.GREEN + "Fixed trace: " + str(removed))

print(Fore.WHITE + "-- Analysing Traceability --")
print(Fore.WHITE + "-- Summary")
print("No Up Trace: " + str(len(after_trace['noUpTrace'])))
print(after_trace['noUpTrace'])
print("No Down Trace: " + str(len(after_trace['noDownTrace'])))
print(after_trace['noDownTrace'])
print("No Test: " + str(len(after_trace['noTest'])))
print(after_trace['noTest'])
print(Fore.WHITE + "-- Differences")
report_trace('noUpTrace')
report_trace('noDownTrace')
report_trace('noTest')