import tkinter as tk
import math

class Proje2():
    def __init__(self):
        self.root = tk.Tk()
        self.lb1=tk.Listbox(self.root,width=50,height=25)
        self.lb1.grid(row=0,column=0,rowspan=10)

        self.value=tk.IntVar(value=0)
        self.formul=[]
        option1=tk.Radiobutton(self.root,text="MATRİS 4x4",variable=self.value, value=1)
        option1.grid(row=3,column=1)
        option2=tk.Radiobutton(self.root,text="MATRİS 10x10",variable=self.value, value=2,)
        option2.grid(row=4,column=1)

        buton1=tk.Button(self.root,text="ONAYLA",width=15,command=self.GaussYokEtme)
        buton1.grid(row=6,column=1)


        tk.mainloop()


    def GaussYokEtme(self):
        def Formul():
            if(self.value==0):
                tk.Message("Lütfen bir matris seçiniz...")
            elif(self.value==1):
                self.formul=[]
            elif(self.value==2):
                self.formul=[]
        def SatırYerDegistirme():
            



        
basla=Proje2()