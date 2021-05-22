import tkinter
import PIL
from PIL import ImageTk, Image
import mysql.connector
from tkinter import *
import AddBook
import DeleteBook
import ViewBooks
import IssueBook
import ReturnBook
import ModifyBook
import ViewSearch





def picture():
    '''textwindow = Toplevel(root)
    textwindow.title("Text in image")
    textwindow.geometry("400x500")'''
    img = PIL.Image.open('lib.png')
    pic = ImageTk.PhotoImage(img)



    '''cv2.imshow('Result', pic)
    cv2.waitKey(0)'''

    '''label = Label(textwindow,image=pic, bg='white')
    label.image = pic
    label.place(x=215, y=75)'''

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def options():
    # Add your own database name and password here to reflect in the code
    # mypass = "sunder9900$"
    mydatabase = "libb"

    con = mysql.connector.connect(host="localhost", user="sunder", password="sunder9900$", database=mydatabase)
    cur = con.cursor()

    root = tkinter.Tk()
    root.title("Library")
    root.maxsize(width=900, height=900)
    root.geometry("600x500")
    # root.configure(bg='blue')

    '''canvas = Canvas(root, width = 300, height = 300)
    canvas.pack()
    img = ImageTk.PhotoImage(file="lib.png")
    canvas.create_image(600,5000,anchor=NW, image=img)'''

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



    Canvas1 = tkinter.Canvas(root)

    #Canvas1.create_image(300, 340, image=img)
    Canvas1.config(bg="#C36241")
    Canvas1.pack(expand=True, fill=tkinter.BOTH)

    headingFrame1 = tkinter.Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = tkinter.Label(headingFrame1, text="Welcome to \n Menus Section", bg='black', fg='white',
                                 font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = tkinter.Button(root, text="Add Book Details", bg='black', fg='white', command = AddBook.addBook)
    btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    changeOnHover(btn1, "steel blue", "black")

    btn2 = tkinter.Button(root, text="Delete Book", bg='black', fg='white', command = DeleteBook.delete)
    btn2.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)
    changeOnHover(btn2, "steel blue", "black")

    btn3 = tkinter.Button(root, text="View/Search", bg='black', fg='white', command = ViewSearch.options)
    btn3.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    changeOnHover(btn3, "steel blue", "black")

    btn4 = tkinter.Button(root, text="Issue Book to Student", bg='black', fg='white', command = IssueBook.issueBook)
    btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)
    changeOnHover(btn4, "steel blue", "black")

    btn5 = tkinter.Button(root, text="Return Book", bg='black', fg='white', command = ReturnBook.returnBook)
    btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)
    changeOnHover(btn5, "steel blue", "black")

    btn6 = tkinter.Button(root, text="Modify", bg='black', fg='white', command = ModifyBook.modifyBook)
    btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
    changeOnHover(btn6, "steel blue", "black")

    '''helpbtn = Button(root, text="Help", bg='#f7f1e3', fg='black', command=picture)
    helpbtn.place(relx=0.05, rely=0.9, relwidth=0.18, relheight=0.08)
    changeOnHover(helpbtn, "steel blue", "#f7f1e3")'''

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.91, relwidth=0.18, relheight=0.08)
    changeOnHover(quitBtn, "steel blue", "#f7f1e3")

    root.mainloop()



