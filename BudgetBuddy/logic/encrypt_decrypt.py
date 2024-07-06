from cryptography.fernet import Fernet
 
class encrypt:
    def __init__(self):
        # Replace 'your_password' with your chosen password
        key = Fernet.generate_key()
        with open("key.key","wb") as k:
            k.write(key)
    def encrypt_text(self,text, key):
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(text.encode())
        return encrypted_text
    def write_encrypted_file(self,file_path, encrypted_text):
        with open(file_path, 'wb') as file:
            file.write(encrypted_text)
    
class decrypt:
    def decrypt_text(self,encrypted_text, key):
        cipher_suite = Fernet(key)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        return decrypted_text

    def read_encrypted_file(self,file_path):
        with open(file_path, 'rb') as file:
            encrypted_text = file.read()
        return encrypted_text
    def get_key(self):
        with open ("key.key" , "rb") as k:
            key = k.read()
        return key