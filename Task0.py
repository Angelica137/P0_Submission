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


def firstText(texts):
    '''
    Returns the first record of texts
    '''
    incoming = texts[0][0]
    answering = texts[0][1]
    time = texts[0][2]
    result = "First record of texts, " + incoming + \
        " texts " + answering + " at time " + time
    return result


def lastCall(calls):
    '''
    Print the alst record of calls
    '''
    incomingNo = calls[-1][0]
    receiving = calls[-1][1]
    time = calls[-1][2]
    duration = calls[-1][3]
    resultCall = "Last record of calls, " + incomingNo + " calls " + \
        receiving + " at time " + time + ", lasting " + duration + " seconds"
    return resultCall


print(firstText(texts))
print(lastCall(calls))
