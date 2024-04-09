def generate_keyset(modulo,size):
    keyset = []
    for i in range(1, size+1):
        if i % 2 != 0:
            inverse = pow(i, -1, modulo)
            keyset.append((i, inverse))
    return keyset


def multiplicative_encrypt(plaintext, key, modulo):
    ciphertext = ""
    for char in plaintext:
        encrypted_char = (ord(char) * key) % modulo
        ciphertext += chr(encrypted_char)
    return ciphertext


def multiplicative_decrypt(ciphertext, key, modulo):
    plaintext = ""
    for char in ciphertext:
        decrypted_char = (ord(char) * key) % modulo
        plaintext += chr(decrypted_char)
    return plaintext


if __name__ == '__main__':
    modulo = 256

    print("Enter the size of keyset:")
    keyset_size = int(input())
    keyset = generate_keyset(modulo, keyset_size)

    print("Enter the choice of key:")
    for index, key_pair in enumerate(keyset):
        print(f"{index + 1}: Key = {key_pair[0]}, Inverse = {key_pair[1]}")

    key_index = int(input()) - 1
    if 0 <= key_index < len(keyset):
        key, inverse_key = keyset[key_index]
    else:
        print("Invalid key index")
        exit()

    while True:
        print("""Press 1 to encrypt
        Press 2 to decrypt
        Press 3 to exit""")
        choice = int(input())

        if choice == 1:
            plaintext = input("Enter plaintext: ")
            ciphertext = multiplicative_encrypt(plaintext, key, modulo)
            print("Ciphertext:", ciphertext)

        elif choice == 2:
            ciphertext = input("Enter ciphertext: ")
            plaintext = multiplicative_decrypt(ciphertext, inverse_key, modulo)
            print("Plaintext:", plaintext)

        elif choice == 3:
            break

        else:
            print("Invalid choice")
