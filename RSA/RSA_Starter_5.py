N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
d = 121832886702415731577073962957377780195510499965398469843281
c = 77578995801157823671636298847186723593814843845525223303932
x = (p - 1)*(q - 1) # totient
"""
    Choose two large prime numbers, p and q.
    compute n = p * q and x = (p-1)*(q-1)
    Choose a number relatively prime to x and call it d. This means that d is not a prime factor of x or a multiple of it.
    Find e such that e * d = 1 mod x.

    To encrypt: C = P^e (mod n) (C = ciphertext)
    To decrypt: P = C^d (mod n) (P = plaintext)
"""

def decrypt(cipher):
    return pow(c, d, N)

print(decrypt(c))