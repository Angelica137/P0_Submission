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


def longest_call(calls):
    '''
    returns the number that spent the longest time on the phone this period
    '''
    telephone_nos = dict()  # O(1)
    for i in range(len(calls)):  # O(n)
        telephone_nos[calls[i][0]] = telephone_nos.get(
            calls[i][0], 0) + int(calls[i][-1])  # O(1)
        telephone_nos[calls[i][1]] = telephone_nos.get(
            calls[i][1], 0) + int(calls[i][-1])  # O(1)
    max_telephone_num = max(
        telephone_nos, key=lambda x: telephone_nos.get(x))  # O(n)
    max_duration = telephone_nos.get(max_telephone_num)  # O(1)
    return max_telephone_num, max_duration  # O(1)


task2_result = longest_call(calls)
answer_task2 = "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    task2_result[0], task2_result[1])
print(answer_task2)
