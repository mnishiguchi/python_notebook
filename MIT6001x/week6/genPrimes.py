# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

# Ideas about the problem
# Have the generator keep a list of the primes it's generated.
# A candidate number x is prime if (x % p) != 0 for all earlier primes p.
def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
 
genPrimes()           
for prime in genPrimes()  :
    print prime