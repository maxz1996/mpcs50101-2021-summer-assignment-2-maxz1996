# Problem 7
# Max Zinski

# an input is valid if it's a whole, positive number
def is_valid(user_input):
    # type is not valid (int or float)
    if type(user_input) not in {type(1), type(1.0)}:
        return False

    # there is a non-zero decimal which is not valid
    if float(user_input) > int(float(user_input)):
        return False

    # hight must be non-negative
    if user_input < 0:
        return False
    
    return True

def pyramid(height):
    if not is_valid(height):
        print("pyramid() received an invalid height argument. The height argument is valid if it is a whole, positive number")
        return
    
    formatted_height = int(height)
    prev_row = ""

    i = 0
    while(i < height):
        prev_row = prev_row + "*"
        print(prev_row)
        i += 1

# tests
# pyramid(10)
# print("\n")
# pyramid(10.0)
# print("\n")
# pyramid("square")
# print("\n")
# pyramid(10.7)
# print("\n")
# pyramid(-1)