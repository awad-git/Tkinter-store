from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
import csv
md=mysql.connector.connect(host='localhost',user='root',password='awad12345',database='construction')
cr=md.cursor()
class mainf :
    def __init__(self,master):
        self.master=master
        self.mf= Frame(master, bg='green')
        self.mf.place(width=600, height=500)
        self.button = Button(self.mf,text="خروج", fg="red",command=self.mf.destroy).grid(row=10,column=4)

w=Tk()
w.title('شركة السني للمقاولات')
w.geometry('600x500')
w.configure(bg='green')
w.resizable(False,False)
#creating the data base /tables
#cr.execute("CREATE DATABASE construction")
#cr.execute("CREATE TABLE customer (name char(20) not null,sort char not null,subsort char not null,quantity int not null,price int not null,cost int )")
#cr.execute("CREATE TABLE supplier (sname char (250) not null,ssort char(250) ,ssubsort char(250) ,squantity int not null,sprice int not null,scost int )")
##2cr.execute("CREATE TABLE supplier (sname char(20) not null,ssort char not null,ssubsort char not null,squantity int not null,sprice int not null,scost int ,stotal int,userid int AUTO_INCREMENT PRIMARY KEY)")
#cr.execute("CREATE TABLE classes (sortname char(250)) ")
#cr.execute("CREATE TABLE subclass (subsort char(250)) ")
#cr.execute("CREATE TABLE capacity (store int default 0,ssort char default NULL ,ssubsort char default NULL)")
#cr.execute("CREATE TABLE stock (store int default 0,ssort char default NULL ,ssubsort char )")
#cr.execute("CREATE TABLE balance (name char(250),debt int (250), pay int (250),rest int(250), date char (250))")
#cr.execute("CREATE TABLE supbalance (name char(250),debt int (250), pay int (250),rest int(250), date char (250))")
#cr.execute("DROP TABLE balance")
#cr.execute("DELETE FROM capacity");md.commit()
#cr.execute("ALTER TABLE   supplier MODIFY COLUMN ssubsort varchar(250)")
#cr.execute("ALTER TABLE   customer MODIFY COLUMN sort varchar(250)")
#cr.execute("ALTER TABLE   customer MODIFY COLUMN subsort varchar(250)")

#mf=mainf(w)

def addsubsort():
    newsubsort = sne1.get()
    #cr.execute("INSERT INTO subclass (subsort) VALUES (newsubsort)")
    # cursor.execute('INSERT INTO time(name, quantity, color)VALUES (%s, %s, %s)', (Name, Quantity, Color))
    cr.execute("INSERT INTO subclass (subsort) VALUES (%s)" ,(newsubsort,))
    #cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (0,NULL,newsubsort))
    cr.execute("SELECT * FROM subclass")
    print(cr.fetchall())
    md.commit()
    sne1.delete(0,END)
def addsort():
    newsort = sne.get()
    cr.execute("INSERT INTO classes (sortname) VALUES (%s)", (newsort,))
    #cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (0, newsort,NULL ))
    cr.execute("SELECT * FROM classes")
    print(cr.fetchall())
    md.commit()
    sne.delete(0,END)
def addsnf():
    global sne,sne1
    global newsort
    newsort=StringVar()
    global newsubsort
    newsubsort=StringVar()
    addsn=mainf(w)
    snlabel=Label(addsn.mf,text='اسم الصنف',fg='black').grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10)
    sne=Entry(addsn.mf,textvariable=newsort)
    newsort=sne.get()
    sne.grid(row=0,column=1,padx=5,pady=5,ipadx=10,ipady=10)
    snlabel1= Label(addsn.mf, text='اسم الفئة', fg='black').grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    sne1= Entry(addsn.mf,textvariable=newsubsort)
    newsubsort=sne1.get()
    sne1.grid(row=2, column=1, padx=5, pady=5, ipadx=10, ipady=10)
    snsave = Button(addsn.mf, text='اضافة فئة', fg='black',command=addsubsort).grid(row=5, column=3, padx=5, pady=5, ipadx=10, ipady=10)
    snsave1= Button(addsn.mf, text='اضافة صنف', fg='black',command=addsort).grid(row=5, column=5, padx=5, pady=5, ipadx=10, ipady=10)

