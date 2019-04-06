from colorama import init, Fore, Back, Style
import check_traces
import get_git_file

# Turn on terminal colours
init()

print(Fore.WHITE + str(get_git_file.analyseTrace(False)))
#print(get_git_file.analyseTrace(True))

# # Turn on terminal colours
# init()

# before_path = ".\\test_before\\"
# after_path = ".\\test_after\\"

# before_trace = check_traces.get_traceability(before_path)

# after_trace = check_traces.get_traceability(after_path)

# print(Fore.WHITE + "-- Summary --")
# print(Fore.WHITE + "-- Missing Up Trace   - " + str(len(after_trace['noUpTrace'])))
# print(Fore.WHITE + "-- Missing Down Trace - " + str(len(after_trace['noDownTrace'])))
# print(Fore.WHITE + "-- Missing Test       - " + str(len(after_trace['noTest'])))

# # Display new tags
# # Find number added
# def report_trace(key):
#     print(Fore.WHITE + "-- " + key)
#     added = set(after_trace[key]) - set(before_trace[key])
#     removed = set(before_trace[key]) - set(after_trace[key])
#     if len(added) > 0:
#         print(Fore.GREEN + "A " + str(added))
#     if len(removed) > 0:
#         print(Fore.RED + "D " + str(removed))

# print(Fore.WHITE + "-- Changes --")
# report_trace('tags')
# report_trace('noUpTrace')
# report_trace('noDownTrace')
# report_trace('noTest')