# Tags must be unique
req_tags = dict()
req_tags['REQA'] = ['1.0','0.2','0.1']
req_tags['REQA'] = ['1.0','0.2']
req_tags['REQC'] = ['1.0']

#
def findTrace(tag, gitID):
    if tag in req_tags:
        # Try and find the commit
        if gitID in req_tags[tag]:
            return True
    return False

# TEST.TXT
# TRACES REQA:0.2
# TRACES REQB:0.2
# TRACES REQC:0.2
test_procedure = dict()
test_procedure['']

# RESULTS.TXT
# TEST.TXT:VERI1 <- Results are from a particular baseline


print(findTrace('REQA','1.1'))