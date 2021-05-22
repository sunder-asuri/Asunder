from tkinter import *
import PIL
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
import menus


def validate():
    global login, name, passw, getLoginId, getName, getLoginID

    login = int(id.get())
    name = userName.get()
    passw = password.get()
    empTable = "employee"
    sqlLoginID = "select empid from " + empTable + " where password = '" + passw + "'"
    sqlName = "select name from " + empTable + " where password = '" + passw + "'"
    try:
        cur.execute(sqlLoginID)
        records = cur.fetchall()
        for i in records:
            getLoginID = i[0]
        cur.execute(sqlName)
        records = cur.fetchall()
        for i in records:
            getName = i[0]

        if getLoginID == login and getName == name:
            messagebox.showinfo("SUCCESS", "You have successfully logged in")

            menus.options()

        else:
            messagebox.showerror("Failure", "Can't log in, check your credentials")
    except:
        messagebox.showinfo("FAILED", "Please check your credentials")

    print(login)
    #print(login is getLoginId)
    #print(type(getLoginID))
    print(name)
    #print(getName)
    #print(records[0])
    #print(getLoginID == login)

    #print(getName == name)



# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

# Add your own database name and password here to reflect in the code
# mypass = "sunder9900$"
mydatabase = "libb"

con = mysql.connector.connect(host="localhost", user="sunder", password="sunder9900$", database=mydatabase)
cur = con.cursor()
global login,name,passw,getLoginId,getName

#window
root = Tk()
root.title('libraray')
root.maxsize(width=900, height=900)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same = True
n = 0.25

# Adding a background image
background_image = PIL.Image.open("lib.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="#12a4d9")
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \nData Library", bg='black', fg='white',
                             font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root, bg='black')
labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

#id
lb1 = Label(labelFrame, text="ID : ", bg='black', fg='white')
lb1.place(relx=0.05, rely=0.2, relheight=0.08)

id = Entry(labelFrame)
id.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

#username
lb2 = Label(labelFrame, text="username : ", bg='black', fg='white')
lb2.place(relx=0.05, rely=0.35, relheight=0.08)

userName = Entry(labelFrame)
userName.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)



#password
lb3 = Label(labelFrame, text="password : ", bg='black', fg='white')
lb3.place(relx=0.05, rely=0.50, relheight=0.08)

password = Entry(labelFrame, show = '*')
password.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

#login
LoginBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command =validate)
LoginBtn.place(relx=0.28, rely=0.7, relwidth=0.18, relheight=0.08)

changeOnHover(LoginBtn, "steel blue", "#d1ccc0")

quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.5, rely=0.7, relwidth=0.18, relheight=0.08)

changeOnHover(quitBtn, "steel blue", "#d1ccc0")

root.mainloop()