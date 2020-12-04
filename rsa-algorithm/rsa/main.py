from rsa import RSA
from sympy import nextprime


def main():
    p = nextprime(1000)
    q = nextprime(p)
    rsa = RSA(p, q)
    print(f'p = {p}; q = {q}')
    private_key = rsa.get_private_key()
    print(f'private key = {private_key}')
    public_key = rsa.get_public_key()
    print(f'public key = {public_key}')
    message = 'Lorem ipsum dolor sit amet, consectetur tincidunt.'
    print(f'message: {message}')
    encrypted = rsa.encrypt(message)
    print(f'encrypted message: {encrypted}')
    decrypted = rsa.decrypt(encrypted)
    print(f'decrypted message: {decrypted}')


if __name__ == '__main__':
    main()
