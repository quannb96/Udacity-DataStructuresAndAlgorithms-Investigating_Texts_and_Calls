"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

# Udacity code init - start >>>
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
# <<< Udacity code init - end

# <<< My code - start >>>
first_record_of_text = texts[0]
last_record_of_call = calls[-1]
print("First record of texts, {} texts {} at time {}".format(first_record_of_text[0], first_record_of_text[1], first_record_of_text[2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_record_of_call[0], last_record_of_call[1], last_record_of_call[2], last_record_of_call[3]))
# <<< my code - end