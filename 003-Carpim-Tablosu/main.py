import time
import random
import sys

skor = 0
can = 3     #skor ve can değerlerimiz

def zorluktext(zorluk):
    if zorluk == 1:
        return "Çok Kolay"
    elif zorluk == 2:
        return "Kolay"
    elif zorluk == 3:   #Ekranda zorluğu yazdırmak için
        return "Orta"
    elif zorluk == 4:
        return "Zor"
    else:
        return "İmkansız"


def soru(zorluk):
    if zorluk == 1:
        sayi1 = random.randint(2, 4)
        sayi2 = random.randint(2, 4)
    elif zorluk == 2:
        sayi1 = random.randint(2, 5)
        sayi2 = random.randint(2, 5)
    elif zorluk == 3:
        sayi1 = random.randint(3, 7)
        sayi2 = random.randint(3, 7)
    elif zorluk == 4:                                  #Zorluğa göre sayı üretme
        sayi1 = random.randint(4, 9)
        sayi2 = random.randint(4, 9)
    elif zorluk == 5:
        sayi1 = random.randint(7, 25)
        sayi2 = random.randint(7, 25)

    return sayi1, sayi2


def zorluk_secin():
    print("""
----------ÇARPIM TABLOSU----------
    -Lütfen Zorluk Seçiniz.

    1-Çok Kolay
    2-Kolay
    3-Orta                                
    4-Zor
    5-İmkansız
    0-Çıkış

    """)#Zorluk seçme

    try:
        zorluk = int(input("Cevabınız = "))
        if zorluk == 0:
            print("Çıkış Yapılıyor...")
            time.sleep(0.5)     #Çıkış işlemi
            print(f"Rekorunuz {skor}!")
            sys.exit()
        if zorluk < 0 or zorluk > 5:
            print("Lütfen Geçerli Bir Seçenek Seçiniz")
            return zorluk_secin()  # Geçersiz girişte tekrar zorluk sorar
        else:
            zorluk1 = zorluktext(zorluk)
            print(f"Seçilen zorluk seviyesi: {zorluk1}")
            time.sleep(1)
            print("Sorular Yükleniyor...")
            return zorluk
    except ValueError:
        print("Lütfen bir sayı giriniz!")
        sys.exit()

def kurallar():
    print("""----------ÇARPIM TABLOSU----------
             Kurallar              
3 Yanlış Cevap Hakkınız Vardır."""
)#kurallar

kurallar()
time.sleep(3)
zorluk = zorluk_secin()#Kuralları ekrana yazdırdık ve daha sonra zorluk seçtirdik.

while True:
    time.sleep(0.5)
    if can==0:
        if skor>=2 or skor<=4:
            print("Tüm Hakların Bitti (Matematik dersi almalısın!)")
            print(f"Rekorunuz {skor}!")
            sys.exit()
        if skor>=5 or skor<=8:
            print("Hakların Bitti Ama Çok İyiydin!")#Skora göre bitiş yazıları.
            print(f"Rekorunuz {skor}!")
            sys.exit()
        if skor>=9:
            print("Konuşmaya Gerek Yok Profesör müsün?")
            print(f"Rekorunuz {skor}!")
            sys.exit()



    sayi1, sayi2 = soru(zorluk)#Zorluğa göre rastgele gelen sayıları aldık.
    dcevap = sayi1 * sayi2  #dcevap= Doğru cevap

    print(f"Sorunuz: {sayi1} x {sayi2} = ?")


    try:
        kcevap = int(input("""
        0-Çıkış
        1-Zorluk Değiştir
        Cevabınız = """))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue


    if kcevap == 0:
        print("Çıkış Yapılıyor...")
        time.sleep(0.5)     #Soru içerisinde çıkış yapma.
        print(f"Rekorunuz {skor}!")
        sys.exit()


    if kcevap == 1:
        zorluk = zorluk_secin() #Soru içerisinde zorluk değiştirme.
        continue

    if kcevap == dcevap:
        skor += 1
        print("----------------------------------")
        print("Tebrikler Doğru Cevap!")#Cevap doğruysa
        print(f"Skorunuz: {skor}")
        print(f"Canınız: {can}")
        print("----------------------------------")
        time.sleep(0.5)
    else:
        can -=1
        print("----------------------------------")
        print("Biraz Daha Çalışmalısın :(")#Cevap yanlışsa
        print(f"Skorunuz: {skor}")
        print(f"Canınız: {can}")
        print("----------------------------------")
        time.sleep(0.5)
# Github: @0umutekinci
