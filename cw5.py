# class Ksztalty():
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#         self.opis= 'To będzie klasa dla ogólnych ksztaltow'
#
#     def pole(self):
#         return self.x * self.y
#
#     def obwod(self):
#         return 2*self.x + 2 * self.y
#
#     def dodaj_opis(self, text):
#         self.opis=text
#
#     def skalowanie(self, czynnik):
#         self.x=self.x*czynnik
#         self.y=self.y*czynnik
#
# class Kwadrat(Ksztalty):
#     def __init__(self,x):
#         self.x=x
#         self.y=x
#
#     def __str__(self):
#         return f'Kwadrat o boku {self.x}'
#
# class KwadratLiteraL(Kwadrat):
#     def obwod(self):
#         return 8*self.x
#     def pole(self):
#         return 3*self.x*self.y
#
# kwadrat = Kwadrat(5)
# print(kwadrat)
# print(kwadrat.obwod())
# print(kwadrat.pole())
# kwadrat.dodaj_opis("Nasza figura to kwadrat")
# print(kwadrat.opis)
# kwadrat.skalowanie(0.3)
# print(kwadrat.obwod())
# print("")
#
# litera_l=KwadratLiteraL(5)
# print(litera_l.obwod())
# print(litera_l.pole())
# litera_l.dodaj_opis("Litera L")
# print(litera_l.opis)
# litera_l.skalowanie(0.5)
# print(litera_l.obwod())

# class Osoba:
#     def __init__(self,imie,nazwisko):
#         self.imie=imie
#         self.nazwisko=nazwisko
#
#     def przedstaw_sie(self):
#         return f"{self.imie} {self.nazwisko}"
#
# class Pracownik(Osoba):
#     def __init__(self,imie,nazwisko,pensja):
#         Osoba.__init__(self,imie,nazwisko)
#         self.pensja=pensja
#
#     def przedstaw_sie(self):
#         return f"{self.imie} {self.nazwisko} i zarabiam {self.pensja}"
#
# class Menadzer(Pracownik):
#     def przedstaw_sie(self):
#         return f"{self.imie} {self.nazwisko}, jestem menadzerem i zarabiam {self.pensja}"
#
# jozek=Pracownik('Józef', 'Bajka', 2000)
# ja=Menadzer('Łukasz', 'Moszczyński', 0)
#
# print(jozek.przedstaw_sie())
# print(ja.przedstaw_sie())

# for element in range(1,11):
#     print(element)
#
# imie='Łukasz'
# it = iter(imie)
# print(it)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# class Wspak:
#     def __init__(self,data):
#         self.data=data
#         self.index=len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index==0:
#             raise StopIteration
#         self.index=self.index-1
#         return self.data[self.index]
#
# napis=Wspak('Piła-motorowa')
# print(napis.__next__())
# for a in napis:
#     print(a)

# def reverse(data):
#     for index in range(len(data)-1,-1,-1):
#         yield data[index]
#
# gen=reverse('Kajak')
# print(next(gen))
# print("Stun Seed")
# print(next(gen))

# litery =(litera for litera in 'Kokojambo')
# print(litery)
# print(next(litery))
