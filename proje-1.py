import tkinter as tk
import math
class Proje1():
    
    def Main(self):
        #bir arayüz başlatalım
        self.root=tk.Tk()
        self.root.config(bg="#FFFFF0")
        self.root.title("Nümerik Proje")
        self.root.resizable(False, False)
        frame=tk.Frame(self.root,bd=2,relief="groove",padx=5,pady=10,bg="lightyellow")
        frame.grid(row=1,column=0,rowspan=4)
        #başlık ekledim
        header=tk.Label(self.root,text="Nümerik Proje #1",font=("normal",18,"bold"),bg="#FFFFF0")
        header.grid(row=0,column=1)
        #yöntem seçimi için radio button kullanmaya karar kıldım.
        self.r1 = tk.IntVar(value=0)
        d1= tk.Radiobutton(frame,text="Aralık Yarılama",variable= self.r1,value=1,bg="lightyellow",command=self.EntryeYaz)
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
        b1.grid(row=4,column=2,padx=10,pady=6)

        #Butona basıldıktan sonra 2. ekran açılıp 2 ayrı lsitboxta sırayla işlemlerin adımlarını göstermesi lazım

        

        tk.mainloop()

    def EntryeYaz(self):
        if self.r1.get() == 1:
            self.formul1.set("e^-x * (2x+5x+2) + 1")
            self.formul2.set("cos(x)-x*e^x")
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

        self.lb1=tk.Listbox(self.top,width=50,height=20)
        self.lb1.grid(row=1,column=0,padx=10,pady=10)
        self.lb2=tk.Listbox(self.top,width=50,height=20)
        self.lb2.grid(row=1,column=1,padx=10,pady=10)
        #Hangi Yöntemin seçildiğine dair:
        if self.r1.get() == 1:
            self.AralikYarilama()

        #buton oluşturup geri döndürelim
        bGeri=tk.Button(self.top,text="Geri Dön",width=25,command=self.geridon)
        bGeri.grid(row=2,column=0,columnspan=3,pady=10)

    def geridon(self):
        self.top.destroy()
        self.root.deiconify()
    def AralikYarilama(self):
        #region Birinci Fonksiyon için.
        #Burada x Değerlerini Oluşturdum
        fBirHataDegeri = 1
        fBirxKucuk = 0
        fBirxBuyuk = -1
        fBirxOrtalama = 0
        Sayac = 1

        def AralikYarilamaFonksiyonBir(x):
            #Seçtiğim Fonksiyonun x'e göre sonucunu döndüren fonksiyonu oluşturdum
            return math.exp(-x) * (x ** 2 + 5 * x + 2) + 1

        #Hata değerimiz 0,001 den küçük olduğunda duracak.
        while fBirHataDegeri >= 0.001:
            #Her seferinde ilk olarak ortalama değeri buluyoruz.
            fBirxOrtalama = (fBirxKucuk + fBirxBuyuk) / 2
            # x değerlerini yazdırıyoruz.
            self.lb1.insert(tk.END, f"{Sayac}) Xa : {fBirxKucuk} Xb = {fBirxBuyuk} Xo ={fBirxOrtalama}")
            #her x değerini fonksiyonumuzda yerine koyup hesaplıyoruz.
            SonucBir = AralikYarilamaFonksiyonBir(fBirxKucuk)
            Sonucİki = AralikYarilamaFonksiyonBir(fBirxBuyuk)
            SonucUc = AralikYarilamaFonksiyonBir(fBirxOrtalama)
            #Fonksiyon sonuçlarını yazdırıyoruz.
            self.lb1.insert(tk.END, f"{Sayac}) Fa = {SonucBir} Fb = {Sonucİki} Fc = {SonucUc}")
            self.lb1.insert(tk.END, "--------------------------------")
            #Yöntem gereği eğer fonksiyon sonuçları aynı işarette ise X değerlerini değiştireceğiz bunun için aşağıdaki yöntemi kullandım
            if SonucUc * Sonucİki > 0:
                fBirxBuyuk = fBirxOrtalama
            else:
                fBirxKucuk = fBirxOrtalama
            if SonucBir < 0:
                SonucBir = SonucBir * -1
            if Sonucİki < 0:
                Sonucİki = Sonucİki * -1
            #Her Seferinde hata değerini hesaplıyoruz (Her seferinde Azalıyor)
            fBirHataDegeri = Sonucİki + SonucBir
            Sayac = Sayac+1
        #endregion
        #region
        # Burada x Değerlerini Oluşturdum
        fİkiHataDegeri = 1
        fİkixKucuk = 0
        fİkixBuyuk = 1
        fİkixOrtalama = 0
        Sayac = 1

        def AralikYarilamaFonksiyonİki(x):
            # Seçtiğim Fonksiyonun x'e göre sonucunu döndüren fonksiyonu oluşturdum
            return math.cos(x) - x * math.exp(x)

        # Hata değerimiz 0,001 den küçük olduğunda duracak.
        while fİkiHataDegeri >= 0.001:
            # Her seferinde ilk olarak ortalama değeri buluyoruz.
            fİkixOrtalama = (fİkixKucuk + fİkixBuyuk) / 2
            # x değerlerini yazdırıyoruz.
            self.lb2.insert(tk.END, f"{Sayac}) Xa : {fİkixKucuk} Xb = {fİkixBuyuk} Xo ={fİkixOrtalama}")
            # her x değerini fonksiyonumuzda yerine koyup hesaplıyoruz.
            SonucBir = AralikYarilamaFonksiyonİki(fİkixKucuk)
            Sonucİki = AralikYarilamaFonksiyonİki(fİkixBuyuk)
            SonucUc = AralikYarilamaFonksiyonİki(fİkixOrtalama)
            # Fonksiyon sonuçlarını yazdırıyoruz.
            self.lb2.insert(tk.END, f"{Sayac}) Fa = {SonucBir} Fb = {Sonucİki} Fc = {SonucUc}")
            self.lb2.insert(tk.END, "--------------------------------")
            # Yöntem gereği eğer fonksiyon sonuçları aynı işarette ise X değerlerini değiştireceğiz bunun için aşağıdaki yöntemi kullandım
            if SonucUc * Sonucİki > 0:
                fİkixBuyuk = fİkixOrtalama
            else:
                fİkixKucuk = fİkixOrtalama
            if SonucBir < 0:
                SonucBir = SonucBir * -1
            if Sonucİki < 0:
                Sonucİki = Sonucİki * -1
            # Her Seferinde hata değerini hesaplıyoruz (Her seferinde Azalıyor)
            fİkiHataDegeri = Sonucİki + SonucBir
            Sayac = Sayac + 1

basla=Proje1()
basla.Main()