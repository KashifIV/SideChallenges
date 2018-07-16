import sys
import tkinter
import pyodbc 
from tkinter  import *

# Initialize Global Variables
indexID = 1
params = ['ID', 'Student_Name', 'Hours_bought', 'First_class', 'Grade', 'Subject1', 'Subject2', 'Subject3','Hours_of_Attendance', 'Days_of_Attendance', 'Comments']
table = "StudentDatabase"

class Form: 
    '''
        General superclass for all Additional pages with the exception of the main menu
    '''
    def __init__(self, root, name, main): 
        self.root = root
        self.main = main
        self.name = name
        self.win = Frame(root)
    def CreateButtons(self): 
        self.MainTitle = Label(self.win, text = "This Section is Unimplemented")
        self.MainTitle.pack(side = TOP)
    def ShowMenu(self): 
        self.win.pack()
    def HideMenu(self): 
        self.win.pack_forget()
    def Back(self): 
        self.HideMenu()
        self.main.ShowMenu()

class ModifyComponent(Form):
    '''
        Allow for the modification of Records with the Exception
        of binding Attributes: ID & Name
    '''
    def __init__(self,root,name,main):
        Form.__init__(self,root,name,main)
        self.CreateButtons()
    def CreateButtons(self):
        self.input = Entry(self.win)
        self.prompt = Label(self.win, text = "Input the ID or Student Name whom you wish to modify.")
        self.ModifyButton = Button(self.win, text = "Modify", command = self.ModifyPerson)
        self.input.pack()
        self.prompt.pack()
        self.ModifyButton.pack()
        self.BackButton = Button(self.win, text = "Back", command = self.Back )
        self.BackButton.pack()
    def ModifyPerson(self):
        if not FindPerson(self.input.get()):
            self.prompt.config(text = "Error, Please Try Again")
        else: 
            self.prompt.config(text = "Enter Information that you'd like to Change & Click Modify Again")
            
            Information = ["Student Name", "Hours Bought", "First Class (MM/DD/YYYY)", "Grade", "Subject 1", "Subject 2",
                         "Subject 3", "Days of Attendance", "Hours of Attendance", "Comments"]
            InformationLabels = []
            self.EntryValues = []
            self.EntryValues.append(Entry(self.win))
            for i in range(1,len(Information)):
                InformationLabels = Label(self.win, text = Information[i])
                InformationLabels.pack()
                temp = Entry(self.win)
                self.EntryValues.append(temp)
                self.EntryValues[i].pack()
            self.ModifyButton.config(command = self.SendData)
    def SendData(self):
        values = []
        for i in self.EntryValues:
            values.append(i.get())
        if (ManipulateData(values, self.input.get())):
            self.prompt.config(text = "Success!")
class DeleteComponet(Form):
    '''
        Delete a Record From the Database
    '''
    def __init__(self, root, name, main):
        Form.__init__(self, root, name, main)
        self.CreateButtons()
    def CreateButtons(self): 
        self.input = Entry(self.win)
        self.prompt = Label(self.win, text = "Input the ID or Student Name whom you wish to remove.")
        self.DeleteButton = Button(self.win, text = "Delete", command = self.DeletePerson)
        self.input.pack()
        self.prompt.pack()
        self.DeleteButton.pack()
        self.BackButton = Button(self.win, text = "Back", command = self.Back )
        self.BackButton.pack()
    def DeletePerson(self):
        if DeleteData(self.input.get()):
            self.prompt.config(text = "Successfully Deleted")
        else: 
            self.prompt.config(text = "Failed, please try again")

class AddComponent(Form):
    '''
        Add a Record to the Database
    '''
    def __init__(self, root, name, main):
        Form.__init__(self, root, name, main)
        self.CreateButtons() 
    def CreateButtons(self):
        self.MainTitle = Label(self.win, text = "Please Enter the Required Information")
        self.MainTitle.pack(side = TOP)
        Information = ["Student Name", "Hours Bought", "First Class (MM/DD/YYYY)", "Grade", "Subject 1", "Subject 2",
                       "Subject 3", "Days of Attendance", "Hours of Attendance", "Comments"]
        InformationLabels = []
        self.EntryValues = []
        for i in range(len(Information)):
            InformationLabels = Label(self.win, text = Information[i])
            InformationLabels.pack()
            temp = Entry(self.win)
            self.EntryValues.append(temp)
            self.EntryValues[i].pack()
        self.AddButton = Button(self.win, text = "Add Record", command = self.AddPerson)
        self.BackButton = Button(self.win, text = "Back", command = self.Back )
        self.AddButton.pack() 
        self.BackButton.pack()
    def CheckValid(self):
        return True
    def AddPerson(self):
        values = []
        for i in self.EntryValues:
           values.append(i.get())
        if not AddData(values): 
            self.MainTitle.config(text = "1 or more fields is incorrect")
        else:
            self.MainTitle.config(text = "Successfully Added")


