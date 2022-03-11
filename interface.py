# source tutorial to build a cmd line shell in python : https://code-maven.com/interactive-shell-with-cmd-in-python
# code modified by dpe22

from cmd import Cmd

class MyPrompt(Cmd):
  prompt = 'health-app> '
  intro = "Welcome to Health App! Type ? to list commands"
  
  def do_exit(self, inp): 
    '''exit health-app.'''
    print("Goodbye")
    return True
  
  def help_exit(self):
    print('exit health-app with x, q, or ctrl-z')
    
  def do_add(self, inp):
    print("adding '{}'".format(inp))
    
  def help_add(self):
    print("add a new entry to the system.")
  
  def default(self, inp): 
    if inp == 'x' or inp == 'q':
      return self.do_exit(inp)
    
    print("Default: {}".format(inp))
    
  do_EOF = do_exit
  help_EOF = help_exit
  
if __name__ == '__main__':
  MyPrompt().cmdloop()
