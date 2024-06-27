def is_prime(value:int) -> bool:
    # Base case - value leq 1 then not prime
    if value <= 1:
        return False
    # Base case - value equals 2 then prime
    if value == 2:
        return True
    # Base case - value is even then not prime
    if value % 2 == 0:
        return False

    for i in range(3, int(value ** 2) + 1, 2):
        if value % i == 0:
            return False
    return True
