def viginere_encryption(pt,key):
    key_stream_string = ""

    for i in range(len(pt)):
        if (i<len(pt)):
            key_stream_string+=key[i%len(key)]
    
    result = ""
    for i in range(len(pt)):
        p = ord(pt[i])-ord('a')
        k = ord(key_stream_string[i])-ord('a')
        result += chr(((p+k)%26)+ord('a'))
    
    return result.upper()


def viginere_decryption(ct,key):
    key_stream_string = ""

    for i in range(len(ct)):
        if (i<len(ct)):
            key_stream_string += key[i%len(key)]
        
    result = ""

    for i in range(len(ct)):
        c = ord(ct[i])-ord('A')
        k = ord(key_stream_string[i]) - ord('A')
        result += chr((c-k)%26 + ord('A'))
    
    return result.lower()


if __name__ == "__main__":
    while True:
        print("Select an option")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        c = input("Select a choice: ")

        if c == '1':
            pt = input("Enter the plain text: ").lower()
            key = input("Enter key string: ").lower()
            print("Encrypted text: ",viginere_encryption(pt,key))
        
        elif c == '2':
            ct = input("Enter the encrypted text: ")
            key = input("Enter key string: ").upper()
            print("Decrypted text: ",viginere_decryption(ct,key))
        
        elif c == '3':
            print("Exiting...")
            break

        else:
            print("You choose a wrong option.Please select right choice")
            continue
        
        
        