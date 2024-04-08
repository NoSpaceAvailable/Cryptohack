from Crypto.Util.number import bytes_to_long
from hashlib import sha256

N, d = open("private_RSA6.key").read().replace('\n', '').replace('d', '').split(' = ')[1:3]
P = b'crypto{Immut4ble_m3ssag1ng}'
# To sign this message, you calculate the hash of the message: H(M) and "encrypt" this with your private key: S = H(M)^d1 mod N1
S = pow(bytes_to_long(sha256(P).digest()), int(d), int(N))
print(S)