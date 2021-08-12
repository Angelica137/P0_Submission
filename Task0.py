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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


def first_text(texts):
    '''
    Returns the first record of texts
    '''
    result = "First record of texts, {} texts {} at time {}".format(
        texts[0][0], texts[0][1], texts[0][2])  # O(1) + O(1) + O(n)
    return result  # O(1)


def last_call(calls):
    '''
    Print the alst record of calls
    '''
    resultCall = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
        calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3])  # O(1) + O(1) + O(n)
    return resultCall  # O(1)


'''
Answer Task0
'''

print(first_text(texts))
print(last_call(calls))
