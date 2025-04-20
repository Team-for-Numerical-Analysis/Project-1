import tkinter as tk

class Proje2():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gauss Eliminasyonu")
        self.lb1 = tk.Listbox(self.root, width=50, height=25)
        self.lb1.grid(row=0, column=0, rowspan=10)

        self.value = tk.IntVar()
        self.value.set(0)
        self.formul = []

        option1 = tk.Radiobutton(self.root, text="MATRİS 4x4", variable=self.value, value=1)
        option1.grid(row=3, column=1)

        option2 = tk.Radiobutton(self.root, text="MATRİS 10x10", variable=self.value, value=2)
        option2.grid(row=4, column=1)

        buton1 = tk.Button(self.root, text="ONAYLA", width=15, command=self.GaussYokEtme)
        buton1.grid(row=6, column=1)

        tk.mainloop()

    def GaussYokEtme(self):
        self.lb1.delete(0, tk.END)

        def Formul():
            secim = self.value.get()
            if secim == 0:
                self.lb1.insert(tk.END, "Lütfen bir matris seçiniz...")
                return False
            elif secim == 1:
                self.formul = [
                    [1.0, 2.0, 3.0, 4.0],
                    [2.0, 3.0, 4.0, 5.0],
                    [5.0, 6.0, 7.0, 8.0],
                    [-7.0, 8.0, 9.0, 1.0]
                ]
            elif secim == 2:
                self.formul = [[float(i + j + 1) for j in range(10)] for i in range(10)]
            return True

        def SatirYerDegistirme():
            n = len(self.formul)
            for index in range(n):
                enbuyuk = index
                for i in range(index + 1, n):
                    if abs(self.formul[i][index]) > abs(self.formul[enbuyuk][index]):
                        enbuyuk = i
                if enbuyuk != index:
                    self.formul[index], self.formul[enbuyuk] = self.formul[enbuyuk], self.formul[index]

        if not Formul():
            return

        SatirYerDegistirme()
        self.lb1.insert(tk.END, "Yer değiştirme metodu uygulandı.")

        # Matris gösterimi
        for satir in self.formul:
            self.lb1.insert(tk.END, " ".join(f"{x:.2f}" for x in satir))

        self.lb1.insert(tk.END, "\nGauss Yok Etme Başladı:")

        # Gauss eliminasyonu (üst üçgen hâle getirme)
        n = len(self.formul)
        for i in range(n):
            for j in range(i + 1, n):
                if self.formul[i][i] == 0:
                    continue
                oran = self.formul[j][i] / self.formul[i][i]
                for k in range(i, n):
                    self.formul[j][k] -= oran * self.formul[i][k]

        self.lb1.insert(tk.END, "\nSonuç Matris:")
        for satir in self.formul:
            self.lb1.insert(tk.END, " ".join(f"{x:.2f}" for x in satir))
Proje2()