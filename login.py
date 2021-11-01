from functools import partial

from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from main import *
import threading
def validateLogin(username, password,root):
	print("username entered :", username.get())
	#print("password entered :", password.get())
	
	
	mypass = "root" #password
	mydatabase="library" #The database name
	con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase)
    #root is the username here
	cur = con.cursor() #cur -> cursor
	
	q =f"SELECT * from users WHERE username='{username.get()}' AND password='{password.get()}';"
	
	a = cur.execute(query=q)
	if(a == 0):
		messagebox.showwarning("Invalid","Invalid Credentials")
	else:
		t = threading.Thread(target=main(),name="t2")
		t.start()
	tkWindow.destroy()
	
	cur.close()
	
	return


global tkWindow
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Admin_Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",bg="#FFBB00").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",bg="#12a4d9").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=lambda : validateLogin(root=tkWindow),bg="#D6ED17").grid(row=4, column=0)  

tkWindow.mainloop()