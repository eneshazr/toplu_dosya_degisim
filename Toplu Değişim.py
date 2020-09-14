#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
import fnmatch
import random
import time
import colorama
from colorama import Fore, Back, Style, init
colorama.init(autoreset=True)

def addegis():

    try:
        print(Fore.CYAN+f"\n Dosya yolunu  C:/Desktop/file/  olarak giriniz.")
        ypath = input(f" Dosya Yolu: ")

        if not os.path.isdir(ypath):
            print(Fore.RED+f"\n {ypath} dosya yolu bulunamadı!")
            return addegis()
        print(Fore.CYAN+f"\n Değişmesini istediğiniz dosyanın uzantısını giriniz. (Örn. png)")
        degisilecek = input(f" Değişilecek uzantı: ")
        print(Fore.CYAN+f"\n Yeni uzantıyı yazınız. (Örn. jpg)\n")
        yeni = input(f" Yeni uzantı: ")

        s = 0
        for file in os.listdir(ypath):
            if fnmatch.fnmatch(file,'*.'+degisilecek):
                s += 1
                print(s,' - ', file)

        if s == 0:
            print(Fore.RED+f"\n {degisilecek} uzantılı dosya bulunamadı!")
            return addegis()
        print(Fore.YELLOW+f"\n  {degisilecek} uzantılı {s} dosya bulundu.\n")
        onay = input(Fore.RED+f"  Yukarıdaki {s} dosyanın uzantısı belirttiğiniz şekilde değişecektir. Bu işlemi Onaylıyormusunuz? evet/hayır\n: ")

        if onay == "EVET" or onay == "evet":
            for dosyaAdi in os.listdir(ypath):
                gdosya = os.path.join(ypath,dosyaAdi)
                if not os.path.isfile(gdosya): continue
                os.path.splitext(dosyaAdi)
                yeniAd = gdosya.replace('.'+degisilecek, '.'+yeni)
                os.rename(gdosya,yeniAd)
            print(Fore.GREEN+f" {s} Dosya Başarıyla Degiştirildi")

            ex = input(f"Çıkılsın mı? e/h  ")
            if ex == "EVET" or ex == "evet" or ex == "e":
                for i in range(1,4):
                    time.sleep(1)
                    print("Konsol Kapatılıyor... ",i)
                sys.exit()

            elif ex == "HAYIR" or ex ==  "hayır" or ex == "hayir" or ex == "HAYİR" or ex == "h":
                return addegis()

        elif onay == "HAYIR" or onay ==  "hayır" or onay == "hayir" or onay == "HAYİR":
            print("\n İşlem iptal edildi.")
            for i in range(1,4):
                time.sleep(1)
                print("Konsol Kapatılıyor... ",i)
            sys.exit()
    except:
        print(Fore.RED+f"")
addegis()