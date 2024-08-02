from tkinter import *
from tkinter import messagebox









class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1000x500+100+100")
        self.root.resizable(False,False)
        self.root.config(bg="lightblue")

        title=Label(self.root,text="Student Management System",font=("times new roman",30,"bold"),bg="gray",fg="black",padx=10,pady=10)
        title.place(x=0,y=0,relwidth=1)
        
        lblidnex=Label(self.root,text="Index No",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=90,width=300,height=40)
        lblname=Label(self.root,text="Student Name",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=150,width=300,height=40)
        lbladderss=Label(self.root,text="Address",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=210,width=300,height=40)
        lblcontact=Label(self.root,text="Contact",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=270,width=300,height=40)
        lblemail=Label(self.root,text="Email",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=330,width=300,height=40)
        lblclass=Label(self.root,text="Class",font=("times",20,),bg="gray",fg="black",justify=LEFT).place(x=20,y=400,width=300,height=40)#entry box








if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

