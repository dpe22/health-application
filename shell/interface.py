# source tutorial to build a cmd line shell in python : https://code-maven.com/interactive-shell-with-cmd-in-python
# https://medium.com/@moinahmedbgbn/a-basic-login-system-with-python-746a64dc88d6
# code modified by dpe22

from cmd import Cmd
from login_system import *

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

  def do_signup(self, inp):
    sub_cmd = signup()
    #sub_cmd.cmdloop()

  def help_signup(self):
    print('create a new user account')
    print()
    
  def do_login(self, inp):
    sub_cmd = login()
    #sub_cmd.cmdloop()

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
