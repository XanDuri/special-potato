# piątek 15:45-18:00
# 30.03-1 kolokwium
#
# lista=[]
# for element in sekwencja:
#     if warunek_na_segmencie:
#         lista.append(akcja_z_elementem)
#
#
# lista=[akcja_z_elementem for element in sekwencja if warunek_na_element]
#
# a={x^2:xe<0,9>}
# b={1,3,8,27,...}
#
# a=[]
# for x in range(0,10):
#     a.append(x**2)
# print(a)
#
# a2=[x**2 for x in range(0,10)]
# print(a2)
#
# b=[]
# for x in range(0,6):
#     b.append(3**x)
# print(b)
#
# b2=[3**x for x in range(0,6)]
# print(b2)
#
# c=[]
# for x in range (0,10):
#     if(a[x]%2==1):
#         c.append(a[x])
# print(c)
#
# c2=[a[x] for x in range (0,10) if (a[x]%2==1)]
# print(c2)
#
# c3=[]
# for x in a:
#     if(x%2==0):
#         c3.append(x)
# print(c3)
#
# c4=[x for x in a if (x%2==0)]
# print(c4)
#
# lista=[]
# for a in [1,2,3]:
#     for b in [1,2,3]:
#         lista.append((a,b))
# print(lista)
#
# lista2=[(a,b) for a in [1,2,3] for b in [1,2,3]]
# print(lista2)
#
# slownik={'PZU':'Państwowy zakład ubezbieczeń',
#          'ZUS':'Zakład ubezpieczeń społecznych',
#          'PKO':'Państwowa kasa oszczędnościowa'}
# print(slownik)
#
# slownik_odwrocony={}
# for key, value in slownik.items():
#     slownik_odwrocony[value]=key
# print(slownik_odwrocony)
#
# slownik2={value: key for key, value in slownik.items()}
# print(slownik2)
#
# def nazwa_funkcji(arg pozycyjne, arg domyslny=wartosc, *arg, **arg):
#   instrukcje
#   return
# import math
# def row_kwadratowe(a,b,c):
#     delta=b**2-4*a*c
#     if delta<0:
#         print('Brak rozwiazan')
#         return -1
#     elif delta==0:
#         print('Jedno rozwiazanie')
#         x=(-b)/(2*a)
#         return x
#     else:
#         print('dwa rozwiazania')
#         x1=((-b)-math.sqrt(delta))/(2*a)
#         x2=((-b)+math.sqrt(delta))/(2*a)
#         return x1,x2
#
#
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2,1))
# print(row_kwadratowe(1,4,1))
#
# def czy_pa(a):
#     if(a%2==0):
#         return 'Parzysta'
#     else:
#         return 'Nie parzysta'
#
# print(czy_pa(2))
# print(czy_pa(3))
#
# import math
# def dlu_odc(x1=1,y1=2,x2=3,y2=4):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)
# #argumenty domyslne
# print(dlu_odc())
# #argumenty pozycyjne
# print(dlu_odc(4,5,6,9))
# #dwa argumenty pozycjyne, dwa okreslone
# print(dlu_odc(2,2,y2=7,x2=5))
# #argumenty po za kolejnoscia
# print(dlu_odc(x2=6,y2=4,x1=2,y1=3))
# #dwa argumenty domyslne, dwa z nowaz wartoscia
# print(dlu_odc(x2=4,y2=7))
#
# def ciag(* liczby):
#     if len(liczby)==0:
#         return 0
#     else:
#         suma=0
#         for i in liczby:
#             suma+=i
#         return suma
#
#
# print(ciag())
# print(ciag(1,2,3,4,5,6,7,8))
#
# def co_lubie(** rzeczy):
#     for cos in rzeczy:
#         print('to sa')
#         print(cos)
#         print('ktore lubie')
#         print(rzeczy[cos])
# co_lubie(gry=['planszowe','komputerowe'], slodycze='czekolada')