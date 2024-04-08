from Crypto.PublicKey import RSA
print(RSA.import_key(open("bruce_rsa.pub").read()).n)