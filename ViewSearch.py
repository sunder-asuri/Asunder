import tkinter

import PIL
from PIL import ImageTk, Image
import mysql.connector
from tkinter import *
import ViewBooks
import searchbook

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
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = tkinter.Canvas(root)


    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=tkinter.BOTH)

    headingFrame1 = tkinter.Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = tkinter.Label(headingFrame1, text="Welcome to \n Menus Section", bg='black', fg='white',
                                 font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    btn1 = tkinter.Button(root, text="Search Book", bg='black', fg='white', command=searchbook.searchBook)
    btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

    changeOnHover(btn1, "steel blue", "black")

    btn2 = tkinter.Button(root, text="View Book", bg='black', fg='white', command=ViewBooks.View)
    btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)
    changeOnHover(btn2, "steel blue", "black")


    quitBtn = tkinter.Button(root, text = "quit", bg = '#f7f1e3', fg='black', command = root.destroy)
    quitBtn.place(relx=0.4, rely=0.65, relwidth=0.18, relheight=0.08)
    changeOnHover(quitBtn, "steel blue", "#d1ccc0")