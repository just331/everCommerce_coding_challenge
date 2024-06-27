from utils import is_prime


def prime_generator(start: int, end: int) -> list:
    # handle inverse range input
    if start > end:
        start, end = end, start

    primes_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes_list.append(num)

    return primes_list
