import sys
from prime_generator import prime_generator


def main():
    if len(sys.argv) != 3:
        print("To Run: python main.py <start> <end>")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("Valid integer inputs only")
        return

    primes_list = prime_generator(start, end)
    print(f"The prime numbers between {start} - {end} are: {primes_list}")


if __name__ == '__main__':
    main()
