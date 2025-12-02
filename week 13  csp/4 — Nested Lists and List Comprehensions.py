list1 = [1, 2, 3]
list2 = [4, 5, 6]

nested_list = [list1, list2]

print(nested_list[0])

print(nested_list[1][1])

print(nested_list[1][0])













# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:
fruits = ["apple", "orange", "bannana", "coconut"]
vege = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vege, meats]

print(groceries[0][2])

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()




           
           





# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]

sum_list = [row[-1] for row in matrix]
print(sum_list)

squares = [x**2 for x in range(1, 11)]
print(squares)

# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

# Print the first list.

# Print the second item from the third list.

# Use a list comprehension to extract the last item from each sub-list.

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.