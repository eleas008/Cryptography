import math
import numpy as np
import sympy as sp



def create_blocks(pt,n):
    while len(pt)%n !=0:
        pt+='x'
    blocks = [pt[i:i+n] for i in range(0, len(pt), n)]

    return blocks

def create_inverse_matrix(key_m,m):
    try:
        inv_key = sp.Matrix(key_m).inv_mod(m)
        return np.array(inv_key).astype(int)
    except:
        raise ValueError("Matrix is not invertible under modulo 26")
    
def create_key_matrix(key,n):
    matrix = []
    k = 0
    for i in range(n):
        row = []
        for j in range(n):
            if k < len(key):
                row.append(ord(key[k])-ord('A'))
                k+=1
        matrix.append(row)
    
    return np.array(matrix)

def hill_cipher_encryption(blocks,key_m):
    matrix = []
    for block in blocks:
        row = [ord(c)-ord('a') for c in block]
        matrix.append(row)
    matrix = np.array(matrix)

    
    encrypted_text = ""
    for row in matrix:
        result = np.dot(row,key_m)%26
        for val in result.flatten():
            encrypted_text += chr(int(val)+ord('A'))
    
    return encrypted_text

def hill_cipher_decryption(blocks,key_im):
    matrix = []
    for block in blocks:
        row = [ord(c)-ord('A') for c in block]  
        matrix.append(row)
    matrix = np.array(matrix)

    decrypted_text = ""
    for row in matrix:
        result = np.dot(row,key_im)%26
        for val in result.flatten():
            decrypted_text += chr(int(val)+ord('a'))
    
    return decrypted_text

if __name__ == '__main__':
    while True:
        print("Choose an option")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        c = int(input("Enter a choice: "))

        if c == 1:

            pt = input("Enter the plain text: ")
            key = input("Enter the key: ")

            n = int(math.sqrt(len(key)))

            if n*n != len(key):
                print("Length of key must be perfect square")
                continue
            
            else:
                blocks = create_blocks(pt,n)
                key_m = create_key_matrix(key,n)
                encrypted_text = hill_cipher_encryption(blocks,key_m)
                print("Encrypted text: ",encrypted_text)
        
        elif c == 2:

            ct = input("Enter cipher text: ")
            key = input("Enter the key: ")

            n = int(math.sqrt(len(key)))

            if n*n != len(key):
                print("Length of key must be perfect square")
            else:
                blocks = create_blocks(ct,n)  
                key_m = create_key_matrix(key,n)
                try:
                    key_im = create_inverse_matrix(key_m,26)
                except ValueError:
                    print("Key matrix is not invertible under modulo 26")
                    continue
                decrypted_text = hill_cipher_decryption(blocks,key_im)
                print("Decrypted text: ",decrypted_text)
        
        elif c == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice!")
            continue

