import hashlib
import getpass
import sqlite3
import new_user

def register():
    App = new_user.NewUser()
    App.run()

def login():
    username = input("Enter username: ")
    pwd = getpass.getpass("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    con = sqlite3.connect('users.db')
    cur = con.cursor()

    [stored_username, stored_pwd] = cur.execute("SELECT username, password FROM users where username =?",(username,))


    if username == stored_username:
        if auth_hash == stored_pwd:
            print("Logged in Successfully!")
        else:
            print("Incorrect Password")
    else:
         print("Invalid Username\n")
         print()
         print("\n ******************************************************** \n              Welcome to dpe22's Health App! \n                 Type ? to list commands \n ******************************************************** \n ")