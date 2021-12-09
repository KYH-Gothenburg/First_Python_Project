def main():
    # Numerical
    # int
    number = 10002929292929192929**50
    # float
    dec = 3.123456789012345

    # Logiska
    # Boolean
    done = True
    done = False

    # String
    name = 'Joakim'

    # Sequence
    # List - uses [ ], dynamic
    values = [1, 2, 3, 4, 5, "hej", True, 4.56]

    # Tuple - uses ()
    tuple_values = (1, 2, 3, 4, "hopp")

    # Indexing
    print(values.index('hej'))
    print(tuple_values[2])

    # Set - uses { } works like a list, but can only store unique values
    set_values = {1, 2, 3, 4, 5, 1, 2}
    print(set_values)
    list_values = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    list_values = list(set(list_values))
    print(list_values)

    # dictionary
    person = {
        'name': 'Pelle',
        'age': 34,
        'email': 'pelle@email.com'
    }
    print(person['email'])




if __name__ == '__main__':
    main()
