#!/usr/bin/env python3
import os
while True:
    def cls():
        if os.name =='nt':
            os.system("cls")
        else:
            os.system("clear")
    şifre=input("Kırmak istediğiniz şifreyi giriniz ")
    cls()
    value = 1
    şifrelim=""
    while value <= 93:
        şifrelim=""
        value = value +1
        for harf in şifre:
            if ord(harf) == 32:
                şifrelim = şifrelim+chr(ord(harf))
            else:
                if abs(ord(harf)-value) < 33:  
                    şifrelim = şifrelim + chr(127 - abs(33 - (ord(harf)-value)))
                    continue 
                şifrelim = şifrelim+chr(abs(ord(harf)-value))
        print("İşlem başarılı, çözülen metin"," ' ",şifrelim," ' ")
    input()
    cls()
    son_tercih=input("programı tekrar çalıştırmak için y'ye\n çıkış için ise herhangi bir tuşa basın ")
    if son_tercih == "y":
        cls()
    else:
        cls()
        exit()

    
