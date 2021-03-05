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
