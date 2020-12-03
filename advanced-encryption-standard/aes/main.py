from aes import ECB, CBC, CFB, OFB, CTR, AlgAES


def execute_algorithm(alg: str, file: str):
    key = b'Sixteen byte key'
    iv = b'1122334455667788'
    block_size = 16
    input_file = f'input/{file}.txt'
    encrypted_file = f'encrypted/{file}-{alg}.txt'
    decrypted_file = f'decrypted/{file}-{alg}.txt'
    if alg == 'ECB':
        ecb = ECB(key, block_size)
        execute_and_log(ecb, input_file, encrypted_file, decrypted_file)
    elif alg == 'CBC':
        cbc = CBC(key, block_size, iv)
        execute_and_log(cbc, input_file, encrypted_file, decrypted_file)
    elif alg == 'CFB':
        cfb = CFB(key, iv)
        execute_and_log(cfb, input_file, encrypted_file, decrypted_file)
    elif alg == 'OFB':
        ofb = OFB(key, iv)
        execute_and_log(ofb, input_file, encrypted_file, decrypted_file)
    elif alg == 'CTR':
        ctr = CTR(key)
        execute_and_log(ctr, input_file, encrypted_file, decrypted_file)
    else:
        raise RuntimeError(f'Unknown algorithm: {alg}')


def execute_and_log(aes: AlgAES, input_file: str, encrypted_file: str, decrypted_file: str):
    encryption_time, decryption_time = aes.execute(input_file, encrypted_file, decrypted_file)
    print(f'encryption: {round(encryption_time, 8)}s')
    print(f'decryption: {round(decryption_time, 8)}s')


if __name__ == '__main__':
    algorithms = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']
    files = ['1Kb', '1Mb', '50Mb', '100Mb', '200Mb']
    for a in algorithms:
        print(f'Algorithm: {a}')
        for f in files:
            print(f'File: {f}')
            execute_algorithm(a, f)
