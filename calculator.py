from tkinter import *
root=Tk()
root.geometry("220x320")
root.iconbitmap("Dtafalonso-Android-Lollipop-Calculator.ico")
root.resizable(False,False)
x=StringVar()
x.set("")
root.title("calculator")
#global var
def click(event):
    text=event.widget.cget('text')
    if text=="=":
        if x.get().isdigit():
            x.set(x.get())
            e1.update()
        else:
            x.set(eval(x.get()))
            e1.update()
    elif text=="Cl":
        x.set("")
        e1.update()
    else:
        x.set(x.get()+text)
        e1.update()
e1=Entry(root,textvariable=x,bg="azure2",font="TimesNewRoman 24")
e1.pack(fill=X,ipadx=2,pady=4,padx=3)
f2=Frame(root,bg='white')
f2.pack()
B1=Button(f2,text="9",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B1.pack(side=LEFT)
B1.bind("<Button-1>",click)
B2=Button(f2,text="8",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B2.pack(side=LEFT)
B2.bind("<Button-1>",click)
B3=Button(f2,text="7",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B3.pack(side=LEFT)
B3.bind("<Button-1>",click)
f3=Frame(root,bg='white')
f3.pack()
B4=Button(f3,text="6",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B4.pack(side=LEFT)
B4.bind("<Button-1>",click)
B5=Button(f3,text="5",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B5.pack(side=LEFT)
B5.bind("<Button-1>",click)
B6=Button(f3,text="4",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B6.pack(side=LEFT)
B6.bind("<Button-1>",click)
f4=Frame(root,bg='white')
f4.pack()
B7=Button(f4,text="3",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=14.5)
B7.pack(side=LEFT)
B7.bind("<Button-1>",click)
B8=Button(f4,text="2",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B8.pack(side=LEFT)
B8.bind("<Button-1>",click)
B9=Button(f4,text="1",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B9.pack(side=LEFT)
B9.bind("<Button-1>",click)
B9.bind("<Button-1>",click)
B10=Button(f2,text="+",bg='white',font='TimesNewRoman 14',pady=10,padx=14)
B10.pack(side=LEFT)
B10.bind("<Button-1>",click)
B11=Button(f3,text="-",bg='white',font='TimesNewRoman 14',pady=10,padx=16)
B11.pack(side=LEFT)
B11.bind("<Button-1>",click)
B12=Button(f4,text="*",bg='white',font='TimesNewRoman 14',pady=10,padx=15)
B12.pack(side=LEFT)
B12.bind("<Button-1>",click)
f5=Frame(root,bg='white')
f5.pack()
B13=Button(f5,text=".",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=18)
B13.pack(side=LEFT)
B13.bind("<Button-1>",click)
B14=Button(f5,text="0",bg='black',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B14.pack(side=LEFT)
B14.bind("<Button-1>",click)
B15=Button(f5,text="=",bg='red',fg='white',font='TimesNewRoman 14',pady=10,padx=15)
B15.pack(side=LEFT)
B15.bind("<Button-1>",click)
B16=Button(f5,text="/",bg='white',font='TimesNewRoman 14',pady=10,padx=17)
B16.pack(side=LEFT)
B16.bind("<Button-1>",click)
f6=Frame(root,bg='white')
f6.pack()
B17=Button(f6,text="Cl",bg='white',font='TimesNewRoman 14',pady=10,padx=11)
B17.pack(side=LEFT)
B17.bind("<Button-1>",click)
B18=Button(f6,text="%",bg='white',font='TimesNewRoman 14',pady=10,padx=12)
B18.pack(side=LEFT)
B18.bind("<Button-1>",click)
B19=Button(f6,text="(",bg='white',font='TimesNewRoman 14',pady=10,padx=18)
B19.pack(side=LEFT)
B19.bind("<Button-1>",click)
B20=Button(f6,text=")",bg='white',font='TimesNewRoman 14',pady=10,padx=15.5)
B20.pack(side=LEFT)
B20.bind("<Button-1>",click)
root.mainloop()