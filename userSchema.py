from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

class User:
    def __init__(self,uid,userName,isAdmin,email,password):
        self.name=userName
        self.uid=uid
        self.isAdmin=isAdmin
        self.email=email
        self.__password = fernet.encrypt(password.encode())

    def display(self):
        print("UID: ", self.uid)
        print("Name: ", self.name)
        print("Email: ", self.email)

    def getPassword(self):
        return fernet.decrypt(self.__password).decode()
