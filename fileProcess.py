# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:27:13 2019

@author: lenovoz
"""
class demiryolu:
    tren_ismi = ""
    calistigi_hat = ""
    vagon_kapasitesi = 0
    yük_kapasitesi = 0
    tren_id = 0
    
class node:
        def __init__(self,data):
            self.data=data
            self.next=None 
class linkedList:
    def __init__(self):
        self.start=None
    def deleteFirst(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            self.start=self.start.next   
    def insert(self,value):
        newNood=node(value)
        if(self.start==None):
            self.start=newNood
        else:
            temp=self.start
            while(temp.next!=None):
                temp=temp.next
            temp.next=newNood
    def viewList(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            temp=self.start
            while(temp!=None):
                print(temp.data,end='')
                temp=temp.next
    def firstData(self):
        if(self.start==None):
            print("Liste Boş.")
        else:
            return self.start.data
    
myList=linkedList()
yönetici=[]
yönetici.append(170401013)
yönetici.append(170401010)
liste=[]
dosya = open("ödev.txt","a") #append modu
print("Merhaba.")
ilk_girdi=int(input("Kullanıcı iseniz 0,Yönetici iseniz ID'nizi,Çıkmak için -1 giriniz:"))
while ilk_girdi != -1:
    if(ilk_girdi == yönetici[0] or ilk_girdi==yönetici[1] or ilk_girdi ==0):
        break
    else:
        print('HATA! BÖYLE BİR YÖNETİCİ BULUNMUYOR.')
        ilk_girdi=int(input("Kullanıcı iseniz 0,Yönetici iseniz ID'nizi,Çıkmak için -1 giriniz:")) 

if(ilk_girdi==-1):
    dosya.close()
    exit
elif(ilk_girdi == 0):
    a_liste=[]
    print("1-Tren Ismi")
    print("2-Çalıştığı Hat")
    print("3-Vagon Kapasitesi")
    print("4-Yük Kapasitesi")
    print("5-Tren ID")
    print("6-Çıkış")
    ikinci_girdi = int(input("Lütfen Aramak Istediginiz Kriteri Seçiniz:"))
    if(ikinci_girdi == 6):
            exit#program sonlanacak
    while(ikinci_girdi>6 or ikinci_girdi<1):
        print("HATA!!!")
        ikinci_girdi = int(input("Lütfen Aramak Istediginiz Kriteri Seçiniz:"))
    if(ikinci_girdi==1):
        with open("ödev.txt","r+") as file3:
            file3.read()
            while True:
                ekle12=str(input("TREN İSMİ:"))
                if(len(ekle12)<15):
                    for j in range(0,(15-len(ekle12))):
                        ekle12+=' '
                    break
                else:
                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-15 ARASINDA KARAKTER GİRİN")
            print(" ID     TREN İSMİ         CALISTIGI HAT      V.KAP      Y.KAP")
            for k in range(0,1000):
                file3.seek((66*k)+6)
                tutucu4=file3.readline(15)
                if(tutucu4==''):
                    break
                if(tutucu4==ekle12):
                    file3.seek(66*k)
                    kelime=file3.readline(66)
                    a_liste.append(kelime)
                    print(kelime)
            if(a_liste==[]):
                print("BU KAYITTA BİR VERİ BULUNAMADI.")
                a_liste.clear()
            file3.close()
    elif(ikinci_girdi==2):
        with open("ödev.txt","r+") as file3:
            file3.read()
            while True:
                ekle12=str(input("ÇALIŞTIĞI HAT:"))
                if(len(ekle12)<20):
                    for j in range(0,(20-len(ekle12))):
                        ekle12+=' '
                    break
                else:
                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-20 ARASINDA KARAKTER GİRİN")
            print(" ID     TREN İSMİ         CALISTIGI HAT      V.KAP      Y.KAP")
            for k in range(0,1000):
                file3.seek((66*k)+22)
                tutucu4=file3.readline(20)
                if(tutucu4==''):
                    break
                if(tutucu4==ekle12):
                    file3.seek(66*k)
                    kelime=file3.readline()
                    a_liste.append(kelime)
                    print(kelime)
            if(a_liste==[]):
                print("BU KAYITTA BİR VERİ BULUNAMADI.")
                a_liste.clear()
            file3.close()
    elif(ikinci_girdi==3):
        with open("ödev.txt","r+") as file3:
            file3.read()
            while True:
                ekle12=str(input("VAGON KAPASİTESİ:"))
                if(len(ekle12)<10):
                    for j in range(0,(10-len(ekle12))):
                        ekle12='0'+ekle12
                    break
                else:
                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA KARAKTER GİRİN")
            print(" ID     TREN İSMİ         CALISTIGI HAT      V.KAP      Y.KAP")
            for k in range(0,1000):
                file3.seek((66*k)+43)
                tutucu4=file3.readline(10)
                if(tutucu4==''):
                    break
                if(tutucu4==ekle12):
                    file3.seek(66*k)
                    kelime=file3.readline()
                    a_liste.append(kelime)
                    print(kelime)
            if(a_liste==[]):
                print("BU KAYITTA BİR VERİ BULUNAMADI.")
                a_liste.clear()
            file3.close()
    elif(ikinci_girdi==4):
        with open("ödev.txt","r+") as file3:
            file3.read()
            while True:
                ekle12=str(input("YÜK KAPASİTESİ:"))
                if(len(ekle12)<10):
                    for j in range(0,(10-len(ekle12))):
                        ekle12='0'+ekle12
                    break
                else:
                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA KARAKTER GİRİN")
            print(" ID     TREN İSMİ         CALISTIGI HAT      V.KAP      Y.KAP")
            for k in range(0,1000):
                file3.seek((66*k)+54)
                tutucu4=file3.readline(10)
                if(tutucu4==''):
                    break
                if(tutucu4==ekle12):
                    file3.seek(66*k)
                    kelime=file3.readline()
                    a_liste.append(kelime)
                    print(kelime)
            if(a_liste==[]):
                print("BU KAYITTA BİR VERİ BULUNAMADI.")
                a_liste.clear()
            file3.close()
    elif(ikinci_girdi==5):
        with open("ödev.txt","r+") as file3:
            file3.read()
            while True:
                ekle12=str(input("TREN ID:"))
                if(len(ekle12)<5):
                    for j in range(0,(5-len(ekle12))):
                        ekle12='0'+ekle12
                    break
                else:
                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA KARAKTER GİRİN")
            print(" ID     TREN İSMİ         CALISTIGI HAT      V.KAP      Y.KAP")
            for k in range(0,1000):
                file3.seek(66*k)
                tutucu4=file3.readline(5)
                if(tutucu4==''):
                    break
                if(tutucu4==ekle12):
                    file3.seek(66*k)
                    kelime=file3.readline()
                    a_liste.append(kelime)
                    print(kelime)
            if(a_liste==[]):
                print("BU KAYITTA BİR VERİ BULUNAMADI.")
                a_liste.clear()
            file3.close()
    dosya.close()
else:
    ucuncu_girdi = 0
    while(ucuncu_girdi !=4):
        print("Yönetici Arayüzüne Hoşgeldiniz :)")
        print("1-Ekleme")
        print("2-Güncelleme")
        print("3-Silme")
        print("4-Çıkış")
        ucuncu_girdi = int(input("Lütfen Yapmak Istediğiniz Islemi Seçiniz:"))
        
        while(ucuncu_girdi>4 or ucuncu_girdi<1):
            print("HATA!!!")
            ucuncu_girdi = int(input("Lütfen Yapmak Istediğiniz Islemi Seçiniz:"))
            
        if ucuncu_girdi == 1:
 #           dosya = open("ödev.txt","a") #append modu
            dorduncu_girdi = 0
            liste2=[]
            while(dorduncu_girdi !=2):
                while True:
                    ekle1 = str(input("Tren Ismi:"))
                    if(len(ekle1)<15):
                        for j in range(0,(15-len(ekle1))):
                            ekle1+=' '
                        break
                    else:
                        print("ÇOK UZUN GİRDİ! LÜTFEN 1-15 ARASINDA KARAKTER GİRİN")
                    
                while True:
                    ekle2 = str(input("Çalıştığı Hat:"))
                    if(len(ekle2)<20):
                        for j in range(0,(20-len(ekle2))):
                            ekle2+=' '
                        break
                    else:
                        print("ÇOK UZUN GİRDİ! LÜTFEN 1-20 ARASINDA KARAKTER GİRİN")
                while True:
                    ekle3 = str(input("Vagon Kapasitesi:"))
                    if(len(ekle3)<10):
                        for j in range(0,(10-len(ekle3))):
                            ekle3='0'+ekle3
                        break
                    else:
                        print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA SAYI GİRİN")
                while True:
                    ekle4 = str(input("Yük Kapasitesi:"))
                    if(len(ekle4)<10):
                        for j in range(0,(10-len(ekle4))):
                            ekle4='0'+ekle4
                        break
                    else:
                        print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA SAYI GİRİN")
                while True:
                    ekle5 = str(input("Tren ID:"))
                    if(len(ekle5)<5):
                        for j in range(0,(5-len(ekle5))):
                            ekle5='0'+ekle5
                        break
                    else:
                        print("ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA SAYI GİRİN")
                nesne = demiryolu()
                nesne.tren_ismi = ekle1
                nesne.calistigi_hat = ekle2
                nesne.vagon_kapasitesi = ekle3
                nesne.yük_kapasitesi = ekle4
                nesne.tren_id= ekle5
                liste.append(nesne)
                dorduncu_girdi = int(input('1-EKLEME\n2-ÇIKIŞ\n'))
               # if(dorduncu_girdi <1 or dorduncu_girdi>2):
                #    print('HATA!!! YANLIŞ GİRDİ.')
                while(dorduncu_girdi <1 or dorduncu_girdi>2):
                    print('HATA!!! YANLIŞ GİRDİ.')
                    dorduncu_girdi = int(input('1-EKLEME\n2-ÇIKIŞ\n'))
                if(dorduncu_girdi == 2):
                    break
            for i in liste:
                if(myList.start==None):
                    for j in range(0,1000):
    #                        file = open("ödev.txt","r")
                        with open("ödev.txt","r") as file:
                            file.read()
                            file.seek(66*j)
                            tutucu = file.readline(5)
                            if(tutucu == ''):
                                break
                            if(tutucu == i.tren_id):
                                break  
                    if(tutucu == i.tren_id):
                        print(i.tren_id,"ID'li Kayıt Zaten Bulunmaktadır.")
                    else:
                        dosya.write(i.tren_id)
                        dosya.write(':')
                        dosya.write(i.tren_ismi)
                        dosya.write(':')
                        dosya.write(i.calistigi_hat)
                        dosya.write(':')
                        dosya.write(i.vagon_kapasitesi)
                        dosya.write(':')
                        dosya.write(i.yük_kapasitesi)
                        dosya.write("\n")
                        print("EKLEME BAŞARILI.")
                else:#olmazsa buradan silicam
                        for j in range(0,1000):
        #                        file = open("ödev.txt","r")
                            with open("ödev.txt","r") as file:
                                file.read()
                                file.seek(66*j)
                                tutucu = file.readline(5)
                                if(tutucu == ''):
                                    break
                                if(tutucu == i.tren_id):
                                    break  
                        if(tutucu == i.tren_id):
                            print(i.tren_id,"ID'li Kayıt Zaten Bulunmaktadır.")
                        else:
                            myList.viewList()
                            first=myList.firstData()
                            with open("ödev.txt","r+")as file4:
                                file4.read()
                                file4.seek(first)
                                file4.write(i.tren_id+':'+i.tren_ismi+':'+i.calistigi_hat+':'+i.vagon_kapasitesi+':'+i.yük_kapasitesi+'\n')
                                print("EKLEME BAŞARILI.")
                            file4.close()
                            myList.deleteFirst()
            file.close()
            dosya.close()
            
        if ucuncu_girdi == 2:
            besinci_girdi = 0
            while(besinci_girdi != -1):
                besinci_girdi=int(input("-1 ÇIKIŞ\nGÜNCELLENECEK ID:"))
                if(besinci_girdi<-1):
                    print("HATA! ID 0'DAN KÜÇÜK OLAMAZ")
                elif(besinci_girdi>9999):
                    print("HATA! ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA SAYI GİRİN")
                else:
                    with open("ödev.txt","r+") as file1:
                        file1.read()
                        file1.seek(0)
                        if(file1.readline() == ''):
                            print("HATA! DOSYA BOŞ.LÜTFEN ÖNCE EKLEME YAPINIZ")
                            break
                        else:
                            while(besinci_girdi !=-1):
                                ekle10=str(besinci_girdi)
                                if(len(ekle10)<5):
                                    for j in range(0,(5-len(ekle10))):
                                        ekle10='0'+ekle10
                                else:
                                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA SAYI GİRİN")
                                for k in range(0,1000):
                                    file1.seek(66*k)
                                    tutucu2=file1.readline(5)
                                    if(tutucu2==''):
                                        break
                                    if(ekle10 == tutucu2):
                                        while True:
                                            ekle6 = str(input("Tren Ismi:"))
                                            if(len(ekle6)<15):
                                                for j in range(0,(15-len(ekle6))):
                                                    ekle6+=' '
                                                break
                                            else:
                                                print("ÇOK UZUN GİRDİ! LÜTFEN 1-15 ARASINDA KARAKTER GİRİN")
                                            
                                        while True:
                                            ekle7 = str(input("Çalıştığı Hat:"))
                                            if(len(ekle7)<20):
                                                for j in range(0,(20-len(ekle7))):
                                                    ekle7+=' '
                                                break
                                            else:
                                                print("ÇOK UZUN GİRDİ! LÜTFEN 1-20 ARASINDA KARAKTER GİRİN")
                                        while True:
                                            ekle8 = str(input("Vagon Kapasitesi:"))
                                            if(len(ekle8)<10):
                                                for j in range(0,(10-len(ekle8))):
                                                    ekle8='0'+ekle8
                                                break
                                            else:
                                                print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA SAYI GİRİN")
                                        while True:
                                            ekle9 = str(input("Yük Kapasitesi:"))
                                            if(len(ekle9)<10):
                                                for j in range(0,(10-len(ekle9))):
                                                    ekle9='0'+ekle9
                                                break
                                            else:
                                                print("ÇOK UZUN GİRDİ! LÜTFEN 1-10 ARASINDA SAYI GİRİN")
                                        file1.seek(66*k)
                                        file1.write(ekle10+':'+ekle6+':'+ekle7+':'+ekle8+':'+ekle9+'\n')
                                        print("Güncelleme Başarılı.")
                                        file1.flush()
                                        file1.close()
                                        break
                                if(ekle10 != tutucu2):
                                    print("BÖYLE BİR KAYIT BULUNAMADI.LÜTFEN ÖNCE EKLEME YAPINIZ.")
                                    break
                                break
                
        if ucuncu_girdi == 3:
            altıncı_girdi=0
            tutucu3=0
            while(altıncı_girdi!=-1):
                altıncı_girdi=int(input("-1 ÇIKIŞ\nSİLMEK İSTEDİĞİNİZ ID'Yİ GİRİNİZ:"))
                if(altıncı_girdi<-1):
                    print("HATA! YANLIŞ KARAKTER. ID 0'DAN KÜÇÜK OLAMAZ.")
                elif(altıncı_girdi>9999):
                    print("HATA! ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA SAYI GİRİN")
                else:
                    with open("ödev.txt","r+") as file2:
                        file2.read()
                        file2.seek(0)
                        if(file2.readline() == ''):
                            print("HATA! DOSYA BOŞ.LÜTFEN ÖNCE EKLEME YAPINIZ")
                            break
                        else:
                            ekle11=str(altıncı_girdi)
                            if(len(ekle11)<5):
                                for j in range(0,(5-len(ekle11))):
                                    ekle11='0'+ekle11
                            else:
                                    print("ÇOK UZUN GİRDİ! LÜTFEN 1-5 ARASINDA SAYI GİRİN")
                            for q in range(0,1000):
                                tutucu3=file2.seek(66*q)
                                tutucu1=file2.readline(5)
                                if(tutucu1==''):
                                    print("HATA! BÖYLE BİR KAYIT BULUNAMADI.")
                                    break
                                if(tutucu1 == ekle11):
                                    myList.insert(int(tutucu3))
                                    file2.seek(66*q)
                                    file2.write("*****:***************:********************:**********:**********")
                                    print("SİLME İŞLEMİ BAŞARILI.")
                                    break
            file2.close()
    dosya.close()
