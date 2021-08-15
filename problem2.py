# Problem 2
# Max Zinski

# an input is valid if it is a whole number between 0 and 100, inclusive
def is_valid(user_input):
    allowed_chars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
    for c in user_input:
        if c not in allowed_chars:
            return False

    number = int(user_input)
    if number < 0 or number > 100:
        return False
    
    return True

def convert_score_to_grade(score):
    if score >= 90:
        return ['A', '$)']
    elif score >= 80:
        return ['B', ':)']
    elif score >= 70:
        return ['C', ':/']
    elif score >= 60:
        return ['D', ":'("]
    else:
        return ['F', 'x(']

print(f"Enter a score: ")
user_input = input()

while(not is_valid(user_input)):
    print("That is not a valid input. Please enter a whole number between 0 and 100 inclusive.")
    user_input = input()

grade = convert_score_to_grade(int(user_input))

if grade[0] in {'A', 'E', 'F'}:
    prep = 'an'
else:
    prep = 'a'

print(f"You received {prep} {grade[0]} {grade[1]}")