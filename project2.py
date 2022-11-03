import tkinter
from tkinter import *
from tkinter import messagebox
from unittest import result
from tkinter.ttk import Combobox
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="aadhik.s",database="sulthana")
print(mydb)
mainWindow = tkinter.Tk()
mainWindow.geometry('500x500')
mainWindow.title('STUDENT MANAGEMENT')
mainFrame=Frame(mainWindow,highlightbackground='green',highlightthicknes=5)
mainFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')


def adminShow():
    mainWindow.withdraw()

    global adminWindow
    adminWindow= Toplevel(mainWindow)
    adminWindow.geometry('500x500')
    adminWindow.title('ADMIN LOGIN') 
    global adminLoginFrame
    adminLoginFrame=Frame(adminWindow,width=500,height=500,highlightbackground='green',highlightthicknes=5)
    adminLoginFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
    global adminFrame
    adminFrame=Frame(adminWindow,width=500,height=500,highlightbackground='green',highlightthicknes=5)
    unLbl = tkinter.Label(adminLoginFrame,text='User name : ')
    unLbl.grid(row=2,column=1)
    global userName
    userName=StringVar() 
    unEntry = tkinter.Entry(adminLoginFrame,textvariable=userName,width=50)
    unEntry.grid(row=2,column=2)
    pwdLbl = tkinter.Label(adminLoginFrame,text='Password : ')
    pwdLbl.grid(row=4,column=1)
    global password
    password=StringVar() 
    pwdEntry = tkinter.Entry(adminLoginFrame,textvariable=password,width=50,show='*')
    pwdEntry.grid(row=4,column=2)
    loginBtn = tkinter.Button(adminLoginFrame,text='submit',command=adminLogin, anchor=CENTER )
    loginBtn.grid(row=5,column=2)
    
def teacherShow():
    mainWindow.withdraw()
    global teacherWindow
    teacherWindow= Toplevel(mainWindow)
    teacherWindow.geometry('500x500')
    teacherWindow.title('TEACHER LOGIN') 
    global teacherLoginFrame
    teacherLoginFrame=Frame(teacherWindow,width=500,height=500,highlightbackground='green',highlightthicknes=5)
    teacherLoginFrame.grid(row=1,column=1,padx=10,pady=10)
    global teacherFrame
    teacherFrame=Frame(teacherWindow,width=500,height=500,highlightbackground='green',highlightthicknes=5)
    unLbl = tkinter.Label(teacherLoginFrame,text='User name : ')
    unLbl.grid(row=2,column=1)
    global userName
    userName=StringVar() 
    unEntry = tkinter.Entry(teacherLoginFrame,textvariable=userName,width=50)
    unEntry.grid(row=2,column=2)
    pwdLbl = tkinter.Label(teacherLoginFrame,text='Password : ')
    pwdLbl.grid(row=4,column=1)
    global password
    password=StringVar() 
    pwdEntry = tkinter.Entry(teacherLoginFrame,textvariable=password,width=50,show='*')
    pwdEntry.grid(row=4,column=2)
    loginBtn = tkinter.Button(teacherLoginFrame,text='submit',command=teacherLogin, anchor=CENTER )
    loginBtn.grid(row=5,column=2)


adminBtn = tkinter.Button(mainFrame,text='Login as Admin',command=adminShow )
adminBtn.grid(row=3,column=1, sticky='ew')

teacherBtn = tkinter.Button(mainFrame,text='Login as Teacher',command=teacherShow )
teacherBtn.grid(row=4, column=7, sticky='')


def show_failed():
        failedFrame = Frame(teacherWindow,width=100,height=300,highlightbackground='green',highlightthicknes=5)
        failedFrame.grid(row=2,column=1,padx=10,pady=10, sticky='ew') 
        cursor = mydb.cursor()
        cursor.execute("""SELECT * FROM std_%s_marks WHERE eng<35||tam<35||mat<35||sci<35||social<35"""% (exam.get(),))
        result = cursor.fetchall()
        headers = [i[0] for i in cursor.description]
        for h in range(len(headers)):
                e = Entry(failedFrame, width=10, fg='black', justify=CENTER)
                e.grid(row=0, column=h)
                e.insert(END, headers[h])
                e.config(state='readonly')
        i=1
        for student in result:
            for j in range(len(student)):
                e = Entry(failedFrame, width=10, fg='blue', justify=CENTER)
                e.grid(row=i, column=j)
                e.insert(END, student[j])
                e.config(state='readonly')
            i=i+1

