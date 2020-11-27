# Short Hand If
# If you have only one statement to execute, you can put it on the same
#  line as the if statement.
a = 5
b = 2
if a > b: print('a is greater than b')

# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else
# , you can put it all on the same line:

a = 330
b = 330

print('A') if a > b else print('B')

# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:

print('A') if a > b else print('=') if a == b else print('B')
