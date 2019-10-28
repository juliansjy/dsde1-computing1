'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
the_list = [1, 2, 3, 4, 5]

def first_and_last(the_list =[1,2,3]):
    first = the_list[0]
    last = the_list[-1]
    return [first, last]

print(first_and_last(the_list))


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse():
    the_list = [1, 2, 3, 4, 5]
    beginning = the_list[0]
    end = the_list[-1]
    result = (end, beginning)
    try:
        if end > beginning:
            print("This should be the case")
        else:
            print("Please check the code again!")
    except ValueError as err:
        print("there is a ValueError!")
    return result
    #the_list, beginning, end
print(part_reverse())  # hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    the_list.insert(the_list.index(index), index)
    the_list.insert(the_list.index(index), index) 
    return the_list
    
list1 = [1, 2, 3, 4, 5]
ind1 = 2

print(repeat_at_index(list1, ind1))


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word():
    word = "hello"
    if word == word[::-1]:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
    return None

print(palindrome_word())
# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence():
    sentence = "hello olleh"
    if sentence == sentence[::-1]:
        print("this is a palindrome")
    else:
        print("this is not a palindrome")
    return 

print(palindrome_sentence())

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences():
    sentence1 = "Hi my name is Julian."
    sentence2 = " I am 21 yrs old"
    if sentence1.capitalize() and "." or "?" or "!" in sentence1:
        print(sentence1 + sentence2)
    return

print(concatenate_sentences())


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    for keyy in dictionary.keys():
        if keyy == key:
            return True
        else:
            continue
    return False

print(index_exists({"name": "cock",
"age": "sucker",
"home": "youre mums house"
},"name"))

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    for valuee in dictionary.values():
        if valuee == value:
            return True
        else:
            continue
    return False

print(value_exists({"name": "cock",
"age": "sucker",
"home": "youre mums house"
},"cock"))

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''Combines two dictionaries'''
    dict1 = dictionary1
    for key,value in dictionary2.items():
        dict1[key] = value
    return dict1

