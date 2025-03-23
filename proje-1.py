import tkinter as tk
class Proje1():
    
    def Main(self):
        #bir arayüz başlatalım
        self.root=tk.Tk()
        self.root.config(bg="#FFFFF0")

        self.r1=tk.IntVar(value=0)
        
        frame=tk.Frame(self.root,bd=2,relief="groove",padx=5,pady=10,bg="lightyellow")
        frame.grid(row=1,column=0,rowspan=4)
        #başlık ekledim
        header=tk.Label(self.root,text="Nümerik Proje #1",font=("normal",18,"bold"),bg="#FFFFF0")
        header.grid(row=0,column=1)
        #yöntem seçimi için radio button kullanmaya karar kıldım.
        
        d1= tk.Radiobutton(frame,text="Aralık Yarılama",variable= self.r1,value=1,bg="lightyellow") 
        d1.grid(row=1,column=0,sticky="w")
        d2=tk.Radiobutton(frame,text="Newton-Raphson",variable=self.r1,value=2,bg="lightyellow")  
        d2.grid(row=2,column=0,sticky="w")
        d3=tk.Radiobutton(frame,text="Sekant Yöntemi",variable=self.r1,value=3,bg="lightyellow")   
        d3.grid(row=3,column=0,sticky="w")

        #Radio buttonda seçilen seçeneğe göre formülleri göstermemiz gerekecek. Bunun için entry kullanmak istedim
        self.formul1=tk.StringVar()
        self.formul1.set("Formül 1")
        self.formul2=tk.StringVar()
        self.formul2.set("Formül 2")

        e1=tk.Entry(self.root,state="readonly",textvariable=self.formul1)
        e1.grid(row=1,column=2)
        e2=tk.Entry(self.root,state="readonly",textvariable=self.formul2)
        e2.grid(row=2,column=2)
        
        #Butonla seçimimizi onaylayalım
        b1=tk.Button(self.root,text="Onayla",width=25,command=self.buttonOnay)
        b1.grid(row=4,column=2)

        #Butona basıldıktan sonra 2. ekran açılıp 2 ayrı lsitboxta sırayla işlemlerin adımlarını göstermesi lazım

        

        tk.mainloop()


    def buttonOnay(self):
        #ilk ekranı gizleyelim
        self.root.withdraw()
        #ikinci ekranı oluşturalım
        self.top=tk.Toplevel()
        self.top.title("Sonuç Ekranı")
        self.top.config(bg="#FFFFF0")

        #formülleri gösterelim
        self.f1=tk.Label(self.top,textvariable=self.formul1,bg="#FFFFF0")
        self.f1.grid(row=0,column=0)
        self.f2=tk.Label(self.top,textvariable=self.formul2,bg="#FFFFF0")
        self.f2.grid(row=0,column=1)

        #listbox oluşturacağım ki işlemleri gösterebileyim

        lb1=tk.Listbox(self.top)
        lb1.grid(row=1,column=0,padx=10,pady=10)
        lb2=tk.Listbox(self.top)
        lb2.grid(row=1,column=1,padx=10,pady=10)

        #buton oluşturup geri döndürelim
        bGeri=tk.Button(self.top,text="Geri Dön",width=25,command=self.geridon)
        bGeri.grid(row=2,column=1)

    def geridon(self):
        self.top.destroy()
        self.root.deiconify()


basla=Proje1()
basla.Main()