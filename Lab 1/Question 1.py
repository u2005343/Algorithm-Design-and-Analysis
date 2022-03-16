# # Part 2: Comment Find out symbol to write comment in your program code. Anything written after the symbol,
# will not be executed. Write the symbol in your program code.

# To write a comment just add # sign at the start

# Note: Variable must start with character. (Not number or special character such as “1abc” or “@abc”. Small of
# capital letter is permitted. Cannot have special character in any place of the variable name.
# 3.1 Assign a string “Algorithm is fun” to variable x.
# 3.2 Display value of variable x.

x = "Algorithm is fun"
print(x)

# Part 4: Math
# Write python codes to calculate the following questions, then display the output on your console
# 4.1      12+15
# 4.2      15-12
# 4.3      24/6
# 4.4      9*3


print(12 + 15)
print(15 - 12)
print(24 / 6)
print(9 * 3)

# Part 5: Logical
# Write python codes to display output on your console either True or False.
# 5.1     (12 < 13)
# 5.2     (12>13)
# 5.3     (18!=17)

print(12 < 13)
print(12 > 13)
print(18 != 17)

# Part 6: Loop
# for x in range(5):
#     print(x)

# The above python code outputs:
# 0
# 1
# 2
# 3
# 4
#
# Edit the python code to:
# -	Change the increment to 4.
# -	Range of x is between 2 to 30.
# -	The output should be:
# 2
# 6
# 10
# 14
# 18
# 22
# 26

for x in range(2, 30, 4):
    print(x)

# Part 7:
# Array Note: An array is like storage container where multiple items such as numbers or strings of the same
# type are stored. Like other data structures, arrays can also be accessed using indexes. Elements stored in an array
# have a location as a numerical index. Each index starts from 0 and ends with the length of the array-1.
#
# Algorithm 7.1:
# Step 1: Declare an array called animal that has elements “cat”, “tiger”, “horse”.
# Step 2: Display the list of names.

animals: list = ["cat", "tiger", "horse"]
print(animals)

#
# Algorithm 7.2:
# Step 1: Declare an array called numbers that has elements 11, 3, 7, 5, 4
# Step 2: Sort the list using Python List sort()
# Step 3: Display the sorted list.

numbers: list = [11, 3, 7, 5, 4]
numbers.sort()
print(numbers)

# Part 8: Writing python program code for simple real-life algorithms
#
# Algorithm 8.1:
# Step 1: Prompt user to enter their name
# Step 2: Prompt user to enter their age.
# Step 3: Calculate using formula year = (2022 – age) + 100.
# Step 4: Display a message that tells them the year that they will turn 100 years old.
# Sample output if the current year is 2022:
#
# What is your name: Adam
# How old are you: 20
# Adam will be 100 years old in the year 2102
#


name = input("What is your name:")
age = input("How old are you:")
age = int(age)
year: int = (2022 - age) + 100
print(name + " will be 100 years old in the year " + year.__str__())
