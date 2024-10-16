# Analysis

## Task0

Worst-case time complexity is O(1)

- The time complexity for this program is O(1) because we are accessing the first and last values from the lists (calls and texts) by an index.

## Task1

Worst-case time complexity: O(n)

- The task iterates through both texts and calls lists to collect unique telephone numbers using a set. Each list is processed once, resulting in a linear complexity of O(n), where n is the total number of records.

## Task2

Worst-case time complexity: O(n)

- The task iterates through the calls list to calculate the total call duration for each number and finds the number with the longest time. Both steps are linear, so the overall complexity is O(n).

## Task3

### Part A:
Worst-case time complexity: O(n log n)

- The task extracts area codes from the calls list, which is O(n). Sorting the area codes takes O(n log n), so the total complexity is O(n log n).

### Part B:
Worst-case time complexity: O(n)

- The task iterates through the calls list to calculate the percentage of Bangalore-to-Bangalore calls. This results in a linear complexity of O(n).

## Task4
Worst-case time complexity: O(n log n)

The task processes the calls and texts lists to collect numbers and then sorts the result. Sorting has a complexity of O(n log n), so the total complexity is O(n log n).
