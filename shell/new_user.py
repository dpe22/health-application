import npyscreen
import sqlite3
import hashlib
import getpass

class NewUser(npyscreen.NPSApp):
    def main(self):
        pwd = getpass.getpass("Enter new password: ")
        conf_pwd = getpass.getpass("\nConfirm new password: ")

        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

        else:
            print("passwords must match - please try again")
            return

        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Add a new user to Health App",)
        un = F.add(npyscreen.TitleText, name = "Username:",)
        fn  = F.add(npyscreen.TitleText, name = "First Name:",)
        ln = F.add(npyscreen.TitleText, name = "Last Name:",)
        em = F.add(npyscreen.TitleText, name="Email:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, name="Select role(s) using 'x':",
                values = ["Patient","Relative","Practitioner","Administrator","Device Developer"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()


        con = sqlite3.connect('users.db')
        cur = con.cursor()

        # Create table if none exist
        cur.execute('''CREATE TABLE if not exists users
               (firstName text, lastName text, role text, email text, username text, password text, createdOn date)''')

        # Insert a row of data
        cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)",(str(fn),str(ln),str(ms2),str(em),str(un),str(hash1),str(dt)))

        # Save (commit) the changes
        con.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        con.close()

        # print(ms2.get_selected_objects())
        print("new user successfully added - thank you")

if __name__ == "__main__":
    App = NewUser()
    App.run()