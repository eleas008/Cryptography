def viginere_encryption(pt,key):
    key_stream_string = ""

    for i in range(len(pt.replace(" ",""))):
        key_stream_string+=key[i%len(key)]
    
    print(key_stream_string)
    
    result = ""
    j=0
    for i in range(len(pt)):
        if pt[i] == " ":
            result+=" "
            continue
        p = ord(pt[i])-97
        k = ord(key_stream_string[j])-97
        j+=1
        result += chr(((p+k)%26)+65)
    
    return result


def viginere_decryption(ct,key):
    key_stream_string = ""

    for i in range(len(ct.replace(" ",""))):
        key_stream_string += key[i%len(key)]
        
    result = ""
    j = 0
    for i in range(len(ct)):
        c = ord(ct[i])-65
        k = ord(key_stream_string[j]) - 65
        j+=1
        result += chr((c-k)%26 + 97)
    
    return result


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
        
        
        
