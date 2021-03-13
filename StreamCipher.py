import random

class KeyStream:
    def __init__(self, key= 1):
        self.next = key

    def rand(self):
        # Linear congruential generator
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod = [0]*len(cipher)
    mod[11] = ord(' ') ^ ord('1')
    mod[12] = ord(' ') ^ ord('0')
    mod[13] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

# Which given the message and cipher returns the corresponding key stream
def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

# Which given a key_stream and a cipher can decrypt as long as there is key stream enough
def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

# This is goes to alice
eve_message = "This is eve's values secret of her life".encode()

# This is Alice alone
key = KeyStream(31)
message = eve_message
cipher = encrypt(key, message)
print("This Alice alone")
print(message)
print(cipher)
print("\n")

# This is Eve (alone) all evil
eves_key_stream = get_key(eve_message, cipher)

# This is Bank
key = KeyStream(31)
message = encrypt(key, cipher)
print("This is Bob")
print(message)
print("\n")

# Alice agin
message = "Hi bob, let's meet a plan our world domination haha".encode()
key = KeyStream(31)
cipher = encrypt(key, message)
print("This is Alice again")
print(cipher)
print("\n")

# Bob again
key = KeyStream(31)
message = encrypt(key, cipher)
print("This is Bob again")
print(message)
print("\n")

# Eve again
print("This is Eve again")
print(crack(eves_key_stream, cipher))