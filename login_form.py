from tkinter import *
root=Tk()
root.geometry('600x300')
root.title('Login form')

lbl1= Label(root,text="Login form",font=('Arial',20),fg='red')
lbl1.place(x=30,y=30)

userlbl=Label(root,text ='user name')
userlbl.place(x=40,y=70)

usertxt=Entry()
usertxt.place(x=130,y=70)

userlbl=Label(root,text ='Enter password')
userlbl.place(x=40,y=90)

usertxt=Entry()
usertxt.place(x=130,y=70)

userlbl=Label(root,text ='Enter captcha')
userlbl.place(x=40,y=90)

usertxt=Entry()
usertxt.place(x=130,y=120)

bt1=Button(root,text="Login")
bt1.place(x=50,y=150)

bt1=Button(root,text="Cancel")
bt1.place(x=100,y=150)

root.mainloop()


