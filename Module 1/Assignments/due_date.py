# 2. For the second part of the Assignment you will create variables of different types and print the output using a formatted string:
    # 1. Create a program called due_date.py
    # 2. Prompt the user for the day, month, year, time (minutes), time (hours), and time (seconds) this Assignment is due and store each of those 6 values in a variable. Please use the actual assignment Due Date from Canvas as your inputs.
day = input("Enter the day (DD): ")
month = input("Enter the month (MM): ")
year = input("Enter the year (YYYY): ")
hour = input("Enter the hours (HH): ")
minute = input("Enter the minutes (MM): ")
second = input("Enter the seconds (SS): ")
# 3. Use the ‘print’ statement to concatenate the variables into a string and output the due
# date of the assignment in the following format:
# a. “Module 1 Assignment is due on MM/DD/YYYY at HH:MM:SS PM EST”
    # i. Fill in MM, DD, YYYY, HH, MM, and SS using the corresponding variables
    # ii. Your output should not include the quotation marks

print(f"Module 1 Assignment is due on {month}/{day}/{year} at {hour}:{minute}:{second} PM EST")