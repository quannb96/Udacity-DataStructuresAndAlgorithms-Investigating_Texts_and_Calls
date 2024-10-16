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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# <<< Udacity code init - end

# <<< My code - start >>>
# All area codes and mobile prefixes called in Bangalore
area_codes = set()

# Count the total calls from Bangalore and the calls from Bangalore to Bangalore
total_calls_from_bangalore = 0
calls_within_bangalore = 0

# Define variables for Bangalore area code and telemarketer prefix
bangalore_area_code = "(080)"
telemarketer_prefix = "140"
# Define a variable for mobile number prefixes
mobile_prefixes = ['7', '8', '9']

for call in calls:
    calling, receiving = call[0], call[1]

    # The call is made from Bangalore "(080)"
    if calling.startswith(bangalore_area_code):
        total_calls_from_bangalore += 1

        # Add the area code for the receiving number
        if receiving.startswith("("):  # Fixed line
            end_index = receiving.find(")")
            areaCode = receiving[1:end_index]
            area_codes.add(areaCode)
        elif " " in receiving and receiving[0] in mobile_prefixes:  # Mobile number
            area_codes.add(receiving[:4])
        elif receiving.startswith(telemarketer_prefix):  # Telemarketer
            area_codes.add(telemarketer_prefix)

        # Check if the receiving number is also from Bangalore
        if receiving.startswith(bangalore_area_code):
            calls_within_bangalore += 1

# Sort and print the area codes
sorted_area_codes = sorted(area_codes)
print("The numbers called by people in Bangalore have codes: ")
print(*sorted_area_codes, sep="\n")

# Calculate and print the percentage of calls from Bangalore to Bangalore
if total_calls_from_bangalore > 0:
    percentage = (calls_within_bangalore / total_calls_from_bangalore) * 100
else:
    percentage = 0

print(f"{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
