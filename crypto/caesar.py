from helpers import alphabet_position, rotate_character

def encrypt(text, rot):

    encrypted_text = ""

    for letter in text:
        encrypted_text += rotate_character(letter, rot)

    return encrypted_text


def main():
    from sys import argv
    print("This is what the user typed on the command line:", argv)
    text = input("Type a message: ")

    rot = input("What's the number of rotations?")
    rot = int(rot)
    print(encrypt(text, rot))


if __name__=='__main__':
    main()

   
