from pyDes import *

def modify(cipher):
    mod = [0]*len(cipher)
    mod[13] = ord(' ') ^ ord('1')
    mod[14] = ord('1') ^ ord('0')
    mod[15] = ord('0') ^ ord('0')

    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

message = "Hey Give Bob: 10$"
key = "DESCRYPT"
iv = bytes([0]*8)

# mode = CBC
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)

# Alice sending encrypted message
cipher = k.encrypt(message)
print("Length of plaintext: ", len(message))
print("Length of cipher: ", len(cipher))
print("Encrypted: ", cipher)

# Bob modifying the cipher text
cipher = modify(cipher)


# This is the bank decrypted the message
message = k.decrypt(cipher)
print("Decrypted: ", message)

