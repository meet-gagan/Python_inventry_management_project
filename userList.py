import re

from  packages.userSchema import User

regex = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$$"

class UserList:

    users = []

    def signup(self):
        name = input("Enter your name : ").lower()

        email = input("Enter your Email : ").lower()

        while (not re.search(regex, email)):
            print("Invalid email address, please try again")
            email = input("Enter your Email : ").lower()

        password = input("Enter a password : ")
        isAdmin = int(input("Are you 1.admin or 0.user : "))

        while (not (isAdmin == 1 or isAdmin == 0)):
            print("Invalid input, please try again")
            isAdmin = int(input("Are you 1.admin or 0.user : "))

        uid = len(UserList.users) + 1

        TempUser=User(uid,name,isAdmin, email, password)
        UserList.users.append(TempUser)
        print("User created successfully!!!")
        return 1

    def signin(self):
        name=input("Enter your name : ")
        password=input("Enter your password : ")
        for i in UserList.users:
            print(i.name, i.getPassword())
            if i.name == name and i.getPassword() == password:
                print("Welcome!!!")
                return i
        else:
            print("Incorrect Username and Password, Sign Up if you dont have an account")
            return 0
    
    def displayUsers(self):
        if len(UserList.users):
            for i in UserList.users:
                i.display()
        else:
            print("No Users to display")
