def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
        
    return True

# filter(func, itarable)
def filter_primes(sequence):
    return filter(is_prime, sequence)

print(list(filter_primes([11, 1, 10, 9, 2, 5, 4])))