def savesup():
    svsuplist = [spe0.get(), spcsnf.get(), spfea.get(), spe1.get(), spe2.get(), spe3.get()]
    cr.execute("INSERT INTO supplier VALUES (%s,%s,%s,%s,%s,%s)",svsuplist)
    md.commit()
    cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (spe1.get(), spcsnf.get(), spfea.get()))
    md.commit()

    cr.execute("SELECT * FROM  capacity  WHERE  ssort=%s AND ssubsort=%s", (spcsnf.get(), spfea.get()))
    summition = []
    for i in cr.fetchall():
        summition.append(i[0])
    totall = sum(summition)
    print('the summ is ', totall)
    cr.execute("DELETE FROM capacity WHERE  ssort=%s AND ssubsort=%s", (spcsnf.get(), spfea.get()))
    cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (totall, spcsnf.get(), spfea.get()))
    md.commit()
    #check if capacity table is empty
    #a=cr.execute("SELECT count(store) FROM capacity")
    '''
    try:
        cr.execute("SELECT * FROM capacity WHERE ssort=%s AND ssubsort=%s ",(spcsnf.get(), spfea.get()))
        c=[]
        for j in cr.fetchall():
                c.append(j[0])
        return c
        s1=sum(c)
        cr.execute("UPDATE capacity SET store=store+%s WHERE ssort=%s AND ssubsort=%s ",(s1, spcsnf.get(), spfea.get()))
        md.commit()
        # cr.execute("SELECT * FROM capacity")
        #print(cr.fetchall())
        #cr.execute("INSERT INTO capacity VALUES (%s+store ,%s,%s) WHERE ssort=%s AND ssubsort=%s ",(spe1.get(), spcsnf.get(), spfea.get(), spcsnf.get(), spfea.get()))

    except:
            cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)",(spe1.get(), spcsnf.get(), spfea.get()))
            md.commit()
    finally:
           pass '''
    spe0.delete(0,END)
    #spcsnf.delete(0, END)
    #spfea.delete(0, END)
    spe1.delete(0, END)
    spe2.delete(0, END)
    spe3.delete(0, END)
def suptrans():
    translist = [cs1.get(), cs2.get(), cs3.get(), es1.get(), es2.get(), es3.get()]
    cr.execute("INSERT INTO supplier VALUES (%s,%s,%s,%s,%s,%s)", translist);md.commit()
    cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (es1.get(), cs2.get(), cs3.get()));md.commit()
    cr.execute("SELECT * FROM  capacity  WHERE  ssort=%s AND ssubsort=%s",(cs2.get(), cs3.get()))
    summition =[]
    for i in cr.fetchall():
        summition.append(i[0])
    totall=sum(summition)
    print('the summ is ',totall)
    cr.execute("DELETE FROM capacity WHERE  ssort=%s AND ssubsort=%s",(cs2.get(), cs3.get()));md.commit()
    cr.execute("INSERT INTO  capacity  VALUES (%s,%s,%s)",(totall,cs2.get(), cs3.get()))
    md.commit()
    '''
    #a=cr.execute("SELECT count(store) FROM capacity")

    #if a > 0:
    try:
            cr.execute("SELECT * FROM capacity WHERE ssort=%s AND ssubsort=%s ",(cs2.get(), cs3.get()))
            B=[]
            for i in cr.fetchall():
                B.append(i[0])
            return B
            s=sum(B)
            cr.execute("UPDATE capacity SET store=store+%s WHERE ssort=%s AND ssubsort=%s ",(s, cs2.get(), cs3.get()))
            md.commit()
            # cr.execute("SELECT * FROM capacity")
            # print(cr.fetchall())

    except:
            cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (es1.get(), cs2.get(), cs3.get()))
            md.commit()
    finally:
         pass
        #cr.execute("INSERT INTO capacity VALUES (%s,%s,%s)", (es1.get(), cs2.get(), cs3.get())); md.commit()'''
    #cs1.delete(0,END)
    #cs2.delete(0, END)
    #cs3.delete(0, END)
    es1.delete(0, END)
    es2.delete(0, END)
    es3.delete(0, END)
