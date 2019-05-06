
def get_initials(fullname):
    words = fullname.split()
    word_lst = ''
    for word in words:
        word_lst += word[0].upper()

    return word_lst


def main():
    fullname = input("What is your full name?")
    answer = get_initials(fullname)
    print("The initials of", fullname, "are", answer)


if __name__ == '__main__':
    main()
