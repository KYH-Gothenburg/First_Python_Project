import math
from math import sqrt
#from math import *  # Should not be used, pollutes your namespace
from math import sqrt as root


def sqrt(x):
    return x * 2


def main():
    print(math.sqrt(9))  # Uses import math
    print(sqrt(9))       # Uses from math import sqrt
    print(root(9))


if __name__ == '__main__':
    main()
