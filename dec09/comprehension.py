def main():
    values = [1, 2, 3, 4, 5, 6]
    new_values = []
    for value in values:
        if value % 2 == 0:
            new_values.append(value * 2)

    print(new_values)

    # List comprehension
    new_values = [value * 2 for value in values if value % 2 == 0]
    print(new_values)

    # Set comprehension
    new_values = {value * 2 for value in values if value % 2 == 0}
    print(new_values)

    # dictionary comprehension
    new_values = {value: value * 2 for value in values if value % 2 == 0}
    print(new_values)

    # tuple comprehension
    new_values = tuple([value * 2 for value in values if value % 2 == 0])
    print(new_values)


if __name__ == '__main__':
    main()
