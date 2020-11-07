from Crypto.Cipher import AES
from Crypto.Util import Counter
from time import time


class AlgAES:
    def encrypt(self, msg: bytes) -> bytes:
        pass

    def decrypt(self, msg: bytes) -> bytes:
        pass

    def transform_file(self, input_file: str, output_file: str, aes_fn) -> float:
        pass

    def execute(self, input_file: str, encrypted_file: str, decrypted_file: str) -> (float, float):
        encryption_time = self.transform_file(input_file, encrypted_file, self.encrypt)
        decryption_time = self.transform_file(encrypted_file, decrypted_file, self.decrypt)
        return encryption_time, decryption_time


class BlockAES(AlgAES):
    def __init__(self, block_size: int):
        self.block_size = block_size

    def transform_file(self, input_file: str, output_file: str, aes_fn) -> float:
        with open(input_file, 'rb') as f:
            file_content = f.read()
        blocks = self._to_blocks(file_content)
        partial_results = []
        start = time()
        for block in blocks:
            block_res = aes_fn(block)
            partial_results.append(block_res)
        result = b''.join(partial_results)
        end = time()
        with open(output_file, 'wb') as f:
            f.write(result)
        return end - start

    def _to_blocks(self, string):
        return [string[i:i + self.block_size] for i in range(0, len(string), self.block_size)]


class StreamAES(AlgAES):
    def transform_file(self, input_file: str, output_file: str, aes_fn) -> float:
        with open(input_file, 'rb') as f:
            file_content = f.read()
        start = time()
        result = aes_fn(file_content)
        end = time()
        with open(output_file, 'wb') as f:
            f.write(result)
        return end - start


class ECB(BlockAES):
    def __init__(self, key: bytes, block_size: int):
        super(ECB, self).__init__(block_size)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, msg: bytes) -> bytes:
        return self.cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.cipher.decrypt(msg)


class CBC(BlockAES):
    def __init__(self, key: bytes, block_size: int, iv: bytes):
        super(CBC, self).__init__(block_size)
        self.enc_cipher = AES.new(key, AES.MODE_CBC, iv)
        self.dec_cipher = AES.new(key, AES.MODE_CBC, iv)

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)


class CFB(StreamAES):
    def __init__(self, key: bytes, iv: bytes):
        self.enc_cipher = AES.new(key, AES.MODE_CFB, iv)
        self.dec_cipher = AES.new(key, AES.MODE_CFB, iv)

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)


class OFB(StreamAES):
    def __init__(self, key: bytes, iv: bytes):
        self.enc_cipher = AES.new(key, AES.MODE_CFB, iv)
        self.dec_cipher = AES.new(key, AES.MODE_CFB, iv)

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)


class CTR(StreamAES):
    def __init__(self, key: bytes):
        self.enc_cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=b'12345678'))
        self.dec_cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(64, prefix=b'12345678'))

    def encrypt(self, msg: bytes) -> bytes:
        return self.enc_cipher.encrypt(msg)

    def decrypt(self, msg: bytes) -> bytes:
        return self.dec_cipher.decrypt(msg)
