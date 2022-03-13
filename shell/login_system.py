import hashlib
import getpass

def signup():
    
    email = input("Enter email address: ")
    pwd = getpass.getpass("Enter password: ")
    conf_pwd = getpass.getpass("Confirm password: ")
    
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully!")
        return

    else:
        print("Password is not same as above! \n")
        print()
        print("\n ******************************************************** \n              Welcome to dpe22's Health App! \n                 Type ? to list commands \n ******************************************************** \n ")
  

def login():
    email = input("Enter email: ")
    pwd = getpass.getpass("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully!")
    else:
         print("Login failed! \n")
         print()
         print("\n ******************************************************** \n              Welcome to dpe22's Health App! \n                 Type ? to list commands \n ******************************************************** \n ")