def fee():
    adminFrame.grid_forget()
    adminWindow.title('FEES UPDATES')
    global feeFrame
    feeFrame=Frame(adminWindow,width=500,height=500,highlightbackground='green',highlightthicknes=5)
    feeFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
    feeLbl = tkinter.Label(feeFrame,text='enter student id to update fee') 
    feeLbl.grid(row=6,column=1)
    global std_id 
    std_id=StringVar()
    stdEntry = tkinter.Entry(feeFrame,textvariable=std_id,width=50)   
    stdEntry.grid(row=7,column=1)
    stdEntry.focus()
    paid = tkinter.Button(feeFrame,text='PAID',command=update_fee )
    paid.grid(row=9,column=1)
    back = tkinter.Button(feeFrame,text='back',command=feeToAdmin )
    back.grid(row=9,column=2)

def stdToAdmin():
    adminWindow.title('ADMIN')
    stdFrame.grid_forget()
    adminFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')

    
def feeToAdmin():
    adminWindow.title('ADMIN')
    feeFrame.grid_forget()
    adminFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
    
def update_fee():
    cursor=mydb.cursor()
    sql="update fee_detail set fees_status=%s where std_id=%s"
    val =("paid", std_id.get())
    cursor.execute(sql,(val))
    mydb.commit() 
    messagebox.showinfo(title="fees",message="fees paid status updated for the student "+std_id.get()) 

def studDetails():
    adminFrame.grid_forget()
    global stdFrame
    stdFrame = Frame(adminWindow,width=100,height=300,highlightbackground='green',highlightthicknes=5)
    stdFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
    adminWindow.title('STUDENT DETAILS')
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM STUDENT")
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]    
    for h in range(len(headers)):
        e = Entry(stdFrame, width=10, fg='black', justify=CENTER)
        e.grid(row=0, column=h)
        e.insert(END, headers[h])
        e.config(state='readonly')
        i=1
    for student in result:
        for j in range(len(student)):
            e = Entry(stdFrame, width=10, fg='blue', justify=CENTER)
            e.grid(row=i, column=j)
            e.insert(END, student[j])
            e.config(state='readonly')
        i=i+1
    back = tkinter.Button(stdFrame,text='back',command=stdToAdmin )
    back.grid(row=9,column=1)
            
def adminLogin():
    cursor = mydb.cursor()
    sql ="SELECT user_name FROM users where user_name=%s and pwd=%s and user_role=%s"
    val =(userName.get(), password.get(),"admin")
    cursor.execute(sql,val)
    if cursor.fetchone():
        adminWindow.title('ADMIN')
        adminLoginFrame.grid_forget()
        adminFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
        stdBtn = tkinter.Button(adminFrame,text='View Student Details',command=studDetails)
        stdBtn.grid(row=4, column=7, sticky='')
        feeBtn = tkinter.Button(adminFrame,text='Update Student\'s fees paid status',command=fee)
        feeBtn.grid(row=5, column=7, sticky='')
    else:
        messagebox.showerror(title="warning",message="wrong password")

def teacherLogin():
    cursor = mydb.cursor()
    sql ="SELECT user_name FROM users where user_name=%s and pwd=%s and user_role=%s"
    val =(userName.get(), password.get(),"teacher")
    cursor.execute(sql,val)
    if cursor.fetchone():
        teacherLoginFrame.grid_forget()
        teacherFrame.grid(row=1,column=1,padx=10,pady=10, sticky='ew')
        tLbl = tkinter.Label(teacherFrame,text='TEACHER',font=('time new roman',20,'italic'),fg='white',bg='blue') 
        tLbl.grid(row=1,column=1) 
        examLbl = tkinter.Label(teacherFrame,text='select exam to filter failed students') 
        examLbl.grid(row=3,column=1)
        global exam
        exam=Combobox(teacherFrame,values=['quaterly','halfyearly','annual'])
        exam.grid(row=5,column=1)
        show = tkinter.Button(teacherFrame,text='show',command=show_failed)
        show.grid(row=5, column=2)
    else:
        messagebox.showerror(title="warning",message="wrong password")

mainWindow.mainloop()