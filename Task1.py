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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# <<< Udacity code init - end

# <<< My code - start >>>
unique_telephone_numbers = set()

# telephone numbers from texts
for text in texts:
    unique_telephone_numbers.add(text[0])
    unique_telephone_numbers.add(text[1])

# telephone number from calls
for call in calls:
    unique_telephone_numbers.add(call[0])
    unique_telephone_numbers.add(call[1])

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")
# <<< my code - end