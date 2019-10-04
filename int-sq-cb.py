#!/usr/bin/python3
#
# Nikki Benoit
# Aug 8 2019  16:24:31.2431 MDT
#
######################################
# Exploring While loops - loops through integer, it's square, and it's cube
# 9 times while increasing the integer by 1 each time. - Sorts output into named columns
######################################

# Starting integer
integer = 0
# Column names for print formatting
colNameI = "I"
colNameS = "S"
colNameC = "C"

# Cycle through 9 times
while (integer < 10):
    square = integer ** 2   #Get Square of integer
    cube = integer ** 3     #Get Cube of integer

    #print columns center justified w/in 3 spaces
    print(colNameI.center(3), colNameS.center(3), colNameC.center(3))
    #print integer, square, and cube center justified w/in 3 spaces
    print("{:^3d}".format(integer), "{:^3d}".format(square), "{:^3d}".format(cube), "\n")

    integer += 1            #increase integer

# If we left out the integer += 1, we'd get the same print out 9 times
