import random
import time
import sys

kw = 0  # Kullanıcı kazanma sayısı
bw = 0  # Bilgisayar kazanma sayısı


def bss():
    r = random.randint(1, 3)
    if r == 1:
        return "Taş"
    elif r == 2:  # Random bir seçenek oluşturuyoruz.
        return "Kağıt"
    return "Makas"


def kontrol(ks):
    ks = ks.lower()

    if ks in ["taş", "tas", "t"]:
        return "Taş"
    elif ks in ["kağıt", "kagit", "k", "kâğıt", "kağit"]:
        return "Kağıt"  # Kullanıcıdan gelen cevabı istediğimiz cevaplar olup olmadığını kontrol ediyoruz.
    elif ks in ["makas", "m"]:
        return "Makas"
    else:
        return "hata"  # Eğer istenilen cevap verilmemişse "hata" değerini cevap olarak gönderiyoruz.


print("""
------------TAŞ KAĞIT MAKAS------------
     Kural Basit 3 Olan kazanır!

         İYİ EĞLENCELER!

""")
time.sleep(1)  # Yazıların okunması için süre tanıdık.

while True:
    print("=================================")
    ks = input("Seçiminizi Giriniz = ")
    print("=================================")
    ks = kontrol(ks)

    if ks == "hata":
        print("Geçersiz Seçenek")  # Gelen cevap "hata" ise "Geçersiz Seçenek" yazıp program sonlanıyor.
        sys.exit()

    bs = bss()
    print("Kullanıcı : ", ks)
    print("Bilgisayar : ", bs)
    print("---------------------------------")

    if ks == bs:
        print("Sonuç : Berabere!")
    elif (ks == "Taş" and bs == "Makas") or (ks == "Kağıt" and bs == "Taş") or (ks == "Makas" and bs == "Kağıt"): #Kazanan senaryoları yazdık
        print("Sonuç : Kazandınız!")
        kw += 1  # kw= Kullanıcı Win
    else:
        print("Sonuç : Kaybettiniz :(")
        bw += 1  # bw= Bilgisayar Win

    print("---------------------------------")
    print(f"Kullanıcı {kw} - Bilgisayar {bw}")   # Her tur kaç kaç olduğunu gösteriyoruz.
    print("---------------------------------")

    # Skor kontrolü: İlk 3 olan kazanır
    if kw == 3:
        print("""=============SKOR TABLOSU=============
               KAZANDINIZ!
                          """)
        print(f"Kullanıcı: {kw}, Bilgisayar: {bw}")
        sys.exit()

    if bw == 3:
        print("""=============SKOR TABLOSU=============
               KAYBETTİNİZ!
                          """)
        print(f"Kullanıcı: {kw}, Bilgisayar: {bw}")
        sys.exit()
