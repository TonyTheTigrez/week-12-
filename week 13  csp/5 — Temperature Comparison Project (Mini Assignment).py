# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

tempature = int(input("What is today's tempature?: "))

if tempature >= -10 and tempature <= 45:
    print("It is cold out!")
elif tempature > 45 and tempature < 75:
    print("It is warm out!")
elif tempature <= 75 and tempature <= 110:
    print("It is hot out!")
else:
    print("Extreme tempature warning!")
