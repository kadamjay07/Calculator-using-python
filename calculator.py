from tkinter import*
import random
import time 
import datetime

root=Tk()
root.geometry('1600x8000')
root.title("Make it help you")

text_Input = StringVar()
operator = ""

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)



f1 = Frame(root,width=800, height=700,bg="powder blue", relief=SUNKEN)
f1.pack(side=BOTTOM)

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f1,font=('arail',20,'bold'),textvariable=text_Input, bd=30,insertwidth=4, bg='powder blue', justify='center')
txtDisplay.grid(columnspan=4)

btn7=Button(f1,padx=16,pady=16, fg='black',font=("arail",20,'bold'),text='7',bg='powder blue',command=lambda : btnclick(7))
btn7.grid(row=2,column=0)
btn8=Button(f1,padx=16,pady=16, fg='black',font=('arail',20,'bold'),text="8", bg='powder blue', command =lambda:btnclick(8))
btn8.grid(row=2,column=1)
btn9=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text= "9", bg='powder blue', command= lambda:btnclick(9))
btn9.grid(row=2,column=2)
Addition=Button(f1,padx=16,pady=16,fg='black',font=("arail",20,'bold'),text="+",bg='powder blue',command=lambda:btnclick("+"))
Addition.grid(row=2,column=3)


btn4=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='4',bg='powder blue',command=lambda:btnclick(4))
btn4.grid(row=3,column=0)
btn5=Button(f1,padx=16,pady=16,fg='black',font=("arail",20,'bold'),text='5',bg='powder blue',command=lambda:btnclick(5))
btn5.grid(row=3,column=1)
btn6=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='6',bg='powder blue' ,command=lambda:btnclick(6))
btn6.grid(row=3,column=2)
Subtraction=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='-',bg= 'powder blue',command=lambda:btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='1',bg='powder blue',command=lambda:btnclick(1))
btn1.grid(row=4,column=0)
btn2=Button(f1,padx=16,pady=16,fg="black",font=('arail',20,'bold'),text="2",bg="powder blue",command=lambda:btnclick(2))
btn2.grid(row=4,column=1)
btn3=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='3',bg='powder blue',command=lambda:btnclick(3))
btn3.grid(row=4,column=2)
Multiply=Button(f1,padx=16,pady=16,fg='black',font=('arail',20,'bold'),text='*',bg='powder blue',command=lambda:btnclick("*"))
Multiply.grid(row=4,column=3)


btn0=Button(f1,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="0", bg="powder blue", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)
btnClear=Button(f1,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="C", bg="powder blue", command=btnClearDisplay)
btnClear.grid(row=5,column=1)
btnEquals=Button(f1,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="=", bg="powder blue", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)
Division=Button(f1,padx=16,pady=16, fg="black", font=('arail',20,'bold'),text="/", bg="powder blue", command=lambda: btnclick("/"))
Division.grid(row=5,column=3) 



localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(Tops,font=('arail',50,'bold'),text='make it simple',fg='Steel Blue',bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('arail',50,'bold'),text=localtime,fg='steel blue',bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


root.mainloop()