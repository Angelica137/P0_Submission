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


def notInTexts(calls, texts):
    '''
    returns the numbers that do not send or
    receive texts
    '''
    no_texts = []
    for call in calls:
        if call[0] not in no_texts:
            not_in_texts = True
            for text in texts:
                if call[0] in text:
                    not_in_texts = False
            if not_in_texts == True:
                no_texts.append(call[0])
    return no_texts


def noIncomingCalls(numbers, calls):
    '''
    returns the numbers that do not receive any calls
    '''
    no_incoming_calls = []
    for number in numbers:
        incoming_calls = False
        for i in range(len(calls)):
            if number == calls[i][1]:
                incoming_calls = True
                i += 1
        if incoming_calls == False and number not in no_incoming_calls:
            no_incoming_calls.append(number)
    return no_incoming_calls


def findTelemarketers(calls, texts):
    no_texts = notInTexts(calls, texts)  # O(n^2)
    telemarketers = noIncomingCalls(no_texts, calls)  # O(n^2)
    ordered_numbers = sorted(telemarketers)  # O(nlogn)
    return ordered_numbers


'''
Answer
'''
possible_telemarketers = findTelemarketers(calls, texts)
copy = "These numbers could be telemarketers: "
print(copy)
for elem in possible_telemarketers:
    print(elem)
