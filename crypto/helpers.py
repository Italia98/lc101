import string


def alphabet_position(letter):
    if letter in string.ascii_uppercase:
        position = string.ascii_uppercase.find(letter)

    elif letter in string.ascii_lowercase:
        position = string.ascii_lowercase.find(letter)

    return position


def rotate_character(letter, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in letter:
        if not(char.isalpha()):
            encrypted = encrypted + char
        else:
            rotated_index = (alphabet_position(letter) + rot)
            if char.islower():
                encrypted = encrypted + alphabet[rotated_index %26]
            else:
                encrypted = encrypted + alphabet.upper()[rotated_index % 26]
    return encrypted