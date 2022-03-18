

# import math
# from pakiet import *
# napis='dzis jest piatek'
# modul.wyswietl(napis)
# print(modul.dlugosc(napis))

# plik=open('tekst.txt','r')
#
# znaki=plik.read(10)
# linia=plik.readline()
# wiersze=plik.readline()
#
# plik.close()
#
# print(znaki)
# print(linia)
# print(wiersze)
# print(len(wiersze))

# import sys
# print('Podaj kierunek studiów, rok i specjalizację')
# dane=sys.stdin.readline()
#
# plik=open('dane.txt','w+',encoding='utf-8')
# plik.write(dane)
# plik.close()
#
# lista=[]
# for x in range(0,7):
#     lista.append(x)
#
# plik=open('dane.txt','a+')
# plik.write(str(lista))
# plik.close()

# with open('tekst.txt','r') as plik:
#     for linia in plik:
#         print(linia, end='')

# class PierwszaKlasa:
#     """Pierwsza klasa python"""
#     atrybut=54321
#     def pierwsza_metoda(self):
#         return 'pierwsza metoda'
#
# obiekt=PierwszaKlasa()
# print(obiekt)
# print(obiekt.atrybut)
# obiekt.tekst='aaa'
# print(obiekt.tekst)
# print(obiekt.pierwsza_metoda())
# obiekt2=PierwszaKlasa()
# print(obiekt2.tekst)

class Ksztalty:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.opis= 'To będzie klasa dla ogólnych ksztaltow'

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2*self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis=text

    def skalowanie(self, czynnik):
        self.x=self.x*czynnik
        self.y=self.y*czynnik

prostokat = Ksztalty(10,30)
print(prostokat.pole())
print(prostokat.obwod())
print(prostokat.opis)
prostokat.dodaj_opis('Prostokąt')
print(prostokat.opis)
prostokat.skalowanie(0.5)
print(prostokat.x)
print(prostokat.y)