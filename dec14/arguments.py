def func(x):
    x.append(4)
    print("In func", x)


def func2(name, names=None):
    if names is None:
        names = []
    names.append(name)
    return names


def main():
    members = ['Alice', 'Bob']
    print(func2('Carl'))
    print(func2('Dina'))
    print(func2('Eric'))
    # values = [1, 2, 3]
    # func(values)
    # print("After call to func", values)


if __name__ == '__main__':
    main()
