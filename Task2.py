"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# <<< Udacity code init - end

# <<< My code - start >>>

# Time for each phone number
telephones = {}

# Initialize variables to the telephone longest time
tel_longest_time = None
total_longest_time = 0

# Loop through all the calls
for call in calls:
    calling = call[0]
    receiving = call[1]
    time = int(call[3])

    # Add the call time to the calling telephone
    telephones[calling] = telephones.get(calling, 0) + time
    # Update the telephone with the longest calling time
    if telephones[calling] > total_longest_time:
        tel_longest_time = calling
        total_longest_time = telephones[calling]

    # Add the call time to the receiving telephone
    telephones[receiving] = telephones.get(receiving, 0) + time
    # Update the telephone with the longest call time
    if telephones[receiving] > total_longest_time:
        tel_longest_time = receiving
        total_longest_time = telephones[receiving]

# Print the result
print(f"{tel_longest_time} spent the longest time, {total_longest_time} seconds, on the phone during September 2016.")
# <<< my code - end
