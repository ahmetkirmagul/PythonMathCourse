import random
import tkinter as tk

w,l=0,0

def kendine():
    global w,l
    doluMubosMu = random.randint(0,1)
    if doluMubosMu==1:
        etiket.config(text="Öldün!")
        l+=1
        scoreBoard.config(text=f"Kazanma:{w}\nKaybetme:{l}")
    else:
        etiket.config(text="Boşmuş...")
def pcye():
    global w,l
    doluMubosMu = random.randint(0,1)
    if doluMubosMu==1:
        etiket.config(text="Öldüm!")
        w+=1
        scoreBoard.config(text=f"Kazanma:{w}\nKaybetme:{l}")
    else:
        etiket.config(text="Ölmedim...")


#UI TKINTER
pencere = tk.Tk()
pencere.title("Rus ruleti")
pencere.geometry("400x400")
pencere.configure(bg="white")
etiket = tk.Label(pencere, text="Merhaba Ece!", fg="white", bg="black", font=("Arial", 16))
etiket.pack(pady=60,anchor="center")
kendineButon = tk.Button(pencere, text="Kendine Sık!", command=kendine, bg="black",fg="white")
kendineButon.pack(pady=10)
pcyeButon = tk.Button(pencere, text="Karşıya sık!", command=pcye, bg="black", fg="white")
pcyeButon.pack(pady=10)

scoreBoard = tk.Label(pencere, text=f"Kazanma:{w}\nKaybetme:{l}", fg="black", bg="white", font=("Arial", 12))
scoreBoard.pack(pady=60)

pencere.mainloop()


pencere=tk.Tk()