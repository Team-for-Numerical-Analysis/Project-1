import tkinter as tk
import tkinter.messagebox as messagebox
import math
import tracemalloc
import time
class Proje3:
    def __init__(self):
        # Formül dy/dx = y*cos(x) + (x^2)
        #x(n+1) = x(n) + h , y(n+1) = y(n) + f(x(n),y(n))
        #x0 =0 , y0 =1 ,y(5) soruluyor, h=∆𝑥 ve farklı değerlere sahip

       
        
        self.ui()
        self.lb1.insert(tk.END,f"y(0) = {self.y} , x(0) = {self.x} , ∆𝑥 = {self.h}'dır. y(5) kaçtır?")
        
        
        

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

        root.mainloop()

    def buton(self,e):
        selection = self.lb2.curselection()
        self.h=self.lb2.get(selection[0])
        self.y=float(1)
        self.x=float(0)
        self.n=1
        self.euler()


    def euler(self):
        def f(x,y):
            return y * math.cos(x) + x**2
        tracemalloc.start()
        start=time.time()
        while(5>self.x):
            self.y = self.y + self.h * f(self.x,self.y)
            self.lb1.insert(tk.END,f"y({self.x}) değeri {self.y}'dir.")
            self.x = self.x + self.h
            self.lb1.insert(tk.END,f"x({self.n}) değeri {self.x}'dir.")
            self.n+=1

        #bitirmek için istenin y(target)değerini bulalım
        self.y=self.y+self.h*f(self.x,self.y)
        sonuç=self.y
        self.lb1.insert(tk.END,f"y({self.x}) değeri {self.y}'dir.")
        
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        stop=time.time()
        messagebox.showinfo("sonuç",f"geçen zaman={(stop-start):.5f} , Zirve bellek kullanımı: {peak / 1024:.2f} KB, y({self.x:.3f})={sonuç}")
           

Proje3()


