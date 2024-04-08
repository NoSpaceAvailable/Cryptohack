#!/usr/bin/env python3
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

def challenge():
    e = 1
    d = -1

    while d == -1:
        p = getPrime(512)
        q = getPrime(512)
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)
    print(d)
    n = p * q

    flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
    pt = bytes_to_long(flag)
    ct = pow(pt, e, n)

    print(f"n = {n}")
    print(f"e = {e}")
    print(f"ct = {ct}")

    pt = pow(ct, d, n)
    decrypted = long_to_bytes(pt)
    assert decrypted == flag

if __name__ == "__main__":
    data = []
    with open("output_salty.txt") as f:
        for line in f.readlines():
            data.append(int(line.strip().split(' = ')[1]))
    n, e, ct = data
    # d = 1 because e = 1
    print(long_to_bytes(pow(ct, 1, n)).decode())