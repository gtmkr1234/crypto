def vignere_encrypt(planetext:str, key:str):
    res = ""
    for i in range(len(planetext)):
        res += chr(ord('a')+(ord(planetext[i])-2*ord('a')+ord(key[i%len(key)]))%26)
    return res


def vignere_decrypt(ciphertext:str, key:str):
    res = ""
    for i in range(len(ciphertext)):
        res += chr(ord('a')+(ord(ciphertext[i])- ord(key[i%len(key)]))%26)
    return res


while(True):
    print("""
            press 1 for Encryption
            press 2 for Decryption 
            press 0 to quit
            :
""")
    ip = int(input())
    if ip==1:
        planetext = input("Enter the planetext: ")
        key = input("Enter the key:")
        print("The encrypted text is : "+vignere_encrypt(planetext, key))

    if ip==2:
        cipher = input("Enter the ciphertext:")
        key = input("Enter the key:")
        print("Decrypted text is : "+vignere_decrypt(cipher,key))
    
    if ip==0:
        break

    else:
        continue
