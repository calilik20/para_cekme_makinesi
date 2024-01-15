print("""**********************

ATM MAKİNESİNE HOŞGELDİNİZ

İşlemler

1. Bakiye Sorgulama
2. Para yatırma
3. Para çekme

Programdan çıkmak için q ya basınız.

**********************



""")


bakiye = 1000

while True:
   islem = input("işlem seçiniz:")

   if islem=="q":
       print("yine bekleriz.")
       break

   elif islem=="1":
       print("Bakiyeniz {} tldir.".format(bakiye))
   elif islem=="2":
       miktar=int(input("miktarı giriniz:"))
       bakiye += miktar
   elif islem =="3":
        miktar=int(input("Miktarı giriniz:"))
        if (bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsin.")
            continue
        bakiye-=miktar
else:
    print("geçersiz işlem...")