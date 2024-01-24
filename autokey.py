def autokey_encrypt(plane: str, key: int):
    res = ""
    res += chr((ord(plane[0])+key)%256)
    for i in range(1,len(plane)):
        res+= chr((ord(plane[i])+ord(plane[i-1]))%256)
    return res

def autokey_decrypt(cipher: str, key: int):
    res = ""
    res += chr((ord(cipher[0])-key)%256) 
    for i in range(1,len(cipher)):
        res += chr((ord(cipher[i])-ord(res[-1]))%256)
    return res

def bruteforce(plane:str, cipher:str):
    return ord(cipher[0])-ord(plane[0])


while(True):
    print("""
    Press 1 for Encryption
    Press 2 for decryption
    Press 3 for bruteforce
    Press 0 to quit 
    """)
    option = int(input())
    if option == 1:
        pt = input("Enter the plane text")
        key = int(input("Enter the key"))
        cipher = autokey_encrypt(pt,key)
        print(cipher)

    if option == 2:
        ct = input("Enter the cipherText")
        key = int(input("Enter the key"))
        plane = autokey_decrypt(ct,key)
        print(plane)

    if option == 3:
        pt = input("Enter the plane text")
        ct = input("Enter the cipher text")
        print(bruteforce(pt,ct))

    if option == 0:
        break

    else:
        continue