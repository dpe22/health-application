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

    cur.execute("SELECT password FROM users where username =?",(username,))
    data = cur.fetchone()
    password = data[0]
    if len(data) == 0:
        print("Invalid Username")
        return False
    else: 
        if auth_hash == password:
            print("Logged in Successfully!")
            return True
        else:
            print("Incorrect Password\n")
            return False