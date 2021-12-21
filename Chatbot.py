from tkinter import *
from tkinter import Tk, Label, Frame, Entry, Button, StringVar
from pyswip import Prolog
prolog = Prolog()
prolog.consult("kbase.pl")
window = Tk()
X=StringVar()
Y=StringVar()
Z=StringVar()
window.title("AI Project")
window.geometry('550x500')
photo = PhotoImage(file='Icon4.png',width=200,height=140)
label = Label(image=photo)
label.grid(column=2,row=0) 
lbl = Label(window, text="Artificial Intelligence Project",font=("Arial Bold", 30),fg = "light green",
		 bg = "dark green") 
lbl.grid(column=2, row=1)
lb2 = Label(window, text="Hi! Ask me something",font=("Arial Bold", 10),fg = "light blue",
		 bg = "dark blue") 
lb2.grid(column=2, row=2,padx=10, pady=10)
txt = Entry(window, textvariable=X,width=30) 
#X.set("defatult")
s=X.get()
txt.grid(column=2, row=5)
lb4 = Label(window,font=("Arial Bold", 10),fg = "black",
bg = "green",textvariable=Z) 
lb4.grid(column=2, row=7,padx=2, pady=2)
lb3 = Label(window,font=("Arial Bold", 10),fg = "light blue",
bg = "dark blue",textvariable=Y) 
lb3.grid(column=2, row=8,padx=2, pady=2)

def clicked(val):
    var1 = X.get()    
    if(X.get()=='hi'):
          for e in prolog.query("a(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
    elif(X.get()=='thanks'):
          for e in prolog.query("greet(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break   
    elif(var1.split(' ', 1)[0]=='my'):
        for e in prolog.query("b(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='i'):
        for e in prolog.query("c(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='1'):
        for e in prolog.query("d(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val) 
    elif(var1.split(' ', 1)[0]=='2'):
        Y.set("A.  FEF \n B.   ICRC\n C.   NTS\n D.   HEC \n E.   PM\n F.   Loan \n G.   Merit")
        Z.set("Scholerships categories");
        lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='fef'):
        for e in prolog.query("specific(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("FEF Portal");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='icrc'):
        for e in prolog.query("specific('icrc',Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("ICRC Portal");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='nts'):
        for e in prolog.query("specific('nts',Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("NTS Portal");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='hec'):
        for e in prolog.query("specific('hec',Y)"):
              X.set("")
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("HEC Portal");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='pm'):
        for e in prolog.query("specific('pm',Y)"):
              X.set("")
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("PM Portal");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='loan'):
        for e in prolog.query("specific('loan',Y)"):
              X.set("")
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("Loan Portal");
              break
              lb3.configure(text=val) 
    elif(var1.split(' ', 4)[1]=='criteria' and var1.split(' ', 4)[3]=='fef?'):
        for e in prolog.query("elg(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 4)[0]=='eligibility' and var1.split(' ', 4)[3]=='icrc?'):
        for e in prolog.query("elg1(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 4)[1]=='criteria' and var1.split(' ', 4)[3]=='nts?'):
        for e in prolog.query("elg2(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 4)[3]=='hec?'):
        for e in prolog.query("elg3(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 4)[3]=='pm?'):
        for e in prolog.query("elg4(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 4)[3]=='loan?'):
        for e in prolog.query("elg5(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              break
              lb3.configure(text=val)
   
    elif(var1.split(' ', 1)[0]=='how'):
        
        #X.set('how can i apply for these scholerships')
        for e in prolog.query("detail(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='what'):
        
        #X.set('what is the time Table of Student well being center?')
        for e in prolog.query("detail('what',Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set("Time Table of Well bieng center");
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='fef'):
        for e in prolog.query("spec(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='icrc'):
        for e in prolog.query("spec1(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)  
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='nts'):
        for e in prolog.query("spec2(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='hec'):
        for e in prolog.query("spec3(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val) 
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='pm'):
        for e in prolog.query("spec4(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    elif(var1.split(' ', 1)[0]=='specs' and var1.split(' ', 4)[2]=='loan'):
        for e in prolog.query("spec5(X,Y)"):
              print(e["Y"])
              Y.set(e["Y"]);
              Z.set(e["X"]);
              break
              lb3.configure(text=val)
    else:
           Y.set("Sorry Your input is wrong");        
            
   
    X.set("")
    
btn =Button(window, text="->",command= lambda:clicked(X.get())) 
btn.grid(column=2, row=6)          
window.mainloop()

