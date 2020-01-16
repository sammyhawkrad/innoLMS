from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
from datetime import date

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
BORROW_DATE = StringVar()
DUE_DATE = StringVar()

#========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `book` (book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, book_title TEXT, book_qty INTEGER, author TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `members` (member_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, member_name TEXT, email TEXT, phone TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `borrows` (borrow_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, member_name TEXT, book_title TEXT, borrow_date DATE NOT NULL, due_date DATE NOT NULL)")
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
    borrowsmenu = Menu(menubar, tearoff=0)
    accountmenu.add_command(label="Logout", command=Logout)
    accountmenu.add_command(label="Exit", command=Exit2)
    bookmenu.add_command(label="Add new book", command=ShowAddNewBook)
    bookmenu.add_command(label="View all books", command=ShowBooksView)
    membersmenu.add_command(label="Add new member", command=ShowAddNewMember)
    membersmenu.add_command(label="View all members", command=ShowMembersView)
    borrowsmenu.add_command(label="Record new request", command=ShowAddNewBorrow)
    borrowsmenu.add_command(label="View borrowed books", command=ShowBorrowsView)
    menubar.add_cascade(label="Account", menu=accountmenu)
    menubar.add_cascade(label="Books", menu=bookmenu)
    menubar.add_cascade(label="Members", menu=membersmenu)
    menubar.add_cascade(label="Borrow Log", menu=borrowsmenu)


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

#=====================================================MEMBERS=====================================
def ShowAddNewMember():
    global addnewmemberform
    addnewmemberform = Toplevel()
    addnewmemberform.title("getINNOtized Library Management System/Add new book")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewmemberform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewmemberform.resizable(0, 0)
    AddNewMemberForm()

