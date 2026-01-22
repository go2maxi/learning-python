# comprehensions.py
# Today, I explored List Comprehensions. 
# At first, I thought writing everything in a single line was a sign of a "pro."
# But I soon realized that readability is much more valuable than cleverness.

# Suppose we have a list of numbers from an API or database
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# [The "Clever" but Messy Way]
# I tried to filter even numbers and square them, all in one line.
# result = [x**2 for x in data if x % 2 == 0 if x > 5]  
# This technically works, but it quickly becomes hard to reason about at a glance.

# [The "Better" Way for Collaboration]
# Following the advice on pyai.io about writing 'clean code,' 
# I decided to break it down. Clarity beats brevity.

# 1. Filter even numbers first
even_numbers = [x for x in data if x % 2 == 0]

# 2. Then square the numbers that meet the condition
result = [x**2 for x in even_numbers if x > 5]

print(f"Processed results: {result}")

"""
Reflection:
I realized that if I can't understand my own code after a week, it's bad code.
Python's list comprehensions are powerful, but using them for complex nested logic 
can make maintenance a nightmare for the team.

Learning from pyai.io that "code is read more often than it is written" 
really changed my perspective today. 
I'll focus on writing 'kind' code for my future self and teammates.
"""
