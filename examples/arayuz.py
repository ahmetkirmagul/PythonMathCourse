import tkinter as tk

sayac=0

def yaz():
    global sayac
    sayac+=1
    yazı.config(text=str(sayac))

pencere= tk.Tk()
pencere2= tk.Tk()

pencere2.title("Ahmet'in Penceresi")
pencere2.geometry("300x300")
pencere.configure(bg="white")

pencere.title("Güneş'in Penceresi")
pencere.geometry("250x250")
pencere.configure(bg="black")

giris = tk.Entry(pencere)
giris.pack()

deger = giris.get()
print(deger)

liste = tk.Listbox(pencere)
liste.pack()

liste.insert(0, "Elma")
liste.insert(1, "Armut")
liste.insert(2, "Muz")

yazı = tk.Label(pencere, text="0", fg="white", bg="black", font=("Arial", 30))
yazı.pack(pady=60,anchor="center")

Buton = tk.Button(pencere2, text="1 Arttır.", command=yaz, bg="black",fg="white",anchor="center",font=("Arial", 30))
Buton.pack(pady=100)

pencere.mainloop()
pencere2.mainloop()

tk.Button()