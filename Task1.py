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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def uniqueNumbers(texts, calls):
    '''
    prints how many unique numbers are there in the 
    both lists
    '''
    records = texts + calls  # 1 step
    unique_numbers = set()  # 1 step
    for record in records:  # n steps
        unique_numbers.add(record[0])  # 1 step
        unique_numbers.add(record[1])  # 1 step
    count_unique_nos = len(unique_numbers)  # 1 step
    uniqueNosCopy = "There are " + str(count_unique_nos) + \
        " different telephone numbers in the records."  # 1 step
    return uniqueNosCopy  # 1 step


print(uniqueNumbers(texts, calls))
