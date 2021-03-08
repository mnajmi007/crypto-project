def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0

    for c in letters:
        key[c] = letters[(cnt + n) % len(letters)]
        cnt += 1
    return key

def get_decrypt_key(key):
    dkey={}
    for c in key:
        dkey[key[c]] = c
    return dkey

def encrypt(key, messages):
    cipher = ""
    for c in messages:
        if c in key:
          cipher += key[c]
        else:
            cipher += c
    return cipher

key = generate_key(3)
messages="YOU ARE AWESOME"

cipher = encrypt(key, messages)
dkey = get_decrypt_key(key)
decrypt = encrypt(dkey, cipher)

print(messages)
print(cipher)
print(decrypt)

#brute force cipher
for i in range(26):
    dkey = generate_key(i)
    msg = encrypt(dkey, messages)
    print(msg)