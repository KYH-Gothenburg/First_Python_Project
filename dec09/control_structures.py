def main():
    age = 14
    # ...
    # if-statement
    if age < 20:
        print("Age is less than 20")
    else:
        print("Age is greater than or equal to 20")

    if age < 20:
        print("something")
    elif age < 30:
        print("something else")
    elif age < 40:
        print("more")

    # for-loop
    # for(int i = 2; i < 10; i += 2)
    for i in range(2, 10, 2):
        print(i)

    values = [3, 45, 6, 55, 78]
    # for(var value : values)
    for value in values:
        print(value)

    generated = list(range(100))
    print(generated)

    # Loops and break
    for value in values:
        if value == 55:
            break
        print(value)

    for value in values:
        if value == 56:
            break
        print(value)
    else:
        print("inside else")

    for i, value in enumerate(values):
        print(i, value)


    # while
    value = 0
    while value < 10:
        print(value)
        value += 1

    # Python does not ´have a do while



if __name__ == '__main__':
    main()
