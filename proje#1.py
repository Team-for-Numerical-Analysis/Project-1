import tkinter as tk
def Main():
   
    UI()

def UI():
    #bir arayüz başlatalım
    root=tk.Tk()
    #başlık ekledim
    header=tk.Label(root,text="Nümerik Proje #1").grid(row=0,column=1)
    #yöntem seçimi için radio button kullanmaya karar kıldım.
    r1=tk.IntVar(value=0)

    tk.Radiobutton(root,text="Aralık Yarılama",variable=r1,value=1).grid(row=1,column=0)
    tk.Radiobutton(root,text="Newton-Raphson",variable=r1,value=2).grid(row=2,column=0)
    tk.Radiobutton(root,text="Sekant Yöntemi",variable=r1,value=3).grid(row=3,column=0)

    

    tk.mainloop()

Main()