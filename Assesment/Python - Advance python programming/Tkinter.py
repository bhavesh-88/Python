from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

root = Tk()
root.geometry("400x400")
root.title("Employee Registration")
root.resizable(width="false",height="false")



def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="harsh_pythondb"
    )

print(create_conn())

def insert_data():  
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor() # Execute the connection
        query = "insert into employee (fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args) # Execute the query
        conn.commit()
        conn.close()
        msg.showinfo("Insert Status","Data Insert Successfully.")

    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

def search_data():

    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

    if e_id.get()=="":
        msg.showinfo("Search Status","ID is Mandatory for Search Opetation.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from employee where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row = cursor.fetchall()

        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])

        else:
            msg.showinfo("Search Status","ID is not Found!")

        conn.close()

def update_data():  
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor() # Execute the connection
        query = "update employee set fname=%s, lname=%s, email=%s, mobile=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args) # Execute the query
        conn.commit()
        conn.close()
        msg.showinfo("Update Status","Data is Updated Successfully.")

    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory for Delete Operation.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from employee where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Delete Status","Data Deleted Successfully!")
    
    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")


#Labels

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name : ")
l_fname.place(x=50,y=100)

l_lname = Label(root,text="Last Name : ")
l_lname.place(x=50,y=150)

l_email = Label(root,text="Email : ")
l_email.place(x=50,y=200)

l_mobile = Label(root,text="Mobile : ")
l_mobile.place(x=50,y=250)


# TextBoxes

e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=100)

e_lname = Entry(root)
e_lname.place(x=150,y=150)

e_email = Entry(root)
e_email.place(x=150,y=200)

e_mobile = Entry(root)
e_mobile.place(x=150,y=250)

#Buttons

insert = Button(root,text="Insert",bg="black",fg="white",command=insert_data)
insert.place(x=50,y=300)

search = Button(root,text="Search",bg="black",fg="white",command=search_data)
search.place(x=120,y=300)

update = Button(root,text="Update",bg="black",fg="white",command=update_data)
update.place(x=190,y=300)

delete = Button(root,text="Delete",bg="black",fg="white",command=delete_data)
delete.place(x=260,y=300)

root.mainloop()

from tkinter import *
import tkinter.messagebox as msg
import mysql.connector

root = Tk()
root.geometry("400x400")
root.title("Employee Registration")
root.resizable(width="false",height="false")



def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="",
        database="harsh_pythondb"
    )

print(create_conn())

def insert_data():  
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor() # Execute the connection
        query = "insert into employee (fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args) # Execute the query
        conn.commit()
        conn.close()
        msg.showinfo("Insert Status","Data Insert Successfully.")

    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

def search_data():

    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

    if e_id.get()=="":
        msg.showinfo("Search Status","ID is Mandatory for Search Opetation.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "select * from employee where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        row = cursor.fetchall()

        if row:
            for i in row:
                e_fname.insert(0,i[1])
                e_lname.insert(0,i[2])
                e_email.insert(0,i[3])
                e_mobile.insert(0,i[4])

        else:
            msg.showinfo("Search Status","ID is not Found!")

        conn.close()

def update_data():  
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Update Status","All Fields are Mandatory*")
    else:
        conn = create_conn()
        cursor = conn.cursor() # Execute the connection
        query = "update employee set fname=%s, lname=%s, email=%s, mobile=%s where id=%s"
        args = (e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args) # Execute the query
        conn.commit()
        conn.close()
        msg.showinfo("Update Status","Data is Updated Successfully.")

    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory for Delete Operation.")
    else:
        conn = create_conn()
        cursor = conn.cursor()
        query = "delete from employee where id=%s"
        args = (e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        msg.showinfo("Delete Status","Data Deleted Successfully!")
    
    e_id.delete(0,"end")
    e_fname.delete(0,"end")
    e_lname.delete(0,"end")
    e_email.delete(0,"end")
    e_mobile.delete(0,"end")


#Labels

l_id = Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname = Label(root,text="First Name : ")
l_fname.place(x=50,y=100)

l_lname = Label(root,text="Last Name : ")
l_lname.place(x=50,y=150)

l_email = Label(root,text="Email : ")
l_email.place(x=50,y=200)

l_mobile = Label(root,text="Mobile : ")
l_mobile.place(x=50,y=250)


# TextBoxes

e_id = Entry(root)
e_id.place(x=150,y=50)

e_fname = Entry(root)
e_fname.place(x=150,y=100)

e_lname = Entry(root)
e_lname.place(x=150,y=150)

e_email = Entry(root)
e_email.place(x=150,y=200)

e_mobile = Entry(root)
e_mobile.place(x=150,y=250)

#Buttons

insert = Button(root,text="Insert",bg="black",fg="white",command=insert_data)
insert.place(x=50,y=300)

search = Button(root,text="Search",bg="black",fg="white",command=search_data)
search.place(x=120,y=300)

update = Button(root,text="Update",bg="black",fg="white",command=update_data)
update.place(x=190,y=300)

delete = Button(root,text="Delete",bg="black",fg="white",command=delete_data)
delete.place(x=260,y=300)

root.mainloop()











































