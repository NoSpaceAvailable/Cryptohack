from pwn import *
from Crypto.Util import *
from base64 import b64decode
import json
import codecs

HOST = "socket.cryptohack.org"
PORT = 13377

r = remote(host=HOST, port=PORT)

def dec_base64(b64 : str) -> str:
    return b64decode(b64).decode('utf-8')

def dec_hex(hex : str) -> str:
    return bytes.fromhex(hex).decode('utf-8')

def dec_rot13(enc : str) -> str:
    return codecs.decode(enc, 'rot_13')

def dec_bigint(bigint : str) -> str:
    return bytes.fromhex(bigint[2:]).decode('utf-8')

def dec_utf8(utf8 : list) -> str:
    return ''.join([chr(i) for i in utf8])

if __name__ == "__main__":
    while True:
        try:
            data = json.loads(r.recvline().strip())
            if ("flag" in data):
                print("[o] The flag is:", data["flag"])
                break
            res = ""
            send = ''
            if data["type"] == "base64":
                res = dec_base64(data["encoded"])
            elif data["type"] == "hex":
                res = dec_hex(data["encoded"])
            elif data["type"] == "rot13":
                res = dec_rot13(data["encoded"])
            elif data["type"] == "bigint":
                res = dec_bigint(data["encoded"])
            elif data["type"] == "utf-8":
                res = dec_utf8(data["encoded"])
            send = json.dumps({"decoded":res}).encode()
            r.sendline(send)
            print("[o] Data {} sent successfully!".format(send))
        except Exception as e:
            print("Error: {}".format(e))
            break
        
        