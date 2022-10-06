'''
#zad1
def imie(imie,nazwisko):
    print(imie+"."+nazwisko)
imie('Ł','Moszczyński')
#zad2
def inicjal(imie,nazwisko):
    imiew=[i.capitalize() for i in imie][0]
    nazwiskow=[i.capitalize() for i in nazwisko]
    print(imiew[0]+'.'+nazwiskow[0])
imie=['łukasz']
nazwisko=['moszczyński']
inicjal(imie,nazwisko)
#zad3
def rok_urodzenia(rokp,roko,wiek):
    rok=rokp+roko
    rok=int(rok)
    print(rok-wiek)
rok_urodzenia('20','22',21)
#zad4
def funkcja(imie,nazwisko,inicjal):
    inicjal(imie,nazwisko)
imie=['łukasz']
nazwisko=['moszczyński']
funkcja(imie,nazwisko,inicjal)
#zad5
def dziel(a,b):
    if(a>0 and b>0 and b!=0):
        suma=a/b
        print(suma)
dziel(2,4)
#zad6
suma=0
while suma!=100:
    liczba=input("Podaj iczba: ")
    liczba=int(liczba)
    suma += liczba
print(suma)
#zad7
def krotka(lista):
    return (*lista, )
lista=['kot',45,'pies',56]
print(krotka(lista))
#zad8
lista = []
ile = input("Podaj ilosc elementów: ")
ile = int(ile)
for i in range(0,ile):
    print("Podaj liczbe na idexie", i, )
    wartosc = input()
    lista.append(wartosc)
print(tuple(lista))
'''
