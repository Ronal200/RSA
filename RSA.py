import sympy
import random

def generate_prime(bits):
    while True:
        prime = sympy.randprime(2**(bits-1), 2**bits)
        if prime.bit_length() == bits:
            return prime

def generate_keypair(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    
    n = p * q
    phi = (p - 1) * (q - 1)

    e = sympy.randprime(2, phi)
    while sympy.gcd(e, phi) != 1:
        e = sympy.randprime(2, phi)
    
    d = sympy.mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

if __name__ == "__main__":
    # Generación de claves
    public_key, private_key = generate_keypair(50)

    # Mostrar claves
    print("Clave pública:", public_key)
    print("Clave privada:", private_key)

    # Encriptación
    mensaje = "Hola Mundo"
    cifrado = encrypt(mensaje, public_key)
    print("Mensaje cifrado:", cifrado)

    # Desencriptación
    descifrado = decrypt(cifrado, private_key)
    print("Mensaje descifrado:", descifrado)
