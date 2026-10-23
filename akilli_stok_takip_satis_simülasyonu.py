import random 

urunler= [
    "Telefon",
    "Laptop",
    "Kulaklık",
    "Tablet",
    "Mouse"
]

fiyatlar=[25000,45000,3000,15000,1000]

# rastgele stok 

stoklar=[]

for urun in urunler:
    stok=random.randint(5,50)
    stoklar.append(stok)

satislar=[0,0,0,0,0]

calisiyor= True


while calisiyor:
    print("1-Ürünleri göster.")
    print("2-Günlük satış yap.")
    print("3-Kritik stokları göster.")
    print("4-Rapor")
    print("5-Çıkış")

    tercih=input("Tercihiniz: ")

if tercih == "1":
    print("\n Ürün Listesi ")

    for i in range(len(urunler)):
        print(i+1,urunler[i],"|fiyat:",fiyatlar[i],"TL","|stok:",stoklar[i])

#günlük satış

elif tercih == "2":
    print("\n Günlük Satış ")

    for i in range(len(urunler)):

        satis= random.randint(0,15)
        if satis > stoklar [i]:
             print(urunler[i],"Yeterli stok yok.")
             continue

        stoklar[i]= stoklar[i]- satis
        satislar[i]= satislar[i]- satis

        print(urunler[i], satis,"adet satıldı")
        print("Satış tamamlandı.")

elif tercih =="3":
    print(" Kritik Stok ")

    kritik_urunler=[urunler[i] for i in range(len(urunler)) if stoklar[i] < 10]

    if len(kritik_urunler)== 0 :
        print("Kritik stok bulunmuyor.")

    else:
        for urun in kritik_urunler:
            print(urun,"stok seviyesi düşük")

elif tercih== "4":
    print(" Satış Raporu")

    toplam_kazanc= 0

    for i in range(len(urunler)):
        kazanc= satislar[i] * fiyatlar[i]
        toplam_kazanc= toplam_kazanc+ kazanc

        print(urunler[i],"|satış:",satislar[i],"|kazanç:",kazanc,"TL")

    print("Toplm Kazanç:",toplam_kazanc,"TL")
    print(" İlk 3 ürün:")
    print(urunler[:3])
    print(" Son 2 ürün:")
    print(urunler[-2:])

elif tercih == "5":
    print("Program sonlandırılıyor...")
    calisiyor= False

else:
    print("Geçersiz tercih yaptınız!")