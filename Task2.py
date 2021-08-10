"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


def longestCall(calls):
    '''
    returns the number that had the longest call and how long the call was
    '''
    longest_call_mins = 0
    longest_call_no = ''
    for call in calls:
        minutes = int(call[3])
        if minutes > longest_call_mins:
            longest_call_mins = minutes
            longest_call_no = call[0]
    answer = str(longest_call_no) + \
        " spent the longest time, " + str(longest_call_mins) + \
        " seconds, on the phone during September 2016."
    return answer


print(longestCall(calls))
