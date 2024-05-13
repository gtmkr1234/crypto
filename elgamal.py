def primitive_root(n):
    a = n - 1
    lst = [[0] * (a) for i in range(a)]
    # print(lst)
    for i in range(a):
        for j in range(a):
            lst[i][j] = ((i + 1) ** (j + 1)) % n
    primitive = []
    for i in range(a):
        found = False
        for j in range(a - 1):
            if lst[i][j] == 1:
                found = True
                break
        if not found:
            if lst[i][a - 1] == 1:
                primitive.append(i + 1)
    if len(primitive) == 0:
        return None
    else:
        return primitive


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime_list(n):
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


def generate_keys(p, d, e1):
    e2 = pow(e1, d) % p
    public_keys = [e1, e2, p]
    private_key = d
    return public_keys, private_key


def encrypt(public_keys, plain_text,r):
    e1 = public_keys[0]
    e2 = public_keys[1]
    p = public_keys[2]
    ptarray = [ord(i) - 97 for i in plain_text]
    c1 = pow(e1, r) % p
    c2 = [(i * pow(e2, r)) % p for i in ptarray]
    return c1, c2, ptarray

def decrypt(d, p, c1, c2):
    plain_text = [(i*pow(pow(c1,d),p-1-d))%p for i in c2]
    return plain_text


if __name__ == '__main__':
    n = int(input("Enter the range for prime numbers: "))
    prime_list = generate_prime_list(n)
    for index, keypair in enumerate(prime_list):
        print(f"{index + 1} : {keypair}")
    ip = int(input("Enter the choice for the prime number: "))
    p = prime_list[ip - 1]
    r = int(input("Enter choice for the value of r where r is in the range of 2 to p-2"))
    d = int(input("Enter the choice for d where 1<=d<=p-2: "))
    roots = primitive_root(p)
    if roots is not None:
        for index, keypair in enumerate(roots):
            print(f"{index + 1} : {keypair}")
    else:
        print("No primitive roots found")
        exit()
    ip2 = int(input("Enter the choice for the primitive root: "))
    e1 = roots[ip2 - 1]
    public_keys, private_keys = generate_keys(p, d, e1)

    while (True):
        plain_text = input("Enter the plaintext you want to encrypt: ")
        c1, c2, ptarray = encrypt(public_keys, plain_text,r)
        print(f"value of c1 : {c1}")
        print(f"value of c2: {c2}")
        print(ptarray)
        print(decrypt(d,p,c1,c2))