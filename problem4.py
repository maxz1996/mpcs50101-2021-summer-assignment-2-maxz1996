# Problem 4
# Max Zinski

# only find the max if all arguments are numbers (int or float). Although we could allow other number types like decimal, the objective of this
# exercise seems to be focused on finding the max of numbers, not converting/comparing different number types.
def max_of_three(a,b,c):
    types = {type(1), type(1.0)}
    if type(a) not in types or type(b) not in types or type(c) not in types:
        print("Cannot compare numbers because at least one is not a valid type (int or float are valid types). Returning False")
        return False
    
    nums = [a, b, c]
    # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints the initial max value should be the smallest allowed number in python
    max = float('-inf')
    for n in nums:
        if n > max:
            max = n
    
    return float(max)

# tests
# print(max_of_three("a",2.0,3))
# print(max_of_three(3,2,1))
# print(max_of_three(-1000,2.0,1))