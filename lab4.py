#zad1
# plik=open("zad1.txt",'w+')
# lista=[]
# for x in range (0,31):
#     lista.append(x*2)
# plik.write(str(lista))
# plik.close()
#zad2
# plik=open('zad1.txt','r')
# linia=plik.readline()
# plik.close()
# print(linia)
#zad3
# with open('zad3.txt','r') as plik:
#      for linia in plik:
#          print(linia, end='')
#zad4
# class NaZakupy:
#      """NaZakupy"""
#
#      def __init__(self, nazwa_produktu, ilosc, jednostak_miary, cena_jed):
#          self.nazwa_produktu = nazwa_produktu
#          self.ilosc = ilosc
#          self.jednostak_miary = jednostak_miary
#          self.cena_jed = cena_jed
#
#      def wyswietl_produkt(self):
#          return self.nazwa_produktu
#          return self.ilosc
#          return self.jednostak_miary
#          return self.cena_jed
#
#      def ile_produkt(self):
#          return str(self.ilosc) + str(self.jednostak_miary)
#
#      def ile_kosztuje(self):
#           return self.ilosc * self.cena_jed
#
# produkt = NaZakupy('Chleb',5,'kg',1.20)
# print(produkt.wyswietl_produkt())
# print(produkt.ile_produkt())
# print(produkt.ile_kosztuje())
#zad5
# class ciagAry:
#     """Ciag arytmetyczny"""
#     def __init__(self, pocz,kon,co):
#         self.pocz=pocz
#         self.kon=kon
#         self.co=co
#
#     def wyswietl_dane(self):
#         ciag = []
#         for x in range (self.pocz,self.kon):
#             ciag.append(x+self.co)
#         return ciag
#
#     def pobierz_parametry(self):
#         self.pocz=input("Podaj poczatek: ")
#         self.pocz=int(self.pocz)
#         self.kon=input("Podaj ilosc: ")
#         self.kon = int(self.kon)
#         self.co=input("Podaj r: ")
#         self.co = int(self.co)
#
#         ciag = []
#         for x in range(0,self.kon):
#             ciag.append(self.pocz + self.co*x)
#         return ciag
#
#     def pobierz_elementy(self):
#         ciag=[]
#         self.pocz=input("Podaj ilosc w ciagu: ")
#         self.pocz=int(self.pocz)
#         for x in range (0,self.pocz):
#             self.kon=input("Podaj wartosc: ")
#             ciag.append(self.kon)
#         return ciag
#
#     def policz_sume(self):
#         ciag = []
#         suma=0
#         for x in range (self.pocz,self.kon):
#             ciag.append(x + self.co)
#             suma+=x+self.co
#         return suma
#
#     def policz_elementy(self):
#         ciag = []
#         suma = 0
#         for x in range(self.pocz, self.kon):
#             ciag.append(x + self.co)
#             suma+=1
#         return suma
#
# ciag=ciagAry(1,10,2)
# print(ciag.wyswietl_dane())
# print(ciag.pobierz_elementy())
# print(ciag.pobierz_parametry())
# print(ciag.policz_sume())
# print(ciag.policz_elementy())
#zad6
# class Robaczek():
#        """Robaczek"""
#     def __init__(self,x,y,krok):
#         self.x=x
#         self.y=y
#         self.krok=krok
#
#     def idz_w_gore(self,kroki):
#         self.y=self.y+kroki*self.krok
#
#     def idz_w_prawko(self,kroki):
#         self.x=self.x+kroki*self.krok
#
#     def idz_w_dol(self,kroki):
#         self.y=self.y-kroki*self.krok
#
#     def idz_w_lewo(self,kroki):
#         self.x=self.x-kroki*self.krok
#
#     def gdzie_jestem(self):
#         return 'wspolzedne x:'+str(self.x)+' y:'+str(self.y)
#
#
# robak = Robaczek(0,0,10)
# cos.idz_w_gore(4)
# cos.idz_w_prawko(2)
# cos.idz_w_dol(3)
# cos.idz_w_lewo(1)
# print(robak.gdzie_jestem())