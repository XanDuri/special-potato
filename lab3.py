#zad1
# A=[]
# for x in range(1,10):
#     A.append(1-x)
# print(A)
# import math
# B=[]
# for x in range(0,7):
#     B.append(int(math.pow(4,x)))
# print(B)
# C=[]
# for x in B:
#     if x%2==0:
#         C.append(x)
# print(C)
#zad2
# import random
#
# lista1=[]
# for x in range(1,10):
#     lista1.append(random.randint(1,99))
# print(lista1)
# lista2=[]
# for x in lista1:
#     if x%2==0:
#         lista2.append(x)
# print(lista2)
#zad3
# from itertools import chain
#
# slownik={'Bulka':'sztuki','Marchewki':'kilogramy','Mleko':'mililitry','Baton':'sztuki','Lody na patyku':'sztuki','Kieubasa':'sztuki'}
# print(slownik)
# slownik2={}
# for key, value in slownik.items():
#     slownik2.setdefault(value, set()).add(key)
#
# wynik=set(chain.from_iterable(values for key, values in slownik2.items() if len(values)>1))
# print(wynik)
#zad4
# def czytrupro(a,b,c):
#     if(a**2+b**2==c**2):
#         print("Trójkąt prostokątny")
#     else:
#         print("Trójkąt nie prostokątny")
#
# a=input("Podaj a: ")
# a=int(a)
# b=input("Podaj b: ")
# b=int(b)
# c=input("Podaj c: ")
# c=int(c)
#
# czytrupro(a,b,c)
#zad5
# def poletrap(a=2,b=2,h=2):
#     print("Pole trapezu to: ",((a+b)*h)/2)
#
# poletrap()
# a=input("Podaj a: ")
# a=int(a)
# b=input("Podaj b: ")
# b=int(b)
# poletrap(a,b)
#zad6
# import math
# def iciag(a=1,b=4,ile=10):
#     ciag=[]
#     for x in range(0,ile):
#         ciag.append(a*math.pow(b,x))
#     print(ciag)
#     suma=1
#     for y in ciag:
#         suma=suma*y
#     print(suma)
#
# iciag()
#zad7
# import math
# def iciag(*a):
#     ciag=[]
#     for x in range(0,a[2]):
#         ciag.append(a[0]*a[1]**x)
#     print(ciag)
#     suma=1
#     for y in ciag:
#         suma=suma*y
#     print(suma)
#
# iciag(1,4,10)
#zad8

# def kasa(koszyk):
#     suma = 0
#     for key in koszyk:
#         print("Produkt: ",key, ", Cena: ", koszyk[key],"zł.")
#     for key in koszyk:
#         suma=suma+koszyk[key]
#     print("Suma zakupów: ",suma,"zł")
# koszyk = {'Jabłko': 2, 'Marchew': 1.5, 'Bułka': 1.8, 'Ser': 5, 'Mąka': 5.2, 'Jajka': 6}
# kasa(koszyk)
#
# def kasa(**koszyk):
#     suma=0
#     for key,value in koszyk.items():
#         print("Produkt: {} , Cena: {}".format(key,value),"zł")
#     for key,value in koszyk.items():
#         suma=suma+value
#     print("Suma zakupów: ",suma,"zł")
#
# kasa(Jablko= 2, Marchew= 1.5, Bulka= 1.8, Ser= 5, Maka= 5.2, Jajka= 6)
#zad9
from ciagi import *
print(ciagia.an(1,2,3))
print(ciagia.suma(4,5,6))
ciagia.czyary(1,2,3)
ciagia.czyary(1,4,3)
print(ciagia.anzSum(45,43))

print(ciagig.an(1,2,3))
print(ciagig.suma1(43,23))
print(ciagig.ank(12,2,3,1))
print(ciagig.suma0(2,4,5))
ciagig.czygeo(1,2,4)
ciagig.czygeo(1,5,4)
