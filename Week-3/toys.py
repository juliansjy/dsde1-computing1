'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''



# write a function that adds 1
# to the input and prints the result

def add(val1):
    result = val1 + 1
    return result

print(add(3))

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    return # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    result = a + b
    return result
print(sum(3, 4))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    result = sum(a + b)
    inc_return result

print(sum_inc(4, 6))



# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    return


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    # hint: you can add strings together 
    # in order to concatenate them
    return

print("hi there!")