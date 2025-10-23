import random
import time
#VARIABLES
liste = ["taş","kağıt","makas"]
devam=True
berabereSayac,bilgisayarSayac,oyuncuSayac=0,0,0
sonuc=0 #0 berabere 1 user wins 2 computer wins
print("MERHABA! TAŞ KAĞIT MAKAS OYUNUNA HOŞ GELDİN!\n")
input("Başlamak için enterla!\n")

#ANA DÖNGÜ
while devam:

    #Data
    print("\033c", end="")
    print("Hazırsan başlayalım!\n")
    time.sleep(0.5)
    cChoice =random.choice(liste)
    print("Taş!")
    time.sleep(0.3)
    print("Kağıt!")
    time.sleep(0.3)
    print("Makas!")
    time.sleep(0.3)
    uChoice = input("[Seçimin(tas/kagit/makas veya t/k/m)]:").lower()
    print("\033c", end="")
    print(f"{cChoice} seçtim!")
    #BURADA KARŞILAŞTIR
    if uChoice[0] == cChoice[0]:
        sonuc=0
        berabereSayac+=1
        print("Berabere kaldık...hadi bir daha?")
    elif uChoice[0] =="t":
        if cChoice[0] == "k":
            sonuc=2
            bilgisayarSayac=bilgisayarSayac+1
        elif cChoice[0] == "m":
            sonuc=1
            oyuncuSayac=oyuncuSayac+1
    elif uChoice[0] =="k":
        if cChoice[0] == "t":
            sonuc=1
            oyuncuSayac=oyuncuSayac+1
        elif cChoice[0] == "m":
            sonuc=2
            bilgisayarSayac=bilgisayarSayac+1
    elif uChoice[0] == "m":
        if cChoice[0]=="t":
            sonuc=2
            bilgisayarSayac=bilgisayarSayac+1
        elif cChoice[0]=="k":
            sonuc=1
            oyuncuSayac=oyuncuSayac+1
    else:
        print("Yazım hatası mı yaptın :(")
    #Output
    if sonuc==1:
        print(f"Yendin!...")
    elif sonuc==2:
        print(f"Yenildin...üzülme :(")
    
    devamSecim= input("[Çıkmak için 'exit' yaz yoksa devam ediyorum!]:")
    if devamSecim=="exit":
        devam=False
    print("\033c", end="")

print("İyi oyundu!")
print(f"\nSen beni {oyuncuSayac} kere yendin!\nBen seni {bilgisayarSayac} kere yendim! \n{berabereSayac} kere de berabere kaldık!") 