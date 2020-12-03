from aes import ECB, CBC, CFB, OFB, CTR


def destroy_random_byte(file: str):
    with open(file, 'r+b') as f:
        f.seek(100)
        f.write(b'1')


def destroy_decrypted_file(alg: str, file: str):
    key = b'Sixteen byte key'
    iv = b'1122334455667788'
    block_size = 16
    encrypted_file = f'encrypted/{file}-{alg}.txt'
    destroyed_file = f'damaged/{file}-{alg}.txt'
    destroy_random_byte(encrypted_file)
    if alg == 'ECB':
        ecb = ECB(key, block_size)
        ecb.transform_file(encrypted_file, destroyed_file, ecb.decrypt)
    elif alg == 'CBC':
        cbc = CBC(key, block_size, iv)
        cbc.transform_file(encrypted_file, destroyed_file, cbc.decrypt)
    elif alg == 'CFB':
        cfb = CFB(key, iv)
        cfb.transform_file(encrypted_file, destroyed_file, cfb.decrypt)
    elif alg == 'OFB':
        ofb = OFB(key, iv)
        ofb.transform_file(encrypted_file, destroyed_file, ofb.decrypt)
    elif alg == 'CTR':
        ctr = CTR(key)
        ctr.transform_file(encrypted_file, destroyed_file, ctr.decrypt)
    else:
        raise RuntimeError(f'Unknown algorithm: {alg}')


if __name__ == '__main__':
    algorithms = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']
    files = ['1Kb', '1Mb', '50Mb', '100Mb', '200Mb']
    for a in algorithms:
        print(f'Algorithm: {a}')
        for f in files:
            print(f'File: {f}')
            destroy_decrypted_file(a, f)
