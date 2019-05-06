from helpers import alphabet_position, rotate_character

def encrypt(text,keyword):
    counter = 0
    encrypted = ''

    for letter in text:
        if letter.isalpha():
            encrypted += rotate_character(letter, alphabet_position(keyword[counter]))
            counter += 1
            if counter > len(keyword)-1:
                counter = 0
        else:
            encrypted += letter
        
    return encrypted

def main():
    text = input("Whats the text you want to encrypt : ")
    keyword = input("Give me a rotation keyword : ")

    print(encrypt(text, keyword))
    print("Uvs osck rmwse bh auebwsih!")

if __name__ == "__main__":
    main()