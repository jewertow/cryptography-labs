from Crypto.Cipher import AES

BLOCK_SIZE = 16


def encrypt_ecb(msg: bytes, key_str: str) -> bytes:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


def encrypt_cbc(msg: bytes, key_str: str) -> bytes:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1111111111111111')
    return cipher.encrypt(msg)


def decrypt_ecb(msg: bytes, key_str: str) -> bytes:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(msg)


def decrypt_cbc(msg: bytes, key_str: str) -> bytes:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1111111111111111')
    return cipher.decrypt(msg)


def encrypt_file(input_file_name: str, output_file_name: str, key: str, encrypt):
    with open(input_file_name, 'rb') as f:
        plaintext = f.read()
    blocks = _to_blocks(plaintext)
    encrypted_blocks = []
    for block in blocks:
        enc_block = encrypt(block, key)
        encrypted_blocks.append(enc_block)
    result = b''.join(encrypted_blocks)
    with open(output_file_name, 'wb') as f:
        f.write(result)


def decrypt_file(input_file_name: str, output_file_name: str, key: str, decrypt):
    with open(input_file_name, 'rb') as f:
        encrypted = f.read()
    blocks = _to_blocks(encrypted)
    decrypted_blocks = []
    for block in blocks:
        dec_block = decrypt(block, key)
        decrypted_blocks.append(dec_block)
    result = b''.join(decrypted_blocks)
    with open(output_file_name, 'wb') as f:
        f.write(result)


def _to_blocks(string):
    return [string[i:i+BLOCK_SIZE] for i in range(0, len(string), BLOCK_SIZE)]


def main():
    alg = 'ECB'
    key = 'Sixteen byte key'
    prefix_name = '1Kb'
    input_file_name = f'input/{prefix_name}.txt'
    encrypted_file_name = f'{prefix_name}-{alg}.enc.txt'
    decrypted_file_name = f'{prefix_name}-{alg}.dec.txt'
    if alg == 'ECB':
        encrypt_file(input_file_name, encrypted_file_name, key, encrypt=encrypt_ecb)
        decrypt_file(encrypted_file_name, decrypted_file_name, key, decrypt=decrypt_ecb)
    elif alg == 'CBC':
        encrypt_file(input_file_name, encrypted_file_name, key, encrypt=encrypt_cbc)
        decrypt_file(encrypted_file_name, decrypted_file_name, key, decrypt=decrypt_cbc)
    else:
        raise RuntimeError(f'Unknown algorithm: {alg}')


if __name__ == '__main__':
    main()
