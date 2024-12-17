#!/usr/bin/env python3

"""
A program to calculate the area of a circle. The formula we use is
pi * r-squared (pi * r * r).
"""

# Now set the value of pi
PI = 3.14159

# Ask the user for a value for the radius
radius = input("What is the radius? ")

# Let's check the type of the radius value (hint: It should be a string)
print("The type of radius is: ", type(radius))

# All values we get from input() are strings, so to do math, we have to convert
# radius to a float
radius_float = float(radius)

# Let's check the type of the radius_float value (it should be a float!)
print("The type of radius_float is: ", type(radius_float))


"""
Calculate the area. The double asterisks (**) between radius_float and 2 
 tells python we want to square radius_float (raise radius_float to the power of 2)
 We put the radius_float expression inside parentheses to force python to calculate
 the square first
"""
area = PI * (radius_float**2)

# We will use print formatting to create our output to the screen
# We tell python to look for a format argument in position 0 ( {0} )
# print_area = "The area of our circle is {0}"

# Now we tell python what value we want to put in position 0 (in this case, area)
# line = print_area.format(area)
new_var_1 = "Bob"
new_var_2 = "Alice"
print(
    "The area of our circle is {0} {1} {2} {3}".format(
        area, new_var_1, new_var_2, "Hello"
    )
)

# Finally, we print to screen. And we are done!
# print(line)
