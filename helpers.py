import string

def alphabet_position(letter):
    """ takes a letter a-z or A-Z and returns the
    coresponding position in the alphabet 0-25 """
    if letter in string.ascii_lowercase:
        position = (string.ascii_lowercase.find(letter))
    elif letter in string.ascii_uppercase:
        position = (string.ascii_uppercase.find(letter))
    return position

def rotate_character(char, rot):
    """ takes a letter of the alphabet (char) and returns the letter
    that is a specific number (rot) of spaces to the right """
    if char not in string.ascii_letters:
        return char
    new_location = (alphabet_position(char) + rot) % 26
    if char in string.ascii_lowercase:
        new_char = string.ascii_lowercase[new_location]
    elif char in string.ascii_uppercase:
        new_char = string.ascii_uppercase[new_location]
    return new_char