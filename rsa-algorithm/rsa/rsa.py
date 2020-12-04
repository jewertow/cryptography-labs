from sympy import nextprime
from math import gcd


class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = find_relatively_prime(self.phi)
        self.d = self._find_d()
        self.block_size = len(str(self.n)) - 1
        print(f'phi = {self.phi}, block_size = {self.block_size}')

    def get_private_key(self) -> (int, int):
        return self.d, self.n

    def get_public_key(self) -> (int, int):
        return self.e, self.n

    def encrypt(self, message: str) -> str:
        result = ''
        for char in message:
            # c = m ^ e mod n
            enc = (ord(char) ** self.e) % self.n
            enc = str(enc).ljust(self.block_size)
            result += str(enc)
        return result

    def decrypt(self, encrypted_msg: str) -> str:
        result = ''
        for i in range(0, len(encrypted_msg), self.block_size):
            block = encrypted_msg[i: i + self.block_size]
            block = block.strip()
            # m = c ^ d mod n
            dec = (int(block) ** self.d) % self.n
            result += str(chr(dec))
        return result

    def _find_d(self):
        d = 2
        while (self.e * d - 1) % self.phi != 0:
            d += 1
        return d


# FIXME: ta funkcja szuka tylko większej od x, a mniejsza liczba też może być względnie pierwsza
def find_relatively_prime(x: int) -> int:
    prime = nextprime(x)
    while not (gcd(prime, x) == 1):
        prime = nextprime(prime)
    return prime
