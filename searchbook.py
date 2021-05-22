from tkinter import *
import PIL
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

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
mypass = "sunder9900$"
mydatabase = "libb"

con = mysql.connector.connect(host="localhost", user="sunder", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"  # Book Table


def search():
    global SearchBtn, labelFrame, lb1, en1, quitBtn, root, Canvas1

    sub = en1.get()

    SearchBtn.destroy()
    quitBtn.destroy()
    lb1.destroy()
    en1.destroy()

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    y = 0.25

    Label(labelFrame, text="%-10s%-30s%-30s%-20s" % ('BID', 'Title',  'Author', 'Status'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    searchSql = "select * from " + bookTable + " where title = '" + sub + "'"
    try:
        cur.execute(searchSql)
        records = cur.fetchall()
        con.commit()
        for i in records:
            Label(labelFrame, text="%-10s%-30s%-30s%-20s" % (i[0], i[1], i[2], i[3]), bg='black',
                  fg='white').place(relx=0.07, rely=y)
            y += 0.1
            print(i)
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    print(sub)

    quitBtn = Button(root, text="quit", bg='#455A64', fg='white', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.85, relwidth=0.18, relheight=0.08)


def searchBook():
    global en1, SearchBtn, lb1, labelFrame, quitBtn, Canvas1, root

    root = Tk()
    root.title("Library")
    root.maxsize(width=900, height=900)
    root.geometry("600x500")


    Canvas1 = Canvas(root)


    Canvas1.config(bg="brown3")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    headingFrame1 = Frame(root, bg="#333945", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
    headingFrame2.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.9)

    headingLabel = Label(headingFrame2, text="SEARCH BOOK", fg='black')
    headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Enter title : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SearchBtn = Button(root, text="Search", bg='#d1ccc0', fg='black', command=search)
    SearchBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)
    changeOnHover(SearchBtn, "steel blue", "#d1ccc0")

    quitBtn = Button(root, text="Quit", bg='#d1ccc0', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)
    changeOnHover(quitBtn, "steel blue", "#d1ccc0")


    root.mainloop()