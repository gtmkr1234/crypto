def encrypt(planeText: str, key: int):
    res = ""
    for i in planeText:
        res += chr((ord(i)+key)%256) 
    return res

def decrypyt(cipherText: str, key:int):
    res = ""
    for i in cipherText:
        txt = ord(i)-key
        res += chr((txt)%256)
    return res

def bruteforce(planeText: str, cipherText: str):
    return ord(cipherText[0])-ord(planeText[0])



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
        cipher = encrypt(pt,key)
        print(cipher)

    if option == 2:
        ct = input("Enter the cipherText")
        key = int(input("Enter the key"))
        plane = decrypyt(ct,key)
        print(plane)

    if option == 3:
        pt = input("Enter the plane text")
        ct = input("Enter the cipher text")
        print(bruteforce(pt,ct))

    if option == 0:
        break

    else:
        continue