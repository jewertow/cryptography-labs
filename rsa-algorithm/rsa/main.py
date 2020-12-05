from rsa import rsa, encrypt, decrypt
from sympy import nextprime


def main():
    p = nextprime(1000)
    q = nextprime(p)
    private_key, public_key = rsa(p, q)
    print(f'p = {p}; q = {q}')
    print(f'private key = ({private_key.d}, {private_key.n})')
    print(f'public key = ({public_key.e}, {public_key.n})')

    message = 'Lorem ipsum dolor sit amet, consectetur tincidunt.'
    encrypted = encrypt(public_key, message)
    print(f'encrypted message: {encrypted}')
    decrypted = decrypt(private_key, encrypted)
    print(f'decrypted message: {decrypted}')


if __name__ == '__main__':
    main()
