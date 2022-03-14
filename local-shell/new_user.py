import npyscreen
import sqlite3
import hashlib
import getpass

class NewUser(npyscreen.NPSApp):
    def main(self):
        # create a password
        pwd = getpass.getpass("Enter new password: ")
        conf_pwd = getpass.getpass("\nConfirm new password: ")

        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

        else:
            print("passwords must match - please try again")
            return

        # These lines create the new user form and populate it with widgets.
        F  = npyscreen.Form(name = "Add a new user to Health App",)
        un = F.add(npyscreen.TitleText, name = "Username:",)
        fn  = F.add(npyscreen.TitleText, name = "First Name:",)
        ln = F.add(npyscreen.TitleText, name = "Last Name:",)
        em = F.add(npyscreen.TitleText, name="Email:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, name="Select role(s) using 'x':",
                values = ["Patient","Relative","Practitioner","Administrator","Device Developer"], scroll_exit=True)

        # This lets the user interact with the form.
        F.edit()

        # connect to the local users database (sqlite3)
        con = sqlite3.connect('users.db')
        cur = con.cursor()

        # Create table if none exist
        cur.execute('''CREATE TABLE if not exists users
               (firstName text, lastName text, role text, email text, username text, password text, createdOn date)''')

        # Insert a row of data
        cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?)",(str(fn.value),str(ln.value),str(ms2.value),str(em.value),str(un.value),str(hash1),str(dt.value)))

        # Save (commit) the changes
        con.commit()

        # Close the connection
        con.close()

        # print(ms2.get_selected_objects())
        print("new user successfully added - thank you")

if __name__ == "__main__":
    App = NewUser()
    App.run()