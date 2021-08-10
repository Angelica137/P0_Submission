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
    call_times = {}
    for call in calls:
        if call[0] not in call_times:  # O(n)
            call_times[call[0]] = int(call[3])  # 1 step + O(n)
        else:
            call_times[call[0]] += int(call[3])  # 1 step + O(n)
    max_time = max(call_times.values())  # O(n)
    number = [k for k, v in call_times.items() if v == max_time][0]  # O(n) + 1
    copy = "{} spent the longest time, {} seconds, on the phone during September 2016."  # 1 step
    answer_task2 = copy.format(number, max_time)  # 1 + step
    return answer_task2  # 1 step


print(longestCall(calls))
