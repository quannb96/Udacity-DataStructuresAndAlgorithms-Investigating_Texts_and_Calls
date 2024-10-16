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
# <<< Udacity code init - end

# <<< My code - start >>>
# Get all phone numbers that made outgoing calls
outgoing_calls = set()
for call in calls:
    outgoing_calls.add(call[0])

# Get all phone numbers that send texts, receive texts or receive incoming calls
send_or_receive_calls = set()
# Add all numbers that received calls
for call in calls:
    send_or_receive_calls.add(call[1])  # Receiving number

# Add all numbers that sent texts and received texts
for text in texts:
    send_or_receive_calls.add(text[0])  # Sending number
    send_or_receive_calls.add(text[1])  # Receiving number
        
# Numbers that make outgoing calls but never send texts, receive texts or receive incoming calls
telemarketers = outgoing_calls - send_or_receive_calls
sorted_telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers:")
for number in sorted_telemarketers:
    print(number)
