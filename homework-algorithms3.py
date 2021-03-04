# Question 1.
# #The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
#
#     Fn = Fn-1 + Fn-2
# with seed values
#
#    F0 = 0 and F1 = 1.
# Function for nth Fibonacci number
class Fibonacci(object):
    pass


def fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))


# question 2 Recursion for factorial
# # Factorial of a non-negative integer, is multiplication of all
# integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.


def factorial(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


# Driver Code
num = 5
print("Factorial of", num, "is",
      factorial(num))


# Question 3 Recursion for digital root

# Function to convert given
# sum into string
def converttostring(sum):
    str1 = ""

    # Loop to extract digit one by one
    # from the given sum and concatenate
    # into the string
    while sum:
        # Type casting for concatenation
        str1 = str1 + chr((sum % 10) + ord('0'))
        sum = sum // 10

    # Return converted string
    return str1


# Write a function to check if a number a Perfect or not (link about perfect numbers)
# Returns true if n is perfect
def isperfect(n):
    # To store sum of divisors
    sums = 1

    # Find all divisors and add them
    i = 2
    while i * i <= n:
        if i == 0:
            sums = sums + i + n / i
        else:
            pass
        i += 1

    # If sum of divisors is equal to
    # n, then n is a perfect number

    return True if sums == n and n != 1 else False


# Driver program
print("Below are all perfect numbers till 10000")
n = 2


def imperfect(n):
    """

    :type n: object
    """
    pass


def isPerfect(n: object):
    pass


for n in range(10000):
    if isPerfect(n):
        print(n, " is a perfect number")
