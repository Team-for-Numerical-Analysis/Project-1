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
        d2=tk.Radiobutton(frame,text="Newton-Raphson",variable=self.r1,value=2,bg="lightyellow",command=self.EntryeYaz)
        d2.grid(row=2,column=0,sticky="w")
        d3=tk.Radiobutton(frame,text="Sekant Yöntemi",variable=self.r1,value=3,bg="lightyellow",command=self.EntryeYaz)   
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
        self.secim=self.r1.get()
        if self.secim == 1:
            self.formul1.set("e^-x * (2x+5x+2) + 1")
            self.formul2.set("cos(x)-x*e^x")
        if self.secim==2:
            self.formul1.set("(x^3) - (x^2) - 2")
            self.formul2.set("(x^4)-(8*(x^2))+16")
        if self.secim==3:
            self.formul1.set("(e^x) - (x^2)")
            self.formul2.set("(x^3) - 2*(x^2) + 4x - 8")
        
    def buttonOnay(self):
        #ilk ekranı gizleyelim
        self.root.withdraw()
        #ikinci ekranı oluşturalım
        self.top=tk.Toplevel()
        self.top.title("Sonuç Ekranı")
        self.top.config(bg="#FFFFF0")

        # Grid'in sütunlarını ve satırlarını genişletilebilir yap
        self.top.columnconfigure(0, weight=1)
        self.top.columnconfigure(1, weight=1)
        self.top.rowconfigure(0, weight=1)
        self.top.rowconfigure(1, weight=1)



        #formülleri gösterelim
        self.f1=tk.Label(self.top,textvariable=self.formul1,bg="#FFFFF0")
        self.f1.grid(row=0,column=0,sticky="nsew")
        self.f2=tk.Label(self.top,textvariable=self.formul2,bg="#FFFFF0")
        self.f2.grid(row=0,column=1,sticky="nsew")

        #listbox oluşturacağım ki işlemleri gösterebileyim

        self.lb1=tk.Listbox(self.top,width=50,height=20)
        self.lb1.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")
        self.lb2=tk.Listbox(self.top,width=50,height=20)
        self.lb2.grid(row=1,column=1,padx=10,pady=10,sticky="nsew")
        #Hangi Yöntemin seçildiğine dair:
        if self.secim == 1:
            self.AralikYarilama()
        if self.secim == 2:
            self.NewtonRaphson()
        if self.secim == 3:
            self.Sekant()

        #buton oluşturup geri döndürelim
        bGeri=tk.Button(self.top,text="Geri Dön",width=25,command=self.geridon)
        bGeri.grid(row=2,column=0,columnspan=3,pady=10,sticky="nsew")

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
            self.lb1.insert(tk.END, f"{Sayac}) Xa : ({fBirxKucuk}) Xb = ({fBirxBuyuk}) Xo =({fBirxOrtalama})")
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
            self.lb2.insert(tk.END, f"{Sayac}) Xa : ({fİkixKucuk}) Xb = ({fİkixBuyuk}) Xo =({fİkixOrtalama})")
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
    

    def NewtonRaphson(self):
        #x(k+1)=x(k)+(f(x(k))/f'(x(k))) döngü formülüdür ve f(x(k+1))<=E olursa durdurmamız lazım
        
        def f(x,formul):
            #verilen sayıya göre formülü getirecek
            if formul==1:
                return (x**3)-(2*(x**2))-2
            elif formul==2:
                return ((x**4)-8*(x**2) + 16)

        def ft(x,formul):
            #verilen sayıya göre fonksiyonun türevli halini verecek
            if formul==1:
                return (3*(x**2)-(4)*(x))
            elif formul==2:
                return ((4)*(x**3)-16*x)
        
        def yontem(x,formul):
            #formülün numarasına göre değişkenlere atanacak. her fonksiyon için ayrı birer metot yazmamıza gerek kalmadı
            if formul==1:
                lb=self.lb1
                fonk=self.formul1.get() # metotu tekrar tekrar çağırmak yerine bir değişkene atadım
                fonk_t=ft(x,formul)
            else:
                lb=self.lb2
                fonk=self.formul2.get()
                fonk_t=ft(x,formul)

            # değişkenler
            epsilon=0.0001            
            sayac=0
            #formülü ve diğer değişkenleri gösterdim
            lb.insert(tk.END,f"f(x) = {fonk} | x({sayac}) = {x} | E={epsilon}")
            lb.insert(tk.END,"-------------------------------------------------------")

            while(True):
                if(f(x,formul)>epsilon):
                    sonuc=x-((f(x,formul))/(ft(x,formul)))
                    lb.insert(tk.END,f"x({sayac}) = {x} - ({fonk}/{fonk_t}) = {sonuc}")
                    lb.insert(tk.END,"-------------------------------------------------------")
                    
                    #fonksiyon aynı değeri tekrar tekrar döndürmesin diye oluşturulmuş bir if bloğu
                    if f(sonuc,formul) == f(x,formul): 
                        lb.insert(tk.END,"f(x" +(sayac+1)+ f") = f(x{sayac}) olduğundan dolayı işlem tamamlanmıştır.")
                        lb.insert(tk.END, f"kök x = {x}'tir")
                        break
                    x=sonuc 
                else:
                    lb.insert(tk.END,f"f({x}) <= {epsilon} olduğundan")
                    lb.insert(tk.END,f"KÖK-> x = {x}'tir")
                    break
                sayac+=1        

        yontem(8,1)
        yontem(2.5,2)

    def Sekant(self):
        def f(x,fNo):
            if fNo==1:
                return ( math.exp(1) - (x**2) )
            else:
                return ((x**3) - 2*(x**2) + 4*x - 8)

        def Yontem(xEski,xYeni,fNo):
            # döngü denklemi x(k+1)=x(k)-f(x(k))*((x(k-1)-x(k))/f(x(k-1)-f(x(k))))
            if fNo==1:
                lb=self.lb1
                fonk=self.formul1.get()
            else:
                lb=self.lb2
                fonk=self.formul2.get()

            sayac=2
            epsilon=0.0001

            lb.insert(tk.END,f"x(0)={xEski} | x(1)={xYeni} | E={epsilon} | f(x)={fonk}")

            while(True):
                
                if f(xYeni,fNo) > epsilon:
                    sonuc=xYeni-f(xYeni,fNo)*((xEski-xYeni)/(f(xEski,fNo)-f(xYeni,fNo)))
                    lb.insert(tk.END,f"x({sayac})= {xYeni}-{f(xYeni,fNo)}*({xEski} - {xYeni} ) / (({f(xEski,fNo)}) - ({f(xYeni,fNo)})))")

                    if xYeni==sonuc:
                        lb.insert(f"Değişkenler değişmediğinden KÖK-> x={xYeni}'tir.")
                        break
                    
                    xEski=xYeni
                    xYeni=sonuc
                    sayac+=1
                else:
                    lb.insert(tk.END,f"f(x({sayac})) <= E olduğundan")
                    lb.insert(tk.END,f"KÖK-> x = {xYeni}'tir.")
                    break
        
        Yontem(-2,1,1)
        Yontem(-2,3,2)





basla=Proje1()
basla.Main()