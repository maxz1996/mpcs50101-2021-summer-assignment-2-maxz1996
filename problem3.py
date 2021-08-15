# Problem 3
# Max Zinski

def is_strong(user_input):
    if len(user_input) < 12:
        return False
    else:
        # iterate through once and verify all criteria are met
        number = False
        letter = False
        contains_special = False
        uppercase_letter = False
        lowercase_letter = False

        special = {'!', '@', '#', '$', '%'}
        numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        # using ascii codes to establish upper and lower bounds is a common pattern I've observed in algorithm problems involving strings
        # https://www.programiz.com/python-programming/examples/ascii-character
        lower_bound = ord('a')
        upper_bound = ord('z')

        for c in user_input:
            if c in special:
                contains_special = True
            elif c in numbers:
                number = True
            elif lower_bound <= ord(c.lower()) <= upper_bound:
                letter = True
                if c.lower() == c:
                    lowercase_letter = True
                else:
                    uppercase_letter = True

        return number and letter and contains_special and uppercase_letter and lowercase_letter

print("Enter a password: ")
user_input = input()

if is_strong(user_input):
    print("This is a strong password.")
else:
    print("This is not a strong password!")
    print("""Strong passwords contain:
    -at least 12 characters
    -both numbers and letters
    -at least one of these special characters: !, @, #, $, %
    -at least one capital and one lower case letter""")