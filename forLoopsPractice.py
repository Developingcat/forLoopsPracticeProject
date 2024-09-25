"""
Author: Hannah O'Shea 
Date: 9/25/2024
Program: forLoopsPractice.py

What's required: 
Input required ( Positive integer!)
Multiplication ( of atmost, by 12.)
Stable functioning purpose!  

"""
# Opening of the program! 

print("Welcome!")
print("Please Input a positive integer to begin")



lower = int(input("Please enter a positive integer!"))
upper = int(12)

theSum = 0

for number in range(upper, lower + 1 ):
    theSum*= number
