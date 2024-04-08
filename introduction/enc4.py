from Crypto.Util.number import *

if __name__ == "__main__":
    base10_str = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    byte_str = long_to_bytes(base10_str)
    flag = bytes.decode(byte_str)
    print(flag)