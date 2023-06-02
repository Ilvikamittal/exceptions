from tkinter import*
root=Tk()

root.title("sum of 2 numbers")
root.geometry("400x400")
root.configure(background="green")


no1=Label(root,text="number 1 will be: ")   
no1.place(relx=0.2,rely=0.3,anchor=CENTER)

no2=Label(root,text="number 2 will be: ")
no2.place(relx=0.2,rely=0.5,anchor=CENTER)

nu1=Entry(root)
nu1.place(relx=0.8,rely=0.3,anchor=CENTER)

nu2=Entry(root)
nu2.place(relx=0.8,rely=0.5,anchor=CENTER)

sum=Label(root)
sum.place(relx=0.5,rely=0.6,anchor=CENTER)


def sum1():
    num1=int(nu1.get())
    num2=int(nu2.get())
    sum["text"]=str(num1+num2)
    
    
btn1=Button(root,text="calculate",command=sum1)
btn1.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()

