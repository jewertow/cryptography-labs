from bbs import find_next_usable_prime, run_bbs

if __name__ == '__main__':
    p = 7_000_000
    q = 11_000_000
    p = find_next_usable_prime(p)
    q = find_next_usable_prime(q)
    size = 100
    result = run_bbs(p, q, size)
    print(result)
