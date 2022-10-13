print("The program calculates surface area of rectangle prism")

width_input = input("Enter width: ")
width_inp = float(width_input)
length_input = input("Enter length: ")
length_inp = float(length_input)
height_input = input("Enter height: ")
height_inp = float(height_input)

"""
Each function takes the user input and calculates the area of the specific side
The variables (---_num) area used later to calculate the total surface area
The function also prints the values when called
"""
def top(width, length):
    topp = (width * length)
    print("Top =", topp)
top_num = (width_inp * length_inp)
def bottom(width, length):
    bottomm = (width * length)
    print("Bottom =", bottomm)
bottom_num = (width_inp * length_inp)
def right_side(height, length):
    rightt = (height * length)
    print("Right =", rightt)
right_side_num = (height_inp * length_inp)
def left_side(height, length):
    leftt = (height * length)
    print("Left =", leftt)
left_side_num = (height_inp * length_inp)
def front(height, width):
    frontt = (height * width)
    print("Front =", frontt)
front_num = (height_inp * width_inp)
def back(height, width):
    backk = (height * width)
    print("Back =", backk)
back_num = (height_inp * width_inp)

total = top_num + bottom_num + right_side_num + left_side_num + front_num + back_num

"""
The main function calls all of the functions to display on the screen
"""
def main():
    top(width_inp, length_inp)
    bottom(width_inp, length_inp)
    right_side(height_inp, length_inp)
    left_side(height_inp, length_inp)
    front(height_inp, width_inp)
    back(height_inp, width_inp)
    print("The total surface area is:", total)

main()