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




