from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_cbc(data: bytes, key: bytes, iv: bytes):
    padded = pad(data, block_size=16)
    prev_block = iv
    encrypted = []
    for i in range(0, len(padded), 16):
        block = padded[i: i + 16]
        encrypted_block = _encrypt_ecb(_xor(block, prev_block), key)
        encrypted.append(encrypted_block)
        prev_block = encrypted_block
    result = b''.join(encrypted)
    return result


def decrypt_cbc(data: bytes, key: bytes, iv: bytes):
    prev_block = iv
    decrypted = []
    for i in range(0, len(data), 16):
        block = data[i: i + 16]
        decrypted_block = _xor(_decrypt_ecb(block, key), prev_block)
        decrypted.append(decrypted_block)
        prev_block = block
    result = b''.join(decrypted)
    return unpad(result, block_size=16)


def _xor(b1: bytes, b2: bytes):
    return bytes([_b1 ^ _b2 for _b1, _b2 in zip(b1, b2)])


def _encrypt_ecb(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)


def _decrypt_ecb(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(data)


if __name__ == '__main__':
    key = b'1122334455667788'
    iv = b'0000000000000000'
    encrypted = encrypt_cbc(b'Lorem ipsum 123456789', key, iv)
    print(f'encrypted = {encrypted}')
    decrypted = decrypt_cbc(encrypted, key, iv)
    print(f'decrypted = {decrypted.decode()}')
