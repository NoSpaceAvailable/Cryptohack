from Crypto.PublicKey import RSA
key = open("privacy_enhanced_mail.pem", "rb").read()
print(RSA.import_key(key).d)