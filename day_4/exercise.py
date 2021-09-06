# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def subtract(num1, num2):
    return num1 - num2

#     - A function that multiplies three integers
def multiply(num1, num2):
    return num1 * num2

#     - A function that adds four integers
def addition(num1, num2):
    return num1 + num2

def division(num1, num2):
    return num1 / num2

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.
# 
# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.

# Ask for how many people in party
partyNo = float(input("How many people are in the party? "))

# Ask for bill amount
billAmt = float(input("What is the bill amount? "))

# Ask for tip type; fixed percentage or variable amount
tipType = input("Would you like to tip 15%? (y/n) ")
if tipType == "y":
    tipRate = 0.15
    tipAmt = multiply(billAmt, tipRate)
elif tipType == "n": # Ask for tip variable amount if fixed percentage is declined
    tipAmt = float(input("Enter the dollar ($) amount you would like to tip: "))
else:
    tipRate = 0.20
    print("You can't follow instructions so I'm charging you 20%.")
    tipAmt = multiply(billAmt, tipRate)

# Assign global variable called tax_rate
def global_key():
    global taxRate
    taxRate = 0.095

# Create function that calculates taxes
global_key()
taxAmt = multiply(billAmt, taxRate)
print("The taxes are: $" + str(taxAmt))

# Create function that calculates total with taxes
totalAmt = addition(billAmt, taxAmt)
print("The subtotal with taxes is: $" + str(totalAmt))

# Create function that calculates tip
print("The tip is: $" + str(tipAmt))

# Create function that calculates total with tip
totalAmt = addition(totalAmt, tipAmt)
print("The final total with taxes and tip is: $" + str(totalAmt))

# Create function that splits bill based on total
splitAmt = division(totalAmt, partyNo)
print("The split total for each member of your party is: $" + str(splitAmt))