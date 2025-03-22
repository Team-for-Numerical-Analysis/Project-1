import tkinter as tk
def Main():
   
    UI()

def UI():
    #bir arayüz başlatalım
    root=tk.Tk()
    root.config(bg="#FFFFF0")
    
    frame=tk.Frame(root,bd=2,relief="groove",padx=5,pady=10,bg="lightyellow")
    frame.grid(row=1,column=0,rowspan=4)
    #başlık ekledim
    header=tk.Label(root,text="Nümerik Proje #1",font=("normal",18,"bold"),bg="#FFFFF0")
    header.grid(row=0,column=1)
    #yöntem seçimi için radio button kullanmaya karar kıldım.
    r1=tk.IntVar(value=0)
    d1= tk.Radiobutton(frame,text="Aralık Yarılama",variable=r1,value=1,bg="lightyellow") 
    d1.grid(row=1,column=0,sticky="w")
    d2=tk.Radiobutton(frame,text="Newton-Raphson",variable=r1,value=2,bg="lightyellow")  
    d2.grid(row=2,column=0,sticky="w")
    d3=tk.Radiobutton(frame,text="Sekant Yöntemi",variable=r1,value=3,bg="lightyellow")   
    d3.grid(row=3,column=0,sticky="w")

    #Radio buttonda seçilen seçeneğe göre formülleri göstermemiz gerekecek. Bunun için entry kullanmak istedim
    formul1=tk.StringVar()
    formul1.set("Formül 1")
    formul2=tk.StringVar()
    formul2.set("Formül 2")

    e1=tk.Entry(root,state="readonly",textvariable=formul1)
    e1.grid(row=1,column=2)
    e2=tk.Entry(root,state="readonly",textvariable=formul2)
    e2.grid(row=2,column=2)
    
    #Butonla seçimimizi onaylayalım
    b1=tk.Button(root,text="Onayla",width=25).grid(row=4,column=2)

    #Butona basıldıktan sonra 2. ekran açılıp 2 ayrı lsitboxta sırayla işlemlerin adımlarını göstermesi lazım

    tk.mainloop()

Main()