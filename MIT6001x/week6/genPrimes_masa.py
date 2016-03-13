## my implementation
## very inefficient and slow!!!

def genPrimes():
    n = 0
    while True:
        if isPrime(n):
            yield n
        n += 1

def isPrime(n):
    # one is not considered a prime number
    if n <= 1:
        return False
    # two is a prime number
    elif n == 2:
        return True
    # requirement : has no positive divisors other than 1 and itself.
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

for prime in genPrimes():
    print prime