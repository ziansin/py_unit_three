print("The program calculates surface area of rectangle prism.")

"""
The program takes the user inputs to be used in the functions for determining the side areas
The inputs are converted to floats
"""

width_input = input("Enter width: ")
width = float(width_input)
length_input = input("Enter length: ")
length = float(length_input)
height_input = input("Enter height: ")
height = float(height_input)

"""
The side function will take the first and second parameters, the first and second either being the width, length, or height, and multiplies them
The amounts are returned
"""
def side(num1, num2):
    return num1 * num2

"""
The areas for each side are also printed out, along with the total surface area
Total area is also converted to an integer
Parameters for width, length, and height
"""
def totalArea(width, length, height):
    top = side(width, length)
    print("Top =", top)
    bottom = side(width, length)
    print("Bottom =", bottom)
    right = side(height, length)
    print("Right =", right)
    left = side(height, length)
    print("Left =", left)
    front = side(height, width)
    print("Front =", front)
    back = side(height, width)
    print("Back =", back)
    total = top + bottom + right + left + front + back
    total_round = int(total)
    print("The total surface area is:", total_round)
    return total_round
def main():
    totalArea(width, length, height)
main()