def combosupsnf():
    cr.execute("SELECT * FROM classes ")
    snfdata=[]
    for row in cr.fetchall():
        snfdata.append(row[0])
    return snfdata
    print(cr.fetchall())
def combosubsort():
    cr.execute("SELECT * FROM subclass ")
    subsortdata = []
    for row in cr.fetchall():
        subsortdata.append(row[0])
    return subsortdata
    print(cr.fetchall())
def addsup():
    adds=mainf(w)
    global spe0,spe1,spe2,spe3
    global spcsnf,spfea
    spcsnf=StringVar()
    spfea=StringVar()
    spl0=Label(adds.mf,text='اسم المورد',fg='black').grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10)
    spe0=Entry(adds.mf)
    spe0.grid(row=0, column=1, padx=10, pady=10)
    spl1= Label(adds.mf, text='الصنف', fg='black').grid(row=1, column=0, padx=5, pady=5,ipadx=10,ipady=10)
    spc0= ttk.Combobox(adds.mf,textvariable=spcsnf)
    spc0.grid(row=1, column=1, padx=5, pady=5)
    spc0['values']=combosupsnf()
    #spc0['values']=spcval() a=spc0['values']
    spl2= Label(adds.mf, text='الفئة', fg='black').grid(row=2, column=0, padx=5, pady=5,ipadx=10,ipady=10)
    spc1= ttk.Combobox(adds.mf,textvariable=spfea)
    spc1.grid(row=2, column=1, padx=10, pady=10)
    spc1['values']=combosubsort()
    spl3= Label(adds.mf, text='الكمية', fg='black').grid(row=3, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    spe1= Entry(adds.mf)
    spe1.grid(row=3, column=1, padx=10, pady=10)
    spl4= Label(adds.mf, text='السعر للفئة-الطن', fg='black').grid(row=4, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    spe2= Entry(adds.mf)
    spe2.grid(row=4, column=1,padx=10, pady=10)
    def sumprice():
        spe3.delete(0, END)
        tklfa=int(spe1.get())*int(spe2.get())
        spe3.insert(END,tklfa)
    spl5= Button(adds.mf, text='التكلفة', fg='red',bg='blue',command=sumprice).grid(row=5, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    spe3= Entry(adds.mf)
    spe3.grid(row=5, column=1, padx=10, pady=10)
    svsuplist=[spe0.get(),spcsnf.get(),spfea.get(),spe1.get(),spe2.get(),spe3.get()]
    ssave= Button(adds.mf,command=savesup, text='حفظ').grid(row=10, column=2, padx=5, pady=5, ipadx=10, ipady=10)

    #home=Button(w, text='رجوع',command=adds.home).grid(row=10, column=3, padx=5, pady=5, ipadx=10, ipady=10)
def combosuppliers():
    cr.execute("SELECT* FROM supplier")
    supplist=[]
    for i in (cr.fetchall()):
        supplist.append(i[0])
    cosup=set(supplist)
    supplist1=list(cosup)
    return supplist1
def supply():
    global cs1,cs2,cs3,es1,es2,es3
    s=mainf(w)
    ls1=Label(s.mf,text='اسم المورد',fg='black').grid(row=0,column=0,padx=5,pady=5,ipadx=10,ipady=10)
    cs1=ttk.Combobox(s.mf)
    cs1.grid(row=0, column=1, padx=10, pady=10)
    cs1['values']=combosuppliers()
    ls2= Label(s.mf, text='الصنف', fg='black').grid(row=1, column=0, padx=5, pady=5,ipadx=10,ipady=10)
    cs2= ttk.Combobox(s.mf)
    cs2.grid(row=1, column=1, padx=5, pady=5)
    cs2['values']=combosupsnf()
    ls3= Label(s.mf, text='الفئة', fg='black').grid(row=2, column=0, padx=5, pady=5,ipadx=10,ipady=10)
    cs3= ttk.Combobox(s.mf)
    cs3.grid(row=2, column=1, padx=10, pady=10)
    cs3['values']=combosubsort()
    ls4= Label(s.mf, text='الكمية', fg='black').grid(row=3, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    es1= Entry(s.mf)
    es1.grid(row=3, column=1, padx=10, pady=10)
    ls5= Label(s.mf, text='السعر للفئة-الطن', fg='black').grid(row=4, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    es2= Entry(s.mf)
    es2.grid(row=4, column=1,padx=10, pady=10)
    def suptklfa():
        es3.delete(0, END)
        supcost=int(es1.get())*int(es2.get())
        es3.insert(END,supcost)
    ls6= Button(s.mf, text='التكلفة', fg='red',command=suptklfa,bg='blue').grid(row=5, column=0, padx=10, pady=10,ipadx=10,ipady=10)
    es3 = Entry(s.mf)
    es3.grid(row=5, column=1, padx=10, pady=10)
    bsa=Button(s.mf,text='اضافة مورد',command=addsup).grid(row=10,column=4,padx=5,pady=5,ipadx=10,ipady=10)
    bsd=Button(s.mf, text='اضافة صنف/فئة',command=addsnf).grid(row=10, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    #bsd1= Button(s.mf, text='اضافة فئة',command=addsnf).grid(row=10, column=1, padx=5, pady=5, ipadx=10, ipady=10)
    ssave= Button(s.mf, text='حفظ',command=suptrans).grid(row=10, column=2, padx=5, pady=5, ipadx=10, ipady=10)
    home = Button(s.mf, text='الرئيسية', command=s.mf.destroy).grid(row=10, column=3, padx=5, pady=5, ipadx=10, ipady=10)
def savecst():
    newcst=[ec0.get(),cc0.get(),cc1.get(),ec1.get(),ec2.get(),ec3.get()]
    cr.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s)",newcst);md.commit()
    cr.execute("SELECT store FROM capacity WHERE ssort=%s AND ssubsort=%s ",(cc0.get(),cc1.get()))
    csf2=cr.fetchall()
    print(csf2)
    remain2=int(csf2[0][0])-int(ec1.get())
    try:
        cr.execute("UPDATE capacity SET store=%s WHERE ssort=%s AND ssubsort=%s ",(remain2,cc0.get(),cc1.get()));md.commit()
    finally:
        pass
        #cr.execute("INSERT INTO capacity VALUES(%s,%s,%s)", (ec1.get(), cc0.get(), cc1.get()))
        #md.commit()'''
    ec0.delete(0,END)
    #cc1.delete(0, END)
    ec1.delete(0, END)
    ec2.delete(0, END)
    ec3.delete(0, END)
def addcst():
    global ec0,cc0,cc1,ec1,ec2,ec3
    global cstsn ,cstfe
    cstfe=StringVar()
    cstsn=StringVar()
    addc=mainf(w)
    lc0= Label(addc.mf, text='اسم العميل', fg='black').grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    ec0= Entry(addc.mf)
    ec0.grid(row=0, column=1, padx=10, pady=10)
    lc1 = Label(addc.mf, text='الصنف', fg='black').grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    cc0 = ttk.Combobox(addc.mf,textvariable=cstsn)
    cc0.grid(row=1, column=1, padx=5, pady=5)
    cc0['values']=combosupsnf()
    lc2 = Label(addc.mf, text='الفئة', fg='black').grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    cc1 = ttk.Combobox(addc.mf,textvariable=cstfe)
    cc1.grid(row=2, column=1, padx=10, pady=10)
    cc1['values']=combosubsort()
    lc3= Label(addc.mf, text='الكمية', fg='black').grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=10)
    ec1 = Entry(addc.mf)
    ec1.grid(row=3, column=1, padx=10, pady=10)
    lc4 = Label(addc.mf, text='السعر للفئة-الطن', fg='black').grid(row=4, column=0, padx=10, pady=10, ipadx=10,
                                                                    ipady=10)
    ec2 = Entry(addc.mf)
    ec2.grid(row=4, column=1, padx=10, pady=10)
    def cstklf():
        ec3.delete(0,END)
        ec3.insert(END,int(ec1.get())*int(ec2.get()))
    lc5 = Button(addc.mf, text='التكلفة', fg='red',command=cstklf, bg='blue').grid(row=5, column=0, padx=10, pady=10, ipadx=10,
                                                                     ipady=10)
    ec3 = Entry(addc.mf)
    ec3.grid(row=5, column=1, padx=10, pady=10)
    csave = Button(addc.mf,command=savecst, text='حفظ').grid(row=10, column=2, padx=5, pady=5, ipadx=10, ipady=10)
def savecustomer():
    customert=[csc1.get(),csc2.get(),csc3.get(),cse1.get(),cse2.get(),cse3.get()]
    cr.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s)",customert);md.commit()
    cr.execute("SELECT store FROM capacity WHERE  ssort=%s AND ssubsort=%s", (csc2.get(), csc3.get()))
    csf=cr.fetchall()
    print(csf)
    remain=int(csf[0][0])-int(cse1.get())
    cr.execute("UPDATE capacity SET store=%s WHERE  ssort=%s AND ssubsort=%s", (remain,csc2.get(), csc3.get()))
    '''
    cr.execute("SELECT store FROM capacity WHERE  ssort=%s AND ssubsort=%s",(csc2.get(),csc3.get()))
    cstf=[]
    for i in cr.fetchall():
        cstf.append(i[0])
    sumcstf=sum(cstf)
    rem1=sumcstf-int(cse1.get())
    print(rem1)
    #cr.execute("DELETE FROM capacity WHERE ssort=%s AND ssubsort=%s",(csc2.get(),csc3.get())));md.commit()
    #cr.execute("INSERT INTO capacity VALUES (%s,%s,%s) ",(rem1,csc2.get(),csc3.get()))
    md.commit() '''
    #csc1.delete(0,END)
    #csc2.delete(0, END)
    #csc3.delete(0, END)
    cse1.delete(0, END)
    cse2.delete(0, END)
    cse3.delete(0, END)
def combocst():
    cr.execute("SELECT * FROM customer")
    cl=[]
    for i in (cr.fetchall()):
        cl.append(i[0])
    cocust=set(cl)
    cstlist=list(cocust)
    return cstlist
def customers():
    cst=mainf(w)
    global csc1,csc2,csc3,cse1,cse2,cse3
    csl1= Label(cst.mf, text='اسم العميل', fg='black').grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    csc1 = ttk.Combobox(cst.mf)
    csc1.grid(row=0, column=1, padx=10, pady=10)
    csc1['values']=combocst()
    csl2 = Label(cst.mf, text='الصنف', fg='black').grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    csc2 = ttk.Combobox(cst.mf)
    csc2.grid(row=1, column=1, padx=5, pady=5)
    csc2['values']=combosupsnf()
    csl3 = Label(cst.mf, text='الفئة', fg='black').grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    csc3 = ttk.Combobox(cst.mf)
    csc3.grid(row=2, column=1, padx=10, pady=10)
    csc3['values']=combosubsort()
    csl4 = Label(cst.mf, text='الكمية', fg='black').grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=10)
    cse1 = Entry(cst.mf)
    cse1.grid(row=3, column=1, padx=10, pady=10)
    csl5 = Label(cst.mf, text='السعر للفئة-الطن', fg='black').grid(row=4, column=0, padx=10, pady=10, ipadx=10, ipady=10)
    cse2 = Entry(cst.mf)
    cse2.grid(row=4, column=1, padx=10, pady=10)
    def cstklfa():
        cse3.delete(0, END)
        tklfa=int(cse1.get())*int(cse2.get())
        cse3.insert(END,tklfa)
    csl6 = Button(cst.mf, command=cstklfa,text='التكلفة', fg='red', bg='blue').grid(row=5, column=0, padx=10, pady=10, ipadx=10, ipady=10)
    cse3 = Entry(cst.mf)
    cse3.grid(row=5, column=1, padx=10, pady=10)

    bcs1 = Button(cst.mf, text='اضافة عميل', command=addcst).grid(row=10, column=4, padx=5, pady=5, ipadx=10, ipady=10)
    #bcs2 = Button(cst.mf, text='حذف عميل').grid(row=10, column=0, padx=5, pady=5, ipadx=10, ipady=10)
    #bcs3 = Button(cst.mf, text='معاملة جديدة').grid(row=10, column=1, padx=5, pady=5, ipadx=10, ipady=10)
    csave = Button(cst.mf,command=savecustomer, text='حفظ').grid(row=10, column=2, padx=5, pady=5, ipadx=10, ipady=10)
    home = Button(cst.mf, text='الرئيسية', command=cst.mf.destroy).grid(row=10, column=3, padx=5, pady=5, ipadx=10,ipady=10)

def cstsearch():
        custe1.delete(0,END)
        custe2.delete(0,END)
        custe3.delete(0,END)
        cr.execute("INSERT INTO balance VALUES(%s,%s,%s,%s,%s)",(cusco.get(),0,0,0,0));md.commit()
        cr.execute("SELECT SUM(pay) FROM balance WHERE name=%s",(cusco.get(),))
        rest=cr.fetchall()
        remaining=int(rest[0][0])
        cr.execute("DELETE FROM balance WHERE debt=%s AND name=%s AND rest=%s",(0,cusco.get(),0));md.commit()
        cr.execute("SELECT SUM(cost) FROM customer WHERE name=%s ", (cusco.get(),))
        cscos = cr.fetchall()
        print(cscos[0][0])
        cuscost = int(cscos[0][0])
        totalrest=cuscost-remaining
        custe1.insert(END, totalrest)
        tree = mainf(w)
        tv = ttk.Treeview(tree.mf, columns=(1, 2, 3), show='headings', height='10')
        tv.grid(row=1, column=0)
        tv.heading(1, text='الحساب')
        tv.heading(2, text='الصنف')
        tv.heading(3, text='الفئة')
        #tv.heading(4, text='الكمية')
        #tv.heading(5, text='السعر')
        #tv.heading(6, text='الحساب')
        cr.execute("SELECT cost,sort,subsort FROM customer WHERE name=%s ",(cusco.get(),))
        for row in cr.fetchall():
            tv.insert('', 'end', values=row)
        home = Button(tree.mf, text='الرئيسية', command=tree.mf.destroy).grid(row=0, column=0, padx=5, pady=5,
                                                                            ipadx=10, ipady=10)

def savepay():
    if messagebox.askyesno("وحفظ","تاكيد حفظ السداد"):
        cr.execute("INSERT INTO balance VALUES (%s,%s,%s,%s,%s)",(cusco.get(),custe1.get(),custe2.get(),custe3.get(),time.ctime()))
        md.commit()
        custe1.delete(0,END)
        custe2.delete(0,END)
        custe3.delete(0,END)
    cr.execute("SELECT * from balance")
    print(cr.fetchall())
def cstpayrep(resultcst):
    with open(r'C:\العملاء.csv','a') as f:
            w = csv.writer(f, dialect='excel')
            for record in resultcst:
                w.writerow(record)
def cstpay():
    pay=custe1.get()
    rem=int(pay)-int(custe2.get())
    custe3.delete(0,END)
    custe3.insert(END,rem)
def cstdelet():
    if messagebox.askyesno("حذف", "تاكيد حذف العميل"):
        cr.execute("DELETE FROM customer WHERE name =%s",(cusco.get(),));md.commit()
def cust():
    global cusco
    global custe1
    global custe2
    global custe3
    cusname=StringVar()
    cust=mainf(w)
    custl1=Label(cust.mf,text='اختر العميل').grid(row=2, column=0, padx=10, pady=10)
    cusco= ttk.Combobox(cust.mf,textvariable=cusname)
    cusco.grid(row=2, column=1, padx=10, pady=10)
    cusco['values']=combocst()
    custb1=Button(cust.mf,text='بحث',fg='blue',command=cstsearch).grid(row=2, column=3, padx=10, pady=10)
    custbd = Button(cust.mf, text='حذف', fg='blue',bg='red',command=cstdelet).grid(row=2, column=4, padx=10, pady=10)
    custl2=Label(cust.mf,text='الحساب',fg='black').grid(row=3, column=0, padx=10, pady=10)
    custe1=Entry(cust.mf)
    custe1.grid(row=3, column=1, padx=10, pady=10)
    custb2=Button(cust.mf, text='سداد', fg='black',bg='yellow',command=cstpay).grid(row=4, column=0, padx=10, pady=10)
    custe2 = Entry(cust.mf)
    custe2.grid(row=4, column=1, padx=10, pady=10)
    custl3=Label(cust.mf, text='متبقي', fg='black').grid(row=5, column=0, padx=10, pady=10)
    custe3 = Entry(cust.mf)
    custe3.grid(row=5, column=1, padx=10, pady=10)
    savpay = Button(cust.mf,command=savepay,text='حفظ').grid(row=8,column=0,padx=5,pady=5,ipadx=10,ipady=10)
    cr.execute("SELECT * FROM customer WHERE name =%s",(cusco.get(),))
    resultcst=cr.fetchall()
    savpay = Button(cust.mf, command=lambda :cstpayrep(resultcst), text='تقرير').grid(row=8, column=2, padx=5, pady=5, ipadx=10, ipady=10)

def provser():
    proe1.delete(0,END)
    proe2.delete(0,END)
    proe3.delete(0,END)
    cr.execute("INSERT INTO supbalance VALUES (%s,%s,%s,%s,%s)",(proco.get(),0,0,0,0));md.commit()
    cr.execute("SELECT SUM(pay) FROM supbalance WHERE name=%s",(proco.get(),))
    res=cr.fetchall()
    res2=int(res[0][0])
    cr.execute("DELETE FROM supbalance WHERE debt=%s AND name=%s AND rest=%s",(0,proco.get(),0))
    cr.execute("SELECT SUM(scost) FROM supplier WHERE sname=%s",(proco.get(),))
    ssum=cr.fetchall()
    costsum=int(ssum[0][0])
    totalrem=costsum-res2
    proe1.insert(END,totalrem)
    trees=mainf(w)
    tv = ttk.Treeview(trees.mf, columns=(1, 2, 3), show='headings', height='10')
    tv.grid(row=1, column=0)
    tv.heading(1, text='الحساب')
    tv.heading(2, text='الصنف')
    tv.heading(3, text='الفئة')
    cr.execute("SELECT scost,ssort,ssubsort FROM supplier WHERE sname=%s ",(proco.get(),))
    for j in cr.fetchall():
        tv.insert('','end',values=j)
    home = Button(trees.mf, text='الرئيسية', command=trees.mf.destroy).grid(row=0, column=0, padx=5, pady=5,
                                                                          ipadx=10, ipady=10)
def supay():
    spay=int(proe1.get())
    putrem=spay-int(proe2.get())
    proe3.delete(0,END)
    proe3.insert(END,putrem)
def supreport(supresult):
    with open(r'C:\الموردون.csv','a') as f:
            w = csv.writer(f, dialect='excel')
            for record in supresult:
                w.writerow(record)
def suprepay():
    if messagebox.askyesno("وحفظ","تاكيد حفظ السداد"):
        cr.execute("INSERT INTO supbalance VALUES (%s,%s,%s,%s,%s)",(proco.get(),proe1.get(),proe2.get(),proe3.get(),time.ctime()))
        md.commit()
        proe1.delete(0, END)
        proe2.delete(0, END)
        proe3.delete(0, END)
def supdelet():
    if messagebox.askyesno("حذف", "تاكيد حذف المورد"):
        cr.execute("DELETE FROM supplier WHERE sname=%s",(proco.get(),));md.commit()
def provid():
    global proco
    global proe1
    global proe2
    global proe3
    proev=StringVar()
    prov=mainf(w)
    prol1=Label(prov.mf,text='اختر المورد').grid(row=2, column=0, padx=10, pady=10)
    proco= ttk.Combobox(prov.mf)
    proco.grid(row=2, column=1, padx=10, pady=10)
    proco['values']=combosuppliers()
    prob1=Button(prov.mf,text='بحث',fg='blue',command=provser).grid(row=2, column=3, padx=10, pady=10)
    prod = Button(prov.mf, text='حذف', fg='blue',bg='red',command=supdelet).grid(row=2, column=4, padx=10, pady=10)
    prol2=Label(prov.mf,text='الحساب',fg='black').grid(row=3, column=0, padx=10, pady=10)
    proe1=Entry(prov.mf,textvariable=proev)
    proe1.grid(row=3, column=1, padx=10, pady=10)
    prob2=Button(prov.mf, text='سداد', fg='black',bg='yellow',command=supay).grid(row=4, column=0, padx=10, pady=10)
    proe2 = Entry(prov.mf)
    proe2.grid(row=4, column=1, padx=10, pady=10)
    prol3=Label(prov.mf, text='متبقي', fg='black').grid(row=5, column=0, padx=10, pady=10)
    proe3 = Entry(prov.mf)
    proe3.grid(row=5, column=1, padx=10, pady=10)
    sbuton=Button(prov.mf,text='حفظ',fg='black',command=suprepay).grid(row=8,column=0,padx=5,pady=5,ipadx=10,ipady=10)
    cr.execute("SELECT * FROM supplier WHERE sname=%s",(proco.get(),))
    supresult=cr.fetchall()
    repbut= Button(prov.mf, command=lambda: supreport(supresult), text='تقرير').grid(row=8, column=2, padx=5, pady=5,
                                                                                      ipadx=10, ipady=10)


def accounting():
    ac=mainf(w)
    acb1=Button(ac.mf,text='العملاء',bg='yellow',command=cust).grid(row=15, column=10, ipadx=20, ipady=20, padx=50, pady=5)
    acb2=Button(ac.mf,text='الموردون',bg='yellow',command=provid).grid(row=10, column=10, ipadx=20, ipady=20, padx=50,pady=5)
def storage():
    tree=mainf(w)
    tv=ttk.Treeview(tree.mf,columns=(1,2,3),show='headings',height='20')
    tv.grid(row=1,column=0,padx=5,pady=5)
    tv.heading(1,text='المتبقي')
    tv.heading(2,text='النوع')
    tv.heading(3,text='الفئة')
    home = Button(tree.mf, text='الرئيسية', command=tree.mf.destroy).grid(row=0, column=0, padx=5, pady=5)
    #md = mysql.connector.connect(host='localhost', user='root', password='awad12345', database='construction')
    #cr = md.cursor()
    cr.execute('SELECT * FROM capacity')
    rows=cr.fetchall()
    allrows=cr.rowcount
    print('total entries '+str(+allrows))
    for i in rows:
        tv.insert('','end',values=i)
def storage2():
    cr.execute("SELECT * FROM classes")
    storagelist=[]
    for i in cr.fetchall():
        storagelist.append(i[0])
    print(storagelist)
    cr.execute("SELECT * FROM subclass")
    storagl2=[]
    for j in cr.fetchall():
        storagl2.append(j[0])
    print(storagl2)
    ##TREEVEIW
    tree=mainf(w)
    tv=ttk.Treeview(tree.mf,columns=(1,2,3),show='headings',height='20')
    tv.grid(row=1,column=0,padx=5,pady=5)
    tv.heading(1,text='المتبقي')
    tv.heading(2,text='النوع')
    tv.heading(3,text='الفئة')
    home = Button(tree.mf, text='الرئيسية', command=tree.mf.destroy).grid(row=0, column=0, padx=5, pady=5)
    cr.execute("SELECT * FROM capacity WHERE  ssort=%s AND ssubsort=%s", (storagelist[0], storagl2[0]))
    #cr.execute("SELECT * FROM capacity WHERE  ssort=%s AND ssubsort=%s",(storagelist[0][0],storagl2[0][0]))
    sumall=[]
    for l in cr.fetchall():
        sumall.append(l[0])
        #tv.insert('', 'end', values=(storagelist[0][0], storagl2[0][0]), )
    y=0
    z=0
    for r in range(100):
        ww=[]
        cr.execute("SELECT * FROM capacity WHERE  ssort=%s AND ssubsort=%s", (storagelist[y], storagl2[z]))
        #for m in cr.fetchall():
        #tv.insert('', 'end', values=(storagelist[y], storagl2[z], 9))
        y+=1
        z+=1
    #for i in ww:
    #   tv.insert('', 'end', values=(ww[i],), 9))
    return sum(sumall)
    print(sum(sumall))

b1 = Button(w, text='مشتريات', bg='blue',command=supply).grid(row=25, column=10, ipadx=20, ipady=20, padx=50,
                                                                          pady=5)
b2 = Button(w, text='مبيعات', bg='springgreen',command=customers).grid(row=20, column=15, ipadx=20, ipady=20, padx=50, pady=5)
b3 = Button(w, text='مخزن', bg='yellow',command=storage).grid(row=25, column=20, ipadx=20, ipady=20, padx=50, pady=5)
b4 = Button(w, text='حسابات', bg='turquoise',command=accounting).grid(row=30, column=15, ipadx=20, ipady=20, padx=50, pady=5)
w.mainloop()