class Window: 
    '''
        Main menu and core functionality
    '''
    def __init__(self, root, name): 
        self.root = root
        root.geometry("600x500")
        root.pack_propagate(0)
        root.title(name)
        self.MainMenu = Frame(root)
        self.CreateMainButtons()
        self.MainMenu.pack()
    def HideMenu(self): 
        self.MainMenu.pack_forget()
    def ShowMenu(self): 
        self.MainMenu.pack()
    def CreateMainButtons(self): 
        self.MainTitle = Label(self.MainMenu, text = "Please Select an Operation")
        self.MainTitle.pack(side = TOP)
        self.addButton = Button(self.MainMenu, text="Add a Record", command=self.AddRecordDisplay)
        self.addButton.pack(side = LEFT) 
        self.modifyButton = Button(self.MainMenu, text = "Modify a Record", command = self.ModifyRecordDisplay)
        self.modifyButton.pack(side = LEFT)
        self.removeButton = Button(self.MainMenu, text = "Remove a Record", command = self.RemoveRecordDisplay)
        self.removeButton.pack(side = LEFT) 
        self.viewTable = Button(self.MainMenu, text = "View Table", command = self.CreateTable)
        self.viewTable.pack(side = LEFT)
        self.CreateTable()
    def CreateTable(self):
        self.top = Toplevel(self.MainMenu)
        table = GetTable()
        for r in range(len(table)):
            for i in range(len(table[r])):
                v = Label(self.top, text = table[r][i], borderwidth = 4).grid(row = r, column = i)
    def AddRecordDisplay(self):
        self.AddDisplay = AddComponent(self.root, "Add Record", self)
        self.HideMenu()
        self.AddDisplay.ShowMenu()
    def ModifyRecordDisplay(self): 
        self.ModifyDisplay = ModifyComponent(self.root, "Modify Recrod", self)
        self.HideMenu()
        self.ModifyDisplay.ShowMenu()
    def RemoveRecordDisplay(self): 
        self.DeleteDisplay = DeleteComponet(self.root, "Delete Record", self)
        self.HideMenu()
        self.DeleteDisplay.ShowMenu()

#  CONNECT TO THE DATABASE
connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\kashi\Documents\Database1.accdb;')
cursor = connection.cursor()
#FIND AN ID THAT CAN BE USED FOR NEW RECORDS
cursor.execute(("SELECT COUNT(*) from " + table))
indexID = cursor.fetchone()[0]+1
if (indexID == None):
    indexID = 0
indexID += 1
print(indexID)

def ClearTable(cursor):
    cursor.execute('delete * from ' + table)
def GetTable():
    sql = "Select * FROM " + table
    cursor.execute(sql)
    return cursor.fetchall()
def FindPerson(value):
        try:
            if value.isdigit:
                sql = "SELECT ID  FROM " + table + " WHERE ID = ?"
                cursor.execute(sql, value)
            else: 
                sql = "SELECT Student_Name " + table + " WHERE Student_Name LIKE " + value
                cursor.execute(sql)
            return True
        except:
            return False

def AddData(DataEntry):
    try:
        DataEntry = [indexID] + DataEntry
        DataEntry[3] += ' 1:00:00 PM'
        sql = """
        INSERT INTO StudentDatabase (ID, Student_Name, Hours_bought, First_class, Grade, Subject1, Subject2, Subject3, Hours_of_Attendance, Days_of_Attendance, Comments)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """ 
        cursor.execute(sql, DataEntry)
        cursor.commit()
        return True
    except:
        return False
def DeleteData(value): 
    try:
        if value.isdigit():
            cursor.execute('DELETE FROM '+table+ ' WHERE ID = ?', value)
        else:
            cursor.execute('DELETE FROM '+ table +' WHERE Student_Name = (?)', value)
        cursor.commit()
        return True
    except:
        return False
def ManipulateData(values, name):  
    #sql = "UPDATE StudentDatabase SET Grade = 100 WHERE ID = 2"
    for i in range(len(values)): 
        if not values[i] == "": 
            sql = "UPDATE " + table + " SET " + params[i+1] + " = " + values[i] + " WHERE " 
            if not name.isdigit():
                sql += "Student_Name = (?)" 
            else: 
                sql+= "ID = ?"
            print(sql)
            cursor.execute(sql,name)
            cursor.commit()
            
app = tkinter.Tk()
win = Window(app, "Databasing")


app.mainloop()
