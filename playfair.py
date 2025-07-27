def create_matrix(key):
    key = key.upper().replace('J', 'I').replace(' ','')
    char = []

    for c in key:
        if c.isalpha() and c not in char:
            char.append(c)
    
    for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if c not in char:
            char.append(c)
    
    matrix = []
    for i in range(5):
        matrix.append(char[i*5:(i+1)*5])
    return matrix

def find_position(matrix, char):
    char = char.upper().replace('J', 'I')
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i,j

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ','')
    text = ''.join(c for c in text if c.isalpha())

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text):
            if text[i] == text[i+1]:
                result += 'X'
            else:
                result += text[i+1]
                i+=1
        else:
            result += 'X'
        i+=1
    return result

def encrypt_pair(matrix , pair):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(matrix, pair):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def playfair_encryption(text, key):
    matrix = create_matrix(key)
    text = prepare_text(text)

    result = ""
    for i in range(0, len(text), 2):
        result += encrypt_pair(matrix, text[i:i+2])
    return result

def playfair_decryption(text, key):
    matrix = create_matrix(key)

    result = ""
    for i in range(0, len(text), 2):
        result += decrypt_pair(matrix, text[i:i+2])
    return result

while True:
    print("Select an option: ")
    print("1. Encrypt")
    print("2. Decrypt") 
    print("3. Exit")
    
    choice = input("Choose (1-3): ")
    
    if choice == '1':
        key = input("Enter key: ")
        text = input("Enter text: ")
        encrypted = playfair_encryption(text, key)
        print(f"Encrypted: {encrypted}")
        
    elif choice == '2':
        key = input("Enter key: ")
        text = input("Enter cipher text: ")
        decrypted = playfair_decryption(text, key)
        if 'x' in decrypted.lower():
            decrypted = decrypted.replace('X', '')
        print(f"Decrypted: {decrypted.lower()}")

        if 'i' in decrypted.lower():
            print("If actual i exist: ",decrypted.lower())
            print("If actually j exist: ",decrypted.lower().replace('i','j'))
        
        
    elif choice == '3':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice!")
        continue
