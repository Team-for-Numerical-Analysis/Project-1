import tkinter as tk
import math as m


class Proje4:
    def __init__(self):

    #hlist , n , lb1 ,lb2 , root , lab1, lab2
    # f(x,y)=sin(x^2)-y^2 , x(0)=0 y(0)=1 , h=hlist
        self.x=0
        self.y=1


        
        self.ui()




    def ui(self):
        root=tk.Tk()
        lab1=tk.Label(root,text="∆x seçimi")
        lab1.grid(row=0,column=0)
        lab2=tk.Label(root,text="İşlemler")
        lab2.grid(row=0,column=1)
        self.lb1=tk.Listbox(root,width=40)
        self.lb1.grid(row=1,column=1) 
        self.selected=tk.StringVar
        hlist=[1.0,0.5,0.25,0.1,0.05,0.025,0.01,0.005]
        self.lb2=tk.Listbox(root)
        for item in hlist:
            self.lb2.insert(tk.END,item)
        self.lb2.bind('<<ListboxSelect>>',self.buton)
        self.lb2.grid(row=1,column=0)
        self.seçim = tk.StringVar(value="1")
        rb1=tk.Radiobutton(root,text="heun yöntemi",variable=self.seçim,value="1")
        rb2=tk.Radiobutton(root,text="midpoint yöntemi",variable=self.seçim,value="2")
        rb1.grid(row=2,column=0)
        rb2.grid(row=2,column=1)
        root.mainloop()
    
    def buton(self,e):
        selection = self.lb2.curselection()
        self.h=self.lb2.get(selection[0])
        self.rk2()
    
    def rk2(self):
        

        def f(x,y):
           return m.cos((x**2)+(y**2)) + m.log((x+1)**2,m.e) - y**3
        def midpoint(x,y):
            a=0.5
            b=0.5
            c1=0
            c2=1
            
            k1=f(x,y)
            self.lb1.insert(tk.END,f"k1 = {k1}")
            k2=f(x + self.h/2 , y + (self.h/2) * k1)
            self.lb1.insert(tk.END,f"k2 = {k2}")
            y_new=y+self.h*k2
            self.lb1.insert(tk.END,f"y = {y_new}")
            self.lb1.insert(tk.END,"**********************************")
            if(y_new-y<self.h):
                self.lb1.insert(tk.END,f"sonuç = {y_new}")
                return
            return midpoint(x+self.h,y_new)
        def heun(x,y):
            a=1
            b=1
            c1=0,5
            c2=0,5
            k1=f(x,y)
            self.lb1.insert(tk.END,f"k1 = {k1}")
            k2=f(x + self.h , x + self.h * k1)
            self.lb1.insert(tk.END,f"k2 = {k2}")
            y_new= y + (self.h/2)*(k1+k2)
            self.lb1.insert(tk.END,f"y = {y_new}")
            self.lb1.insert(tk.END,"**********************************")
            if(y_new - y < self.h):
                self.lb1.insert(tk.END,f"sonuç = {y_new}")
                return
            return heun(x + self.h , y_new)
 
        if self.seçim=="1":
            heun(self.x,self.y)
        else:
            midpoint(self.x,self.y)
        
Proje4()