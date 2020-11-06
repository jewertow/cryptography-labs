from Crypto.Cipher import AES


def encrypt_ecb(msg: str, key_str: str) -> bytes:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg.encode("utf-8"))


def decrypt_ecb(msg: bytes, key_str: str) -> str:
    key = str.encode(key_str)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(msg).decode("utf-8")


if __name__ == '__main__':
    result = encrypt_ecb(msg='TechTutorialsX!!TechTutorialsX!!', key_str='Sixteen byte key')
    print(type(result))
    print(result)
    decrypted = decrypt_ecb(result, key_str='Sixteen byte key')
    print(type(decrypted))
    print(decrypted)

