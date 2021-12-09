def print_greeting():
    print('Hello there')


def main():
    age = 14
    name = 'Joakim'
    message = name + ' ' + str(age)

    print(message)



# __name__ contains the string '__main__' if
# we run this file.
# If we import the file it will contain the name of the file
if __name__ == '__main__':
    main()
#main()