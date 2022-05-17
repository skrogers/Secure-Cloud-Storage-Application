from cryptography.fernet import Fernet
import eel
import io


#Fernet is the encryption algorithm used

#Function which generates our key (AES)
@eel.expose

def keyGen():       #Used for key generation
    
    key = Fernet.generate_key()     #key generation for encryption and decryption
    file = open('Keys/key.key', 'wb')       #wb - write binary
    
    file.write(key)     #store key in key.key file
    file.close()
    
    print("\nKey Created.\n")       #Output in Console


#Function which reads the key 
def keyRead():
    
    try:    #one key exists
        file = open('Keys/key.key', 'rb')   #key.key filein read binary mode
        key = file.read()       #reads the key
        
        file.close()
        return key
    
    except FileNotFoundError:
        #If key does not exists a new one is created.
        print("No Key exists, a new one has just been created.")
        
        keyGen()
        keyRead()


#Function to encrypt files using the key
@eel.expose
def encrypt(fileName):
    
    Key = keyRead()     #stores key in Key
    
    with open("Files/"+ fileName, "rb") as f:
        data = f.read()     #file data gets stored in data
    
    fernet = Fernet(Key)        #fernet instance
    
    encrypted = fernet.encrypt(data)        #encrypting the file data

    with open("Files/"+ fileName, "wb") as f:
        f.write(encrypted)      #writing encrypted data in the file
    print("\n File Encrypted.\n")


#Function to decrypt files using the key

@eel.expose
def decrypt(fileName):
    Key = keyRead()     #read key
    with open("Downloads/"+ fileName, "rb") as f:
        data = f.read()     #reading encrypted data
    
    fernet = Fernet(Key)        #instance
    
    decrypted = fernet.decrypt(data)    #decrypting data to original

    with open("Downloads/"+ fileName, "wb") as f:
        f.write(decrypted)