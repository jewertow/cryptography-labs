from math import gcd
from random import seed, randint
from sympy import isprime, nextprime
from typing import List


def generate_pseudo_random_string(p: int, q: int, size: int) -> (int, int, List[int]):
    _validate_values(p, q)
    n = p * q
    x = _find_x(n)
    bit_values = []
    for _ in range(size):
        x = (x * x) % n
        print(x)
        bit = x % 2
        bit_values.append(bit)
    return n, x, bit_values


def find_next_usable_prime(x):
    p = nextprime(x)
    while p % 4 != 3:
        p = nextprime(p)
    return p


def _validate_values(p, q) -> None:
    if p < 0 or q < 0:
        raise RuntimeError("'p' and 'q' must be greater than 0")
    if not isprime(p):
        raise RuntimeError("'p' is not a prime number")
    if not isprime(q):
        raise RuntimeError("'q' is not a prime number")
    if not is_congruent(p):
        raise RuntimeError("'p' is not congruent with 3 mod 4")
    if not is_congruent(q):
        raise RuntimeError("'q' is not congruent with 3 mod 4")


def is_congruent(x: int) -> bool:
    return (x - 3) % 4 == 0


def _find_x(n) -> int:
    x = randint(1, int(1e10))
    while not _are_relatively_prime(n, x):
        x = randint(1, int(1e10))
    return x


def _are_relatively_prime(n, x) -> bool:
    return gcd(n, x) == 1
