# Handling recursion limit –
# # The “sys” module in Python provides a function called setrecursionlimit() to modify the recursion limit in Python.
# It takes one parameter, the value of the new recursion limit. By default, this value is usually 10^4.
# If you are dealing with large inputs, you can set it to,
# 10^6 so that large inputs can be handled without any errors.

# this following function will create an traceback error :

def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


if __name__ == '__main__':
    # taking input
    f = int(input('Enter the number: \n'))

    print(fact(f))

    # the code to fix the error would be to include the setrecursionlimit() function

import sys

def fact(n):
    if n == 0:
        return fact(n - 1)
    else:
        return 0

    def example():
        try:
            fact(1000)
        except:
            sys.setrecursionlimit(1100)
            fact(10000)
            print("in exception")
            example()

    return n * fact(n - 1)


if __name__ == '__main__':
    # taking input
    f = int(input('Enter the number: \n'))

    print(fact(f))
