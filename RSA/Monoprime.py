from Crypto.Util.number import long_to_bytes

data = []
with open("output_monoprime.txt") as f:
    for line in f.readlines():
        data.append(int(line.strip().split(' = ')[1]))
n, e, ct = data
d = pow(e, -1, n - 1)
print(long_to_bytes(pow(ct, d, n)).decode())