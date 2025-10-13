import math
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    
    return True

def calculate_phi(a,b):
    return (a-1)*(b-1)

def valid_e(a,phi_n):
    if a>1 and a<phi_n:
        return True
    return False

def find_d(n,a):
    r1 = n
    r2 = a
    t1 = 0
    t2 =1
    while r2!=0:
        q = r1//r2
        r = r1 % r2
        t=t1-q*t2
        r1=r2
        r2=r
        t1=t2
        t2=t
    
    if r1!= 1:
        return
    
    return t1

def  encryption(M,e,n):
    return (M**e)%n


def decryption(CM,d,n):
    return (CM**d)%n

if __name__ == '__main__':
    while True:
        print("Choose an option\n1. Continue\n2. Exit")
        C=int(input("Choose an option: "))
        if C==1:
            p = int(input("Enter the value of p: "))
            q = int(input("Enter the value of q: "))

            if p==q:
                print("p and q must not equal to each other")
                continue

            if not is_prime(p) or not is_prime(q):
                print("Please choose prime numbers.")
                continue
            
            print("Both numbers are prime")

            phi_n = calculate_phi(p,q)

            print("Phi_n: ",phi_n)

            e = int(input("Enter the value of Public Key:"))

            if not valid_e(e,phi_n):
                print("Choose valid public key")
                continue
            
            print("Choosen valid public key")

            d = find_d(phi_n,e)
            if d is None:
                print("They are not co-prime")
                continue
            print("Private Key: ",d)    

            while True:
                print("Choose an option\n1. Encryption\n2. Decryption\n3. Exit")
                c=int(input("Choose a number: "))
                if c == 1:
                    M = int(input("Enter the Message: "))
                    CM = encryption(M,e,p*q)
                    print("Encrypted Text: ",CM)
                elif c == 2:
                    CM = int(input("Enter the Cipher Message: "))
                    PM = decryption(CM,d,p*q)
                    print("Decrypted text: ",PM)
                elif c == 3:
                    break
                else:
                    continue
        elif C==2:
            break
        else:
            continue        
        

        


