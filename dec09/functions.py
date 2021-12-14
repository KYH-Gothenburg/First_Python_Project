from other import print_double


def greet(name, end="."):
    message = f"Hello {name}{end}"
    print(message)


def create_greeting(name, end="."):
    return f"Hello {name}{end}"


def double_values(a, b):
    a *= 2
    b *= 2
    return a, b


def many_values():
    return 10, 15, 23, 45, 67, 88, 94


def main():
    greet("Anna", "!")
    greet(end="?", name="Pelle")
    greet("Lisa")

    message = create_greeting("Bob")
    print(message)

    x = 10
    y = 20
    x, y = double_values(x, y)
    print(x, y)
    result = double_values(30, 60)
    print(result)

    result = many_values()
    print(result)

    x, *y = many_values()
    print(x, y)
    first, *rest, last = many_values()
    print(first, rest, last)

    first, *_, last = many_values()
    print(first, last)

    print_double(5)


if __name__ == '__main__':
    main()
