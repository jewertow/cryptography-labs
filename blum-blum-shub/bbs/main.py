from bbs import find_next_prime, generate_pseudo_random_string
from fips_tests import single_bit_test, series_test, long_series_test, poker_test, _divide_into_segments, _segments_to_int_values
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
    print('Test pojedynczych bitów:')
    single_bits_counter, passed = single_bit_test(random_bits_string)
    print(f'Liczba bitów równych 1: {single_bits_counter}')
    print_test_result(passed)

    print('------------------')
    print('Test serii:')
    results, passed = series_test(random_bits_string)
    print(results)
    print_test_result(passed)

    print('------------------')
    print('Test długiej serii:')
    passed = long_series_test(results)
    print_test_result(passed)

    print('------------------')
    print('Test pokerowy:')
    poker_test_value, passed = poker_test(random_bits_string)
    print(f'Wynik testu pokerowego: {poker_test_value}')
    print_test_result(passed)


def print_test_result(passed: bool):
    if passed:
        print('Test zaliczony')
    else:
        print('Test niezaliczony')


if __name__ == '__main__':
    main()
