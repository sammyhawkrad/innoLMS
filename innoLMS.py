Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkintet
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import tkintet
ModuleNotFoundError: No module named 'tkintet'
>>> import tkinter
>>> window = tkinter.Tk()
>>> window.title("getINNOtized Library Management System")
''
>>> label = tkinter.Label(window, text = "getINNOtized Library Management System").pack()
>>> window.mainloop()