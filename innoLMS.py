from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("getINNOtized Library Management System")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#99ff99")

#========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()
BOOK_TITLE = StringVar()
AUTHOR = StringVar()
BOOK_QTY = IntVar()
SEARCH = StringVar()
MEMBER_NAME = StringVar()
EMAIL = StringVar()
PHONE = StringVar()

#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `book` (book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, book_title TEXT, book_qty INTEGER, author TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `members` (member_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, member_name TEXT, email TEXT, phone TEXT)")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()

def Exit():
    result = tkMessageBox.askquestion('getINNOtized Library Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

def Exit2():
    result = tkMessageBox.askquestion('getINNOtized Library Management System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()

def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("getINNOtized Library Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()
    
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)
    
def Home():
    global Home
    Home = Tk()
    Home.title("getINNOtized Library Management System/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="getINNOtized Library Management System", font=('arial bold', 30))
    lbl_display.pack()
    menubar = Menu(Home)
    accountmenu = Menu(menubar, tearoff=0)
    bookmenu = Menu(menubar, tearoff=0)
    membersmenu = Menu(menubar, tearoff=0)
    accountmenu.add_command(label="Logout", command=Logout)
    accountmenu.add_command(label="Exit", command=Exit2)
    bookmenu.add_command(label="Add new book", command=ShowAddNewBook)
    bookmenu.add_command(label="View all books", command=ShowBooksView)
    membersmenu.add_command(label="Add new member", command=ShowAddNewMember)
    membersmenu.add_command(label="View all members", command=ShowMembersView)
    menubar.add_cascade(label="Account", menu=accountmenu)
    menubar.add_cascade(label="Books", menu=bookmenu)
    menubar.add_cascade(label="Members", menu=membersmenu)

    Home.config(menu=menubar)
    Home.config(bg="#99ff99")

#=====================================================BOOKS=====================================
def ShowAddNewBook():
    global addnewbookform
    addnewbookform = Toplevel()
    addnewbookform.title("getINNOtized Library Management System/Add new book")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewbookform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewbookform.resizable(0, 0)
    AddNewBookForm()

def AddNewBookForm():
    TopAddNew = Frame(addnewbookform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Book", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNewBook = Frame(addnewbookform, width=600)
    MidAddNewBook.pack(side=TOP, pady=50)
    lbl_booktitle = Label(MidAddNewBook, text="Book Title:", font=('arial', 25), bd=10)
    lbl_booktitle.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNewBook, text="Book Quantity:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_author = Label(MidAddNewBook, text="Author:", font=('arial', 25), bd=10)
    lbl_author.grid(row=2, sticky=W)
    booktitle = Entry(MidAddNewBook, textvariable=BOOK_TITLE, font=('arial', 25), width=15)
    booktitle.grid(row=0, column=1)
    bookqty = Entry(MidAddNewBook, textvariable=BOOK_QTY, font=('arial', 25), width=15)
    bookqty.grid(row=1, column=1)
    author = Entry(MidAddNewBook, textvariable=AUTHOR, font=('arial', 25), width=15)
    author.grid(row=2, column=1)
    btn_add = Button(MidAddNewBook, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNewBook)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNewBook():
    Database()
    cursor.execute("INSERT INTO `book` (book_title, book_qty, author) VALUES(?, ?, ?)", (str(BOOK_TITLE.get()), int(BOOK_QTY.get()), str(AUTHOR.get())))
    conn.commit()
    BOOK_TITLE.set("")
    AUTHOR.set("")
    BOOK_QTY.set("")
    cursor.close()
    conn.close()

def ViewBooksForm():
    global tree
    TopViewForm = Frame(viewbooksform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewbooksform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewbooksform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="All Library Books", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchBook)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=ResetBookSearch)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=DeleteBook)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("BookID", "Book Title", "Book Qty", "Author"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('BookID', text="BookID",anchor=W)
    tree.heading('Book Title', text="Book Title",anchor=W)
    tree.heading('Book Qty', text="Book Qty",anchor=W)
    tree.heading('Author', text="Author",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayBooksData()

def DisplayBooksData():
    Database()
    cursor.execute("SELECT * FROM `book`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SearchBook():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `book` WHERE `book_title` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def ResetBookSearch():
    tree.delete(*tree.get_children())
    DisplayBooksData()
    SEARCH.set("")

def DeleteBook():
    if not tree.selection():
       print("ERROR")
    else:
        result = tkMessageBox.askquestion('getINNOtized Library Management System', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `book` WHERE `book_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    

def ShowBooksView():
    global viewbooksform
    viewbooksform = Toplevel()
    viewbooksform.title("getINNOtized Library Management System/Library Books")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewbooksform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewbooksform.resizable(0, 0)
    ViewBooksForm()



#============================================AUTHENTICATION===========================================

def Logout():
    result = tkMessageBox.askquestion('getINNOtized Library Management System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes': 
        admin_id = ""
        root.deiconify()
        Home.destroy()
  
def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 

def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
accountmenu = Menu(menubar, tearoff=0)
accountmenu.add_command(label="Account", command=ShowLoginForm)
accountmenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=accountmenu)
root.config(menu=menubar)

#========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

#========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="getINNOtized Library Management System", font=('arial bold', 30))
lbl_display.pack()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
