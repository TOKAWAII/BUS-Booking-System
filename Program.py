from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("BUS RESERVATION SYSTEM");
root.geometry('800x600')
Label(root,text="Bus Booking System",font="Bold 25",fg="black",bg="CYAN" ).grid(row=0,column=5)
a=PhotoImage(file= 'bus.gif')
Label(root,image=a).grid(row=8,column=5)
conn = sqlite3.connect('BUS_LIST.db')
c = conn.cursor()
c.execute(
    "CREATE Table IF NOT EXISTS bb_bus(OPERATOR text,BUS_TYPE text,D_FROM text,A_TO text,DATE text,DEP_TIME text,ARR_TIME text,FARE integer,SEATS integer)")
conn.commit()
def add():
    rt=Tk()
    rt.geometry('800x600')
    lt1=Label(rt,text="Bus Booking System",font="Bold 15",fg="white",bg="orange" ).grid(row=0,column=3)
    lt2=Label(rt,text="Bus Operator Details Filling ",font="Bold 15",fg="white",bg="red" ).grid(row=1,column=3)
    lt3=Label(rt,text='Full Name:',font='bold 10').grid(row=40,column=1)
    e1=Entry(rt)
    e1.grid(row=40,column=2)
    f1=Label(rt,text='Contact Number:',font="bold 10").grid(row=41,column=1)
    e2=Entry(rt)
    e2.grid(row=41,column=2)
    f2=Label(rt,text='Address:',font="bold 10").grid(row=42,column=1)
    e3=Entry(rt)
    e3.grid(row=42,column=2)
    def detail():
        l1=Label(rt,text='Operator:',font="bold 10").grid(row=44,column=1)
        e4=Entry(rt)
        e4.grid(row=44,column=2)
        l2=Label(rt,text='Bus Type:',font="bold 10").grid(row=45,column=1)
        e5=Entry(rt)
        e5.grid(row=45,column=2)
        l3=Label(rt,text='From:',font="bold 10").grid(row=46,column=1)
        e6=Entry(rt)
        e6.grid(row=46,column=2)
        l4=Label(rt,text='To:',font="bold 10").grid(row=47,column=1)
        e7=Entry(rt)
        e7.grid(row=47,column=2)
        l5=Label(rt,text='Date:',font="bold 10").grid(row=48,column=1)
        e8=Entry(rt)
        e8.grid(row=48,column=2)
        l6=Label(rt,text='Dep Time:',font="bold 10").grid(row=49,column=1)
        e9=Entry(rt)
        e9.grid(row=49,column=2)
        l7=Label(rt,text='Arr Time:',font="bold 10").grid(row=50,column=1)
        e10=Entry(rt)
        e10.grid(row=50,column=2)
        l8=Label(rt,text='Fare:',font="bold 10").grid(row=51,column=1)
        e11=Entry(rt)
        e11.grid(row=51,column=2)
        l9=Label(rt,text='Seats:',font="bold 10").grid(row=52,column=1)
        e12=Entry(rt)
        e12.grid(row=52,column=2)


        def clicbtnb():
            conn = sqlite3.connect('BUS_LIST.db')
            c = conn.cursor()
            values = (e4.get(), e5.get(), e6.get(), e7.get(), e8.get(), e9.get(), e10.get(), e11.get(), e12.get())
            c.execute("""INSERT INTO bb_bus(OPERATOR,BUS_TYPE,D_FROM,A_TO ,DATE,DEP_TIME ,ARR_TIME ,FARE ,SEATS)
                          VALUES(?,?,?,?,?,?,?,?,?)""", values)
            conn.commit()
            row = c.fetchall()
            conn.close()
            messagebox.showinfo("DATA", "DATA SAVED")
            rt.destroy()

        Button(rt,text='Save',command=clicbtnb ,font="bold 13 " ).grid(row=53,column=3)

    Button(rt,text='Add Details',command=detail,font="bold 10").grid(row=43,column=4)
    rt.mainloop()

def search():
    m=Tk()
    m.geometry('800x600')
    lbl = Label(m, text="BUS BOOKING SERVICE",font="Bold 15",fg="CYAN",bg="BLUE").grid(column=2, row=0,columnspan=5)
    Label(m, text="LISTING BUSES",font="Bold 15",fg="white",bg="RED").grid(column=3, row=1,columnspan=3)

    lb1 = Label(m, text="BUS TYPE").grid(column=1, row=4)
    V = StringVar(m)

    choice = ['AC', 'NON-AC', 'AC-SLEEPER', 'NON-AC SLEEPER']
    OptionMenu(m, V, *choice).grid(column=5, row=4)
    lb2 = Label(m, text="FROM").grid(column=1, row=5)
    p = Entry(m)
    p.grid(column=5, row=5)
    lb3 = Label(m, text="TO").grid(column=1, row=6)
    q = Entry(m)
    q.grid(column=5, row=6)
    lb4 = Label(m, text="DATE").grid(column=1, row=7)
    r = Entry(m)
    r.grid(column=5, row=7)
    def ct():
        op=Tk()
        an=p.get()
        bn=q.get()
        cn=r.get()
        if an==' ' or bn==' ' or cn==' ':
            tkMessageBox.showerror("OOPS","you can't leave any field empty")
        else:
            conn = sqlite3.connect('BUS_LIST.db')
            c = conn.cursor()

            c.execute("SELECT * FROM bb_bus WHERE D_FROM= ? AND A_TO = ?  ",(an,bn))
            conn.commit()
            ro=c.fetchall()
            row=6
            column=2
            for i in ro:
                for j in i:
                    qwerty=Label(op,text=j , bg="grey")
                    qwerty.pack(padx=5,pady=20,side=LEFT)
                column=column+3
                row=row+1

            print(ro)
            conn.close()
        op.mainloop()
    b1 = Button(m, text="Home", command=m.destroy,font="bold 13 ").grid(column=4,row=11,sticky='W')
    b2 = Button(m, text="Search", command=ct,font="bold 13 ").grid(column=5, row=11)
    m.mainloop()

Button(root,text='Add Bus',command=add ,font="bold 10").grid(row=10,column=2)
Button(root,text='Search Bus',command=search , font="bold 10").grid(row=10,column=6)


conn.commit()
conn.close()
root.mainloop()
