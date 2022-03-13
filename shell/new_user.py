import npyscreen

class NewUser(npyscreen.NPSApp):
    def add_user(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Add a new user to Health App",)
        fn  = F.add(npyscreen.TitleText, name = "First Name:",)
        ln = F.add(npyscreen.TitleText, name = "Last Name:",)
        em = F.add(npyscreen.TitleText, name="Email:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date:")
        ms2= F.add(npyscreen.TitleMultiSelect, max_height =-2, name="Select role(s) using 'x':",
                values = ["Patient","Relative","Practitioner","Administrator","Device Developer"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        # print(ms2.get_selected_objects())
        print("Thank you!")
        return fn,ln,em,dt,ms2

if __name__ == "__main__":
    App = NewUser()
    App.run()