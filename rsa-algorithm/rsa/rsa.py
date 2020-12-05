from sympy import nextprime
from math import gcd


class PrivateKey:
    def __init__(self, d, n):
        self.d = d
        self.n = n


class PublicKey:
    def __init__(self, e, n):
        self.e = e
        self.n = n


def rsa(p: int, q: int) -> (PrivateKey, PublicKey):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_relatively_prime(phi)
    d = _find_d(e, phi)
    return PrivateKey(d, n), PublicKey(e, n)


def encrypt(pub_key: PublicKey, message: str) -> str:
    block_size = len(str(pub_key.n - 1))
    result = ''
    for char in message:
        # c = m ^ e mod n
        enc = (ord(char) ** pub_key.e) % pub_key.n
        enc = str(enc).ljust(block_size)
        result += str(enc)
    return result


def decrypt(priv_key: PrivateKey, encrypted_msg: str) -> str:
    block_size = len(str(priv_key.n - 1))
    result = ''
    for i in range(0, len(encrypted_msg), block_size):
        block = encrypted_msg[i: i + block_size]
        block = block.strip()
        # m = c ^ d mod n
        dec = (int(block) ** priv_key.d) % priv_key.n
        result += str(chr(dec))
    return result


def _find_d(e: int, phi: int) -> int:
    d = 2
    while (e * d - 1) % phi != 0:
        d += 1
    return d


# FIXME: ta funkcja szuka tylko większej od x, a mniejsza liczba też może być względnie pierwsza
def find_relatively_prime(x: int) -> int:
    prime = nextprime(x)
    while not (gcd(prime, x) == 1):
        prime = nextprime(prime)
    return prime
