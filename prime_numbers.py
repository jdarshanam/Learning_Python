#Solution-I
def count_primes(num: int) -> int:
    if num < 2:
        return 0
    
    # 2 or greater
    #list to store our prime numbers
    primes = [2]
    # Counter going upto input num
    x = 3

    while x < num:
        #check if x is prime
        for y in range(3,x,2): # step 2 , because we are interested only odd numbers, as evens are divisible by 2.
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(f"primes - {primes}")
    return len(primes)
print(count_primes(100))

#Solution-II
def count_primes_improved(num: int) -> int:
    if num < 2:
        return 0
    
    # 2 or greater
    #list to store our prime numbers
    primes = [2]
    # Counter going upto input num
    x = 3

    while x < num:
        #check if x is prime
        for y in primes: # step 2 , because we are interested only odd numbers, as evens are divisible by 2.
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(f"primes - {primes}")
    return len(primes)

print(count_primes_improved(100))

#Solution-III
def count_primes_fast(num: int) -> int:
    if num < 2:
        return 0

    primes = [2]
    x = 3

    while x <= num:
        # Only check against primes we've already found, up to sqrt(x)
        for p in primes:
            if p * p > x:  # Past the square root? It's prime!
                primes.append(x)
                break
            if x % p == 0:  # Divisible by a prime? Not prime!
                break
        x += 2

    print(f"primes - {primes}")
    return len(primes)
print(count_primes_fast(100))