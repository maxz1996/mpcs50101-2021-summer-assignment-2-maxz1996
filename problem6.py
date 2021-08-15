# Problem 6
# Max Zinski

# a valid word or phrase contains only spaces and valid english letters
def is_valid(user_input):
    # remove spaces
    formatted_input = user_input.replace(" ", "") # https://www.journaldev.com/23763/python-remove-spaces-from-string#:~:text=Python%20String%20strip()%20function%20will%20remove%20leading%20and%20trailing%20whitespaces.&text=If%20you%20want%20to%20remove,or%20rstrip()%20function%20instead.
    
    lower_bound = ord('a')
    upper_bound = ord('z')

    for c in formatted_input:
        # character is not one of the 26 English characters
        if ord(c.lower()) < lower_bound or ord(c.lower()) > upper_bound:
            return False

    return True

# some of this code is redundant since is_valid implements some of it, but splitting up validation and formatting makes the code more modular imo
def format_input(user_input):
    formatted_input = user_input.replace(" ", "")
    return formatted_input.lower()
    
# a palindrome is a word or phrase that READS the same forwards and backwards. Allow upper and lowercase mismatches when evaluating if
# a string is a palindrome. For example, Racecar is a palindrome.
# palindrome detection lends itself very well to stacks
def is_a_palindrome(formatted_input):
    # create two iterators, one starting from the front of the string and one starting from the back.
    # at each step, compare the two characters at each iterator 
    front_i = 0
    back_i = len(formatted_input) - 1
    s = formatted_input
    while(front_i < back_i):
        front_l = s[front_i]
        back_l = s[back_i]
        if front_l != back_l:
            return False
        front_i += 1
        back_i -= 1
    
    return True


print("Enter a word or phrase: ")
user_input = input()

while(not is_valid(user_input)):
    print("That is not a valid input. A valid input is a word or phrase where each character is one of the 26 English letters or a space")
    print("Enter a word or phrase: ")
    user_input = input()

formatted_input = format_input(user_input)
is_palindrome = is_a_palindrome(formatted_input)
if is_palindrome: print("This is a palindrome.")
else: print("This is not a palindrome.")