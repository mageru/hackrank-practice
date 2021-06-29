# implement algorithm to determine if a string has
# all unique characters

def unique_chars(the_string):
    counter = {}
    for val in the_string:
        if val in counter:
            return False
        counter[val] = 1
    return True


if __name__ == '__main__':
    the_string = "This is a test"
    print(the_string+": "+str(unique_chars(the_string)))