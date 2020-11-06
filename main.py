from Crypto.Cipher import AES

BLOCK_SIZE = 16


class FixedSizeBlockAES:
    def __init__(self, key: bytes, block_size: int):
        self.key = key
        self.block_size = block_size

    def encrypt(self, msg: bytes) -> bytes:
        pass

    def decrypt(self, msg: bytes) -> bytes:
        pass

    def execute(self, input_file: str, encrypted_file: str, decrypted_file: str):
        self.transform_file(input_file, encrypted_file, self.encrypt)
        self.transform_file(encrypted_file, decrypted_file, self.decrypt)

    def transform_file(self, input_file: str, output_file: str, aes_fn):
        with open(input_file, 'rb') as f:
            file_content = f.read()
        blocks = self._to_blocks(file_content)
        partial_results = []
        for block in blocks:
            block_res = aes_fn(block)
            partial_results.append(block_res)
        result = b''.join(partial_results)
        with open(output_file, 'wb') as f:
            f.write(result)

    def _to_blocks(self, string):
        return [string[i:i + self.block_size] for i in range(0, len(string), self.block_size)]


class ECB(FixedSizeBlockAES):
    def encrypt(self, msg: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_ECB)
        return cipher.decrypt(msg)


class CBC(FixedSizeBlockAES):
    def __init__(self, key: bytes, block_size: int, iv: bytes):
        super(CBC, self).__init__(key, block_size)
        self.iv = iv

    def encrypt(self, msg: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.decrypt(msg)


def main():
    alg = 'ECB'
    iv = b'1111111111111111'
    key = b'Sixteen byte key'
    prefix_name = '200Mb'
    input_file = f'input/{prefix_name}.txt'
    encrypted_file = f'{prefix_name}-{alg}.enc.txt'
    decrypted_file = f'{prefix_name}-{alg}.dec.txt'
    if alg == 'ECB':
        ecb = ECB(key, BLOCK_SIZE)
        ecb.execute(input_file, encrypted_file, decrypted_file)
    elif alg == 'CBC':
        cbc = CBC(key, BLOCK_SIZE, iv)
        cbc.execute(input_file, encrypted_file, decrypted_file)
    else:
        raise RuntimeError(f'Unknown algorithm: {alg}')


if __name__ == '__main__':
    main()
