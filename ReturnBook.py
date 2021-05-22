from tkinter import *
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
issueTable = "books_issued"  # Issue Table
bookTable = "books"  # Book Table

allBid = []  # List To store all Book IDs


def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get()

    extractBid = "select bid from " + issueTable
    try:
        cur.execute(extractBid)
        records = cur.fetchall()
        con.commit()
        for i in records:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from " + bookTable + " where bid = '" + bid + "'"
            cur.execute(checkAvail)
            records = cur.fetchall()
            con.commit()
            for i in records:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book ID not present")
    except:
        messagebox.showinfo("Error", "Can't fetch Book IDs")

    issueSql = "delete from " + issueTable + " where bid = '" + bid + "'"

    print(bid in allBid)
    print(status)
    updateStatus = "update " + bookTable + " set status = 'avail' where bid = '" + bid + "'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value entered is wrong, Try again")

    allBid.clear()
    root.destroy()


def returnBook():
    global bookInfo1, SubmitBtn, quitBtn, Canvas1, con, cur, root, labelFrame, lb1

    root = Tk()
    root.title("Library")
    root.maxsize(width=900, height=900)
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="slateblue2")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID to Delete
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    # Submit Button
    SubmitBtn = Button(root, text="Return", bg='#d1ccc0', fg='black', command=returnn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    changeOnHover(SubmitBtn, "steel blue", "#d1ccc0")

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    changeOnHover(quitBtn, "steel blue", "#d1ccc0")

    root.mainloop()