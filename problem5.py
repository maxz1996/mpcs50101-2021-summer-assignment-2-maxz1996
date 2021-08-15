# Problem 5
# Max Zinski

# an input is valid if it's a number
def is_valid(user_input):
    allowed_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}

    # this initial check simplifies the process of verifying the rest of the input
    if len(user_input) > 1 and user_input[0] == '-':
        starting_i = 1
    else:
        starting_i = 0

    for i in range(starting_i, len(user_input)):
        # valid numbers have at most one decimal
        if user_input[i] == '.':
            allowed_chars.remove('.')
            continue
        if user_input[i] not in allowed_chars:
            return False
    
    return True

def is_divisible_by_eleven(number_input):
    # our number has non-zero decimals and therefore cannot be divisible by an integer
    if float(number_input) > int(float(number_input)):
        return False

    # at this point, our number_input (within the context of this script) is guaranteed to be a string representing an integer (could be negative)
    sum = 0
    should_add = True
    for n in number_input:
        if n != '-':
            if should_add:
                sum += int(n)
            else:
                sum -= int(n)
            # flip should_add, so we alternate correctly
            should_add = not should_add
    
    print(f"sum: {sum}")
    return sum % 11 == 0


print("Enter a number: ")
user_input = input()

while(not is_valid(user_input)):
    print("That is not a valid input. A valid input is a number.")
    print("Enter a number: ")
    user_input = input()

is_divisible = is_divisible_by_eleven(user_input)

if is_divisible: print("This is divisible by 11.")
else: print("This is not divisible by 11.")