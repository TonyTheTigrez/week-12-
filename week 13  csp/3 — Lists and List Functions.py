# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.

# collections are used to store multiple items in a single variable
#list are ordered collections of itmes
# lists are mutable, meaning you cna change their content
# lists are created using square brackets []

lof = ["apple", "banana", "cherry", "date"]
print(lof) # prints list ['apple', 'banna', 'cherry', 'date']
print(type(lof)) # <class 'list'>

#accsesing items ina  list

print(lof[0]) # apple
print(lof[1]) # banna
print(lof[-1]) # date
print(lof[1:3]) # bannana, cherry
#reversign a list
lof.reverse() 
print(lof)
print(lof[::-1])

#add to list
lof.append("elderberry")
lof.append("watermelon")
lof.append("mango")
print(lof)

#add to list
lof.extend(["fig", "grape", "honeydew"])
lof.reverse()
print(lof)

#removes and returns last tiem
popped_item = lof.pop()
print(popped_item)
print(lof)

#inserting tisma t a specific index
lof.insert(1, "blueberry")
print(lof)

#removing a specific item by value
lof.remove("banana")
print(lof)
lof.insert(3, "banana")
lof.sort()
print(lof)

# imagine u have 100 items to manage

loi = list(range(1, 1001))
print(loi)
print(len(loi))

#extend list
loi.extend(range(1001, 2001))
print(len(loi))