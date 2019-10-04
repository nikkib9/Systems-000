#!/usr/bin/python3
#
# Nikki Benoit
# Aug 9 2019  11:04:35.435 MDT
#

######################################
# Calculate binary output for a user entered number
######################################
print("Decimal to Binary")
#Create variable for user given numeric entry
number =  ""

# Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert to binary? ")

# Convert entry into an integer and store as tempnumb
tempnumb = int(number)
# Create binary output string variable
bin_output = ""

# While tempnumb is not 0
while(tempnumb > 0):
    # Divide number by 2 and reassign string to prepend remainder to previous string
    bin_output = str(tempnumb % 2) + bin_output
    # New number is now old number divided by 2
    tempnumb = int(tempnumb / 2)

print(bin_output)

######################################
# Calculate octal output for a user entered number
######################################
print("Decimal to Octal")
#Create variable for user given numeric entry
number =  ""

# Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert to octal? ")

# Convert entry into an integer and store as tempnumb
tempnumb = int(number)
# Create octal output string variable
bin_output = ""

# While tempnumb is not 0
while(tempnumb > 0):
    # Divide number by 8 and reassign string to prepend remainder to previous string
    bin_output = str(tempnumb % 8) + bin_output
    # New number is now old number divided by 8
    tempnumb = int(tempnumb / 8)

print("0o" + bin_output)

######################################
# Calculate hex output for a user entered number
######################################
print("Decimal to Hex")
#Create variable for user given numeric entry
number = ""
#Hex mapping variable
hexidecimal = "123456789ABCDEF"

# Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert to hexidecimal? ")

# Convert entry into an integer and store as tempnumb
tempnumb = int(number)
# Create hexidecimal output string variable
bin_output = ""

# while(tempnumb > 0):
#     bin_output = hexidecimal[(tempnumb % 16)] + bin_output
#     tempnumb = int(tempnumb / 16)

while(tempnumb > 0):
    bin_output = hexidecimal[tempnumb % 16 - 1] + bin_output
    tempnumb = int(tempnumb / 16)

print("0x" + bin_output)

######################################
# Calculate base output for a user entered number given a user entered base
######################################
print("Decimal to User entered Base")
#Create variable for user given numeric entry
number = ""
#Hex mapping variable
values = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get number from user.  Verify entry is a number. If entry is NOT numeric, ask again.
while(not(number.isnumeric())):
    number = input("What is the decimal to convert? ")
    base = input("What base would you like to convert that to? ")

# Convert entries into integers and store in variables
tempnumb = int(number)
convertTo = int(base)

# Create base output string variable
bin_output = ""

while(tempnumb > 0):
    bin_output = hexidecimal[tempnumb % convertTo - 1] + bin_output
    tempnumb = int(tempnumb / convertTo)

print(bin_output)

######################################
# Calculate decimal from base
######################################
print("Base to Decimal")
# Request number and base to convert from
number = input("What is the number to convert? ")
base = input("What base would you like to convert that from? ")
# Convert base str to integer
baseInt = int(base)
# Convert str number by base and print
print(int(number, baseInt))
