# source tutorial to build a cmd line shell in python : https://code-maven.com/interactive-shell-with-cmd-in-python
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6
# code modified by dpe22

from cmd import Cmd
from login_system import *
import sys

class SignedIn(Cmd):
  prompt = '>>>>  '
  intro = "\n ******************************************************** \n       Welcome Darren!   Type ? to list commands \n ******************************************************** \n "
  
  def do_exit(self, inp): 
    '''exit health-app.'''
    sys.exit("\nGoodbye!\n")
  
  def help_exit(self):
    print('exit health-app with x, q, or ctrl-z')
    print()

  def do_signout(self, inp):
    sub_cmd = SignedOut()
    sub_cmd.cmdloop()

  def help_signout(self):
    print('log off this user account')
    print()
  
  def default(self, inp): 
    if inp == 'x' or inp == 'q':
      return self.do_exit(inp)
    
    print("Command not recognized: {}\n".format(inp))
    print("Type ? to list commands")
    
  do_EOF = do_exit
  help_EOF = help_exit

class SignedOut(Cmd):
  prompt = '>>>>  '
  intro = "\n ******************************************************** \n\n              Welcome to dpe22's Health App! \n\n ******************************************************** \n\nType ? to list commands"
  
  def do_exit(self, inp): 
    '''exit health-app.'''
    sys.exit("\nGoodbye!\n")
  
  def help_exit(self):
    print('exit health-app with x, q, or ctrl-z')
    print()

  def do_register(self, inp):
    sub_cmd = signup()

  def help_register(self):
    print('create a new user account')
    print()
    
  def do_login(self, inp):
    sub_cmd = login()
    sub_cmd = SignedIn()
    sub_cmd.cmdloop()


  def help_login(self):
    print("please provide a registered email and password to log in to Health App")
  
  def default(self, inp): 
    if inp == 'x' or inp == 'q':
      return self.do_exit(inp)
    
    print("Command not recognized: {}\n".format(inp))
    print("Type ? to list commands")
    
  do_EOF = do_exit
  help_EOF = help_exit
  
if __name__ == '__main__':
  SignedOut().cmdloop()
