import npyscreen
import sqlite3

class NewDevice(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        F  = npyscreen.Form(name = "Add a new device to Health App",)
        dn = F.add(npyscreen.TitleText, name = "Device Name:",)
        id  = F.add(npyscreen.TitleText, name = "Serial Number:")
        pid = F.add(npyscreen.TitleText, name="Assigned to Patient ID:")
        did = F.add(npyscreen.TitleText, name = "Assigned to Developer ID:")
        dt = F.add(npyscreen.TitleDateCombo, name = "Date Created:")
        ms = F.add(npyscreen.TitleSelectOne, max_height = 10, name="Select unit of measurement:",
                values = ["BPM", "Fahrenheit", "Celsius", "mmHg", "mg/dl", "inches", "kilograms"], scroll_exit=True)
        ms2= F.add(npyscreen.TitleSelectOne, max_height =-2, name="Select type of measurement:",
                values = ["Pulse","Temperature","Blood Pressure","Blood Sugar","Height","Weight"], scroll_exit=True)

        # This lets the user interact with the Form.
        F.edit()

        # Connect to local database SQLite3
        con = sqlite3.connect('devices.db')
        cur = con.cursor()

        # Create table if none exist
        cur.execute('''CREATE TABLE if not exists devices
               (deviceName text, serialNumber text, patientID text, developerID text, createdOn date, units text, measurement text)''')

        # Insert a row of data
        cur.execute("INSERT INTO devices VALUES (?,?,?,?,?,?,?)",(str(dn.value),str(id.value),str(pid.value),str(did.value),str(dt.value),str(ms),str(ms2.value)))

        # Save (commit) the changes
        con.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        con.close()

        # print(ms2.get_selected_objects())
        print("new device successfully added - thank you")

if __name__ == "__main__":
    App = NewDevice()
    App.run()