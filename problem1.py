# Problem 1
# Max Zinski

# an input is valid if it is a positive, whole number
def is_valid(user_input):
    if len(user_input) == 0:
        return False

    allowed_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for c in user_input:
        if c not in allowed_chars:
            return False
    
    return True

# https://www.almanac.com/content/temperature-conversion c = (f - 32) * 5/9
def convert_fahr_to_cels(fahr_temp):
    return (fahr_temp - 32) * 5/9

print(f"Enter a temperature in fahrenheit: ")
user_input = input()

while(not is_valid(user_input)):
    print("Please enter a positive, whole number numeric temperature: ")
    user_input = input()

f_temp = int(user_input)
c_temp = convert_fahr_to_cels(f_temp)
print(f"The temperature is {round(c_temp, 2)} in Celsius.")