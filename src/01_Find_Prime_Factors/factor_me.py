def find_primes_until(num):
    end = ((num//2) + 1)
    if end <= 2:
        return []

    primes = [2]
    for number in range(3,end,2):
        for factor in range(3,int((number**0.5)+1)):
            if number % factor == 0:
                break
        else:
            primes.append(number)
    return primes

def get_prime_factors(num):
    primes = find_primes_until(num)
    factors = []

    for prime in primes:
        while num % prime == 0:
            factors.append(prime)
            num = num // prime
    if num > 1:
        factors.append(num)
    return factors
        
        

if __name__ == '__main__':
    print(get_prime_factors(630))  # [2, 3, 3, 5, 7]
    print(get_prime_factors(13))  # [13]
    print(get_prime_factors(100))