# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:

# and → Both conditions must be True

# or → At least one condition must be True

# not → Inverts True/False

# You can chain comparisons: 1 < x < 5

# Examples:
x = 10
print(x > 5 and x < 15)   # True
print(x < 5 or x == 10)   # True
print(not(x == 10))       # False
print(1 < x < 20)         # True


# Practice Problems:
#Grade checker

grade = int(input("What score did you get: "))

if grade >= 90:
    print("You got an A.")
elif grade <= 89 and grade >= 80:
    print("You get a B.")
elif grade <= 79 and grade >= 70:
    print("You got a C.")
elif grade < 70 and grade > 68:
    print("You got a D.")
else:
    print("You got a F.")
# Write an expression that checks if a number is between 50 and 100 (inclusive).

# Write an expression that checks if a number is NOT equal to 0 and greater than 10.

# Use chained comparison to check if 3 < 4 < 5.

# Challenge: Create a password rule using logical operators:

