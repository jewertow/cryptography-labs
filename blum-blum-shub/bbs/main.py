from bbs import find_next_prime, generate_pseudo_random_string
from fips_tests import single_bit_test, series_test
import random

DEBUG = False


def debug(log):
    if DEBUG:
        print(log)


def main():
    random.seed(32)
    p = 7_000_000
    q = 11_000_000
    p = find_next_prime(p)
    q = find_next_prime(q)
    size = 20_000
    n, x, random_bits_string = generate_pseudo_random_string(p, q, size)
    debug(random_bits_string)
    print(f'n = {n}')
    print(f'x = {x}')

    print('------------------')
    print('Test pojedynczych bitów')
    single_bits_counter, passed = single_bit_test(random_bits_string)
    print(f'Liczba bitów równych 1: {single_bits_counter}')
    if passed:
        print('Test zaliczony')
    else:
        print('Test niezaliczony')

    print('------------------')
    print('Test serii')
    results, passed = series_test(random_bits_string)
    print(results)
    if passed:
        print('Test zaliczony')
    else:
        print('Test niezaliczony')

    suma = 0
    for key, value in results.items():
        suma += (key * value)
    print(suma)


if __name__ == '__main__':
    main()
