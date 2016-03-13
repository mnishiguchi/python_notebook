def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)


# testDriver
def applyToEach(aList, aFunction):
    for (a, b) in aList :
        print a,'%', b, 'this:', aFunction(a, b), 'built-in:', a%b

test = [(5, 5), (2, 5), (7, 5), (1, 1), (1, 5), (5, 1)]
applyToEach(test, rem)
