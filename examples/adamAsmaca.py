#MERHABA
import random

#Kelimeleri belirle(kullanıcı değil, sen yani güneş)
kelimeler = ["güneş","ahmet","selin","ec","samet","ahmet"]
tahmin = []

#Random kelime seç
secim = random.choice(kelimeler)

#Arayüz
print("MERHABA! ADAM ASMACA OYUNUNA HOŞ GELDİNİZ")
input("Başlamak için entera basın!")

print("_ "*len(secim))
for i in secim:
    tahmin.insert(0,"_")

oyunDevamMi=True
while oyunDevamMi:
    #Girdi(Input)
    girilenHarf = input("Bir harf gir:")

    #Kontrol et

    harfVar=False
    for k in secim:
        if girilenHarf == k:
            tahmin[secim.index(k)]=k
            harfVar=True
    if harfVar==False:
        print("Bu harf yok.")

    tahminString = "".join(tahmin)
    print(tahminString)
    #Mesela bak söylemiyorum sesli rencide etmemek için sen bulmuş gibi ol tamam mı
    #ben olsam önce değişkenleri yazdırırdım çünkü bunları karşılaştırıyoruz ya eşit mi diye? şimdi bak secim diye bir şey var bu kelimenin kendisi mesela g
    if tahmin == secim:
        oyunDevamMi=False

print("Bitti.")


#eğer her harf doğruysa bitsin
#adam öldüyse bitsin