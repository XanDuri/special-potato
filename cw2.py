



# x==y równy
# x!=y różny
# x>y wyiększy
# x<y mniejszy
# x>=y wiekszy równy
# x<=y mniejszy równy

# if :#warunrk1
#     #instrukcja1
# elif :#warunek2 else if
#     #instrukcja2
# else:
#     #instrukcja jak reszta zawiedzie

# a=8
# b=7

# if a>b:
#     print("Liczba a jest większe od liczby b")
# elif a<b:
#     print("Liczba a jest mniejsze od liczby b")
# else:
#     print("Liczba a jest równa liczbie b")

# if a==b:
#     print("Liczba a jest równa liczbie b")
# else:
#     print("Liczba a nie jest równa liczbie b")

# a=input('Podaj liczby: ')
# a=int(a)
# print(a)

# print("Działanie a>b i c>d")
# a=input('Podaj liczby a: ')
# b=input('Podaj liczby b: ')
# c=input('Podaj liczby c: ')
# d=input('Podaj liczby d: ')
# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)
# if (a>b) & (c>d):
#     print("a jest wieksze od b i c jest wieksze od c")
# else:
#     print("a jest mniejsze od b lub c jest mniejsze od c")

# for :#licznik in skewencja
#     #instrukcja
# else:
#     #instrukcja lub po zakonczenu

# for a in range(0,7,1):
#     print(a) # 0,1,2,3,4,5,6 pod sobą

# lista = ['cos',4,6.3,'*']
# for a in lista:
#     print(a) # cos, 4, 6.3, * pod sobą
# else:
#     print('wyświetlono wszystkie elementy z listy')

# while #warunek
#     #instrukcja
# else:
#     #instrukcja lub po pętli

# a = 1
# while a < 6:
#   print(a)
#   a += 1

# lista = [4,6,8,7,5,2,1,6,8]
# licznik=0
# liczba=input('wpisz liczbę całkowitą: ')
# while licznik!=len(lista):
#     if int(liczba)-lista[licznik]==0:
#         print('liczba '+str(liczba)+' - '+str(lista[licznik])+' = 0')
#         break
#     else:
#         licznik+=1
# else:
#     print('Żadna z wartości nie dała odpowiedniego wyniku')

# lista1 =[4,6,8,9,4,2,5,6]
# lista2 =[5,7,8,3]
# suma=[]
# for a in lista1:
#     for b in lista2:
#         wynik = a+b
#         suma.append(wynik)
#     print(suma)

# try:
#     #instrukcja które mogą zawierać błąd
# except :#nazwa_błędu
#     #instrukcja po wykryciu błędu
# except :#nazwa_błędu2
#     #instrukcja po wykryciu błędu2
# else:
#     #wynik bez błęfu

# a=input("Podaj pierwszą liczbe: ")
# b=input("Podaj druga liczbe: ")
# try:
#     a=int(a)
#     b=int(b)
#     wynik=a/b
#     print(wynik)
# except ZeroDivisionError:
#     print("Nie dziel przez 0")
# except ValueError:
#     print('nie wczytno liczby całkowitej')

# lista =['a',5,5.6,[1,2,3]]
# slownik={klucz:wartość} {1:10,'a'='b',-1:20-}
# slownik[klucz]
# slownik[nowy_klucz]=wartość_dla_nowego_klucza
# append, insert, extend, pop, remove, del, sort, nevens

# lista=['b',45,3.5,'$',[3,5,6]]
# print(lista)
# lista.append(4)
# print(lista)
# lista.insert(4,'obiekt4')
# print(lista)
# lista.extend()
# slownik={3:20,2:21,1:45,5:67,4:34,6:67,'a':'b'}
# print(slownik)
# slownik[4]=36
# print(slownik)
# del slownik[4]
# print(slownik)
# slownik.pop('a')
# print(slownik)
# print(slownik[5])

