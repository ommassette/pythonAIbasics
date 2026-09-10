# this is a one liner comment

"""
This is a multi-line comment that spans
multiple lines

"""

#VARIABLES: a reference to something that has been stored somewhere in memory.

age = 25  # integer variable
       

output = age #redifining the variable output to age

age = (input("Enter your age: "))
output = age  # taking input from user and storing it in the variable age

output = type(age)  # checking the type of the variable age

#Standard output: obligated to return or give an output to the user.
print(age)  # Output: 25


"""
Types of Variable based on scope:

you cannot use a variable unless it has been defined. The scope of a variable determines where it can be accessed in the code.

1. Local Variable: A variable that is defined within a function and can only be accessed within that function.
2. Global Variable: A variable that is defined outside of any function and can be accessed from anywhere in the code.

variables can be immutable or mutable. Immutable variables cannot be changed after they are created, 
while mutable variables can be changed.
"""
