# source tutorial to build a cmd line shell in python : https://code-maven.com/interactive-shell-with-cmd-in-python
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6
# code modified by dpe22

from cmd import Cmd
import hashlib

def signup():
    
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    
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

def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully!")
    else:
         print("Login failed! \n")

class MyPrompt(Cmd):
  prompt = '>>>>  '
  intro = "\n ******************************************************** \n              Welcome to dpe22's Health App! \n                 Type ? to list commands \n ******************************************************** \n "
  
  def do_exit(self, inp): 
    '''exit health-app.'''
    print("\nGoodbye!")
    print()
    return True
  
  def help_exit(self):
    print('exit health-app with x, q, or ctrl-z')
    print()
    
  def do_login(self, inp):
    sub_cmd = login()
    sub_cmd.cmdloop()

  def help_login(self):
    print("please provide a registered email and password to log in to Health App")
  
  def default(self, inp): 
    if inp == 'x' or inp == 'q':
      return self.do_exit(inp)
    
    print("Default: {}".format(inp))
    print()
    
  do_EOF = do_exit
  help_EOF = help_exit
  
if __name__ == '__main__':
  MyPrompt().cmdloop()
