"""
Author: Hannah O'Shea 
Date: 9/27/2024
Program: basicMultiplicationTable.py

What's required: 
Input required ( Positive integer!)
Multiplication ( of atmost, by 12.)
Stable functioning purpose!  

1. Ask user for a number (1-12)
2. Print out the name of that multiplication table: 
    "Multiplication Table for <number>:" 
3. for loop print out all the multiplication facts (1-12) for the users number 
Multi-Advance-Table, now with built-in custom range and multi-table options 

1. Ask the user if they want to generate multiple tables 
2. Create a function to do steps 2 & 3 above (3 variables: number, start=1, end=12)
3. Create a control structure to handle the user answer from step 1
    What to do if yes 
    What to do if no 

"""
# Create the code 

print("Hello! Hi! Welcome! Please input a number of 1-12 below to get started with the table!") 

print("Please enter in the number between 1-12!")

numOne = int(input("The number you'd like the multiples of: "))

product = (1,12) 
# Idea to try: Change the product value each time? Possibly? Try setting it in a range? 


for count in range (numOne, 1, 12): 
    # Somewhere here is where it goes wrong 
    product = (1, 12) * numOne 
print (product) 
# Something something to do with product, try something like the income calcuator? Maybe just a formula will help? 