from Crypto.PublicKey import RSA
print(RSA.import_key((open("2048b-rsa-example-cert.der", "rb").read())).n)