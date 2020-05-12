import time
import sys
from time import sleep


giris = "Yaşına Göre Hayatta Olduğun Saat, Dakika ve Saniyeyi Hesaplayacağım"
for char in giris:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\n")
time.sleep(0.6)


words = "Hazırsan Başlayalım!"
for char in words:
    sleep(0.06)
    sys.stdout.write(char)
    sys.stdout.flush()
print("\n")
time.sleep(0.6)


print("İsmin Nedir?")
isim = input()
print("\n")
time.sleep(1)

print("Yaşın Kaç " + isim + "?")
yas = int(input())
print("\n")
time.sleep(1)

print("Bir Saniye Bekleteceğim " + isim)
print("\n")
time.sleep(1)

dots = ".\t.\t.\t.\n.\t.\t.\t.\n.........................\n"
for char in dots:
    sleep(0.06)
    sys.stdout.write(char)
    sys.stdout.flush()

print("\n")

sonuc = "İşte Sonuç! \n"
for char in sonuc:
    sleep(0.08)
    sys.stdout.write(char)
    sys.stdout.flush()

print("\n")
time.sleep(1)


print("Yaklaşık")
print('[', yas * 8766, ']', 'Saat')
print("[", yas * 525949, "]", 'Dakika ')
print("[", yas * 31556952, "]", 'Saniye ', 'Yaşamışsın!')
print("\n")
time.sleep(1)
print("Helal Olsun " + isim + "!")
time.sleep(55)
