from Crypto.Cipher import AES
from Crypto.Util import Counter

BLOCK_SIZE = 16


class AlgAES:
    def encrypt(self, msg: bytes) -> bytes:
        pass

    def decrypt(self, msg: bytes) -> bytes:
        pass

    def execute(self, input_file: str, encrypted_file: str, decrypted_file: str):
        pass


class FixedSizeBlockAES(AlgAES):
    def __init__(self, block_size: int):
        self.block_size = block_size

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
    def __init__(self, key: bytes, block_size: int):
        super(ECB, self).__init__(block_size)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, msg: bytes) -> bytes:
        return self.cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.cipher.decrypt(msg)


class CBC(FixedSizeBlockAES):
    def __init__(self, key: bytes, block_size: int, iv: bytes):
        super(CBC, self).__init__(block_size)
        self.enc_cipher = AES.new(key, AES.MODE_CBC, iv)
        self.dec_cipher = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)


class CTR(AlgAES):
    def __init__(self, key: bytes):
        # prefix == nonce
        self.enc_cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=b'12345678'))
        self.dec_cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=b'12345678'))

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)

    def execute(self, input_file: str, encrypted_file: str, decrypted_file: str):
        self.transform_file(input_file, encrypted_file, self.encrypt)
        self.transform_file(encrypted_file, decrypted_file, self.decrypt)

    def transform_file(self, input_file: str, output_file: str, aes_fn):
        with open(input_file, 'rb') as f:
            file_content = f.read()
        result = aes_fn(file_content)
        with open(output_file, 'wb') as f:
            f.write(result)


def execute_algorithm(alg: str, file: str):
    key = b'Sixteen byte key'
    iv = b'1122334455667788'
    input_file = f'input/{file}.txt'
    encrypted_file = f'encrypted/{file}-{alg}.txt'
    decrypted_file = f'decrypted/{file}-{alg}.txt'
    if alg == 'ECB':
        ecb = ECB(key, BLOCK_SIZE)
        ecb.execute(input_file, encrypted_file, decrypted_file)
    elif alg == 'CBC':
        cbc = CBC(key, BLOCK_SIZE, iv)
        cbc.execute(input_file, encrypted_file, decrypted_file)
    elif alg == 'CTR':
        ctr = CTR(key)
        ctr.execute(input_file, encrypted_file, decrypted_file)
    else:
        raise RuntimeError(f'Unknown algorithm: {alg}')


if __name__ == '__main__':
    algorithms = ['ECB', 'CBC', 'CTR']
    files = ['1Kb', '1Mb', '50Mb', '100Mb', '200Mb']
    for a in algorithms:
        print(f'Algorithm: {a}')
        for f in files:
            print(f'File: {f}')
            execute_algorithm(a, f)
