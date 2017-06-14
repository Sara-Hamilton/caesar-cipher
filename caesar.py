from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    """ takes a string (text) and returns a string of the same length
    with all of the alpha characters rotated a specific number (rot)
    of spaces to the right of the alphabet """
    new_string = ""
    for char in text:
        new_string = new_string + rotate_character(char, rot)
    return new_string

def main():
    """ prompts user for input of a string
    verifies input arguments are correct
    and returns the encrypted string"""
    from sys import argv, exit
    if len(argv) != 2 or argv[1].isdigit() is False:
        print('usage: python caesar.py n')
        exit()
    rot = int(argv[1])
    text = input("Type a message:")
    result = rotate_string(text, rot)
    return result

if __name__ == "__main__":
    main()