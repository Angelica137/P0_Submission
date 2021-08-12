"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def find_telemarketers(calls, texts):
    '''
    returns the numbers that do not send or
    receive texts
    '''
    outgoing_calls = set()  # O(1)
    incoming_calls_texts = set()  # O(1)
    for call in calls:  # O(n)
        outgoing_calls.add(call[0])  # O(1)
        incoming_calls_texts.add(call[1])  # O(1)
    for text in texts:  # O(n)
        incoming_calls_texts.add(text[0])  # O(1)
        incoming_calls_texts.add(text[1])  # O(1)
    telemarketers = outgoing_calls - incoming_calls_texts  # O(n)
    result = sorted(telemarketers)  # O(n log n)
    return result  # O(1)


'''
Answer
'''

pt = find_telemarketers(calls, texts)
copy = "These numbers could be telemarketers: "
print(copy)
for elem in pt:
    print(elem)
