def caeser_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            p = ord(char) - base
            c = (p*shift) % 26
            result += chr(base + c)
        else:
            result += char
    return result.upper()

def caeser_cipher_decrypt(text, shift):
    r1 = 26
    r2 = shift
    t1 = 0
    t2 = 1
    while r2!=0:
        q = r1 // r2
        r = r1 % r2
        r1 = r2
        r2 = r

        t = t1 - q * t2
        t1 = t2 
        t2 = t
    
    if r1 != 1:
        return "Shift value is not coprime with 26, decryption not possible."


    shift_inverse = t1 % 26

    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A')
            c = ord(char)- base
            p = (c * shift_inverse) % 26
            result += chr(base + p)
        else:
            result += char
    return result.lower()


if __name__ == "__main__":

    while True:
    
        print("Select an option: ")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Unknown key value to decrypt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            pt = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Encrypted text: ", caeser_cipher_encrypt(pt.lower(), shift))
        elif choice == '2':
            ct = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            print("Decrypted text: ", caeser_cipher_decrypt(ct.upper(), shift))

        elif choice == '3':
            ct = input("Enter the text to decrypt: ")
            for shift in range(1,26):
                print(f"Shift {shift}: {caeser_cipher_decrypt(ct.upper(), shift)}")
        
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
            continue

    

    