def AddNewMemberForm():
    TopAddNew = Frame(addnewmemberform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Member", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNewMember = Frame(addnewmemberform, width=600)
    MidAddNewMember.pack(side=TOP, pady=50)
    lbl_membername = Label(MidAddNewMember, text="Name:", font=('arial', 25), bd=10)
    lbl_membername.grid(row=0, sticky=W)
    lbl_email = Label(MidAddNewMember, text="Email:", font=('arial', 25), bd=10)
    lbl_email.grid(row=1, sticky=W)
    lbl_phone = Label(MidAddNewMember, text="Phone:", font=('arial', 25), bd=10)
    lbl_phone.grid(row=2, sticky=W)
    membername = Entry(MidAddNewMember, textvariable=MEMBER_NAME, font=('arial', 25), width=15)
    membername.grid(row=0, column=1)
    email = Entry(MidAddNewMember, textvariable=EMAIL, font=('arial', 25), width=15)
    email.grid(row=1, column=1)
    phone = Entry(MidAddNewMember, textvariable=PHONE, font=('arial', 25), width=15)
    phone.grid(row=2, column=1)
    btn_add = Button(MidAddNewMember, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNewMember)
    btn_add.grid(row=3, columnspan=2, pady=20)

def AddNewMember():
    Database()
    cursor.execute("INSERT INTO `members` (member_name, email, phone) VALUES(?, ?, ?)", (str(MEMBER_NAME.get()), str(EMAIL.get()), str(PHONE.get())))
    conn.commit()
    MEMBER_NAME.set("")
    PHONE.set("")
    EMAIL.set("")
    cursor.close()
    conn.close()

def ViewMembersForm():
    global tree
    TopViewForm = Frame(viewmembersform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewmembersform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewmembersform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Library Members", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchMember)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=ResetMemberSearch)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=DeleteMember)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("MemberID", "Name", "Email", "Phone"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('MemberID', text="MemberID",anchor=W)
    tree.heading('Name', text="Name",anchor=W)
    tree.heading('Email', text="Email",anchor=W)
    tree.heading('Phone', text="Phone",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayMembersData()

def DisplayMembersData():
    Database()
    cursor.execute("SELECT * FROM `members`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SearchMember():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `members` WHERE `member_name` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def ResetMemberSearch():
    tree.delete(*tree.get_children())
    DisplayMembersData()
    SEARCH.set("")

def DeleteMember():
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
            cursor.execute("DELETE FROM `members` WHERE `member_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    

def ShowMembersView():
    global viewmembersform
    viewmembersform = Toplevel()
    viewmembersform.title("getINNOtized Library Management System/Library Members")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewmembersform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewmembersform.resizable(0, 0)
    ViewMembersForm()

#=====================================================BOOK BORROW=====================================
def ShowAddNewBorrow():
    global addnewborrowform
    addnewborrowform = Toplevel()
    addnewborrowform.title("getINNOtized Library Management System/Add new book borrow")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewborrowform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewborrowform.resizable(0, 0)
    AddNewBorrowForm()

def AddNewBorrowForm():
    TopAddNew = Frame(addnewborrowform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Borrow Request", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNewBorrow = Frame(addnewborrowform, width=600)
    MidAddNewBorrow.pack(side=TOP, pady=50)
    lbl_membername = Label(MidAddNewBorrow, text="Name:", font=('arial', 25), bd=10)
    lbl_membername.grid(row=0, sticky=W)
    lbl_booktitle = Label(MidAddNewBorrow, text="Book Title:", font=('arial', 25), bd=10)
    lbl_booktitle.grid(row=1, sticky=W)
    lbl_borrow_date = Label(MidAddNewBorrow, text="Borrow Date:", font=('arial', 25), bd=10)
    lbl_borrow_date.grid(row=2, sticky=W)
    lbl_due_date = Label(MidAddNewBorrow, text="Due Date:", font=('arial', 25), bd=10)
    lbl_due_date.grid(row=3, sticky=W)
    membername = Entry(MidAddNewBorrow, textvariable=MEMBER_NAME, font=('arial', 25), width=15)
    membername.grid(row=0, column=1)
    booktitle = Entry(MidAddNewBorrow, textvariable=BOOK_TITLE, font=('arial', 25), width=15)
    booktitle.grid(row=1, column=1)
    borrow_date = Entry(MidAddNewBorrow, textvariable=BORROW_DATE, font=('arial', 25), width=15)
    borrow_date.grid(row=2, column=1)
    due_date = Entry(MidAddNewBorrow, textvariable=DUE_DATE, font=('arial', 25), width=15)
    due_date.grid(row=3, column=1)
    btn_add = Button(MidAddNewBorrow, text="Save", font=('arial', 18), width=30, bg="#009ACD", command=AddNewBorrow)
    btn_add.grid(row=4, columnspan=2, pady=20)

def AddNewBorrow():
    Database()
    cursor.execute("INSERT INTO `borrows` (member_name, book_title, borrow_date, due_date) VALUES(?, ?, ?, ?)", (str(MEMBER_NAME.get()), str(BOOK_TITLE.get()), str(BORROW_DATE.get()), str(DUE_DATE.get())))
    conn.commit()
    MEMBER_NAME.set("")
    BOOK_TITLE.set("")
    BORROW_DATE.set("")
    DUE_DATE.set("")
    cursor.close()
    conn.close()

def ViewBorrowsForm():
    global tree
    TopViewForm = Frame(viewborrowsform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewborrowsform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewborrowsform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="List of Borrowed Books", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchBorrow)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=ResetBorrowSearch)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=DeleteBorrow)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("BorrowID", "Name", "Book Title", "Borrow Date", "Due Date"), selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('BorrowID', text="BorrowID",anchor=W)
    tree.heading('Name', text="Name",anchor=W)
    tree.heading('Book Title', text="Book Title",anchor=W)
    tree.heading('Borrow Date', text="Borrow Date",anchor=W)
    tree.heading('Due Date', text="Due Date",anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayBorrowsData()

def DisplayBorrowsData():
    Database()
    cursor.execute("SELECT * FROM `borrows`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SearchBorrow():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `borrows` WHERE `member_name` OR `book_title` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

def ResetBorrowSearch():
    tree.delete(*tree.get_children())
    DisplayBorrowsData()
    SEARCH.set("")

def DeleteBorrow():
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
            cursor.execute("DELETE FROM `borrows` WHERE `borrow_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    

def ShowBorrowsView():
    global viewborrowsform
    viewborrowsform = Toplevel()
    viewborrowsform.title("getINNOtized Library Management System/Borrowed Books")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewborrowsform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewborrowsform.resizable(0, 0)
    ViewBorrowsForm()


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
