'''
listaa = []
for i in range(1,11,1):
    listaa.append(i)
print(listaa)

listab = []
for i in range(0,21,2):
    listab.append(i)
print(listab)

listac = []
for i in range(1,11,1):
    listac.append(i*i)
print(listac)

listad = []
for i in range(0,10,1):
    listad.append(0)
print(listad)

listae = []
for i in range(0,10,1):
    if i%2!=0:
        listae.append(1)
    else:
        listae.append(0)
print(listae)

listaf = []
for i in range(0,2,1):
    for j in range(0,5,1):
        listaf.append(j)
print(listaf)

#-----------------zad2-----------
wlista=[]
i = 0
while i < 10:
    i+=1
    wlista.append(i)
print(wlista)

wlistb=[]
i = 0
while i < 21:
    wlistb.append(i)
    i += 2
print(wlistb)

wlistc=[]
i = 0
while i < 11:
    wlistc.append(i*i)
    i += 1
print(wlistc)

wlistd=[]
i = 0
while i < 10:
    wlistd.append(0)
    i += 1
print(wlistd)

wliste=[]
i = 0
while i < 10:
    if i%2==0:
        wliste.append(0)
    else:
        wliste.append(1)
    i += 1
print(wliste)

wlistf=[]
i = 0
while i < 2:
    j = 0
    while j < 5:
        wlistf.append(j)
        j += 1
    i += 1
print(wlistf)
#--------zad3-------
lista = [1,7,-54,8,9,5,-3,4,-7]
def ile_ujemnych(lista):
    ile = 0
    for i in lista:
        if i < 0:
            ile += 1
    print(ile)
ile_ujemnych(lista)
#-------zad4--------
listaa=[1,2,3,4,5,6,7]
def iloczyn(listaa):
    suma = 1
    for i in listaa:
        suma = suma*i
    print(suma)
iloczyn(listaa)

#------zad5---------
lista = [-2,4,7,2,9,10]
def minmax(lista):
    maximum=lista[1]
    minimum=lista[1]
    for i in lista:
        if minimum>i:
            minimum=i
        if maximum<i:
            maximum=i
    print(maximum)
    print(minimum)

minmax(lista)

#-------zad6--------
listaa = [1,2,3,567,4,3,6]
def przemienna(listaa):
    suma=0
    ile=0
    for i in listaa:
        if ile%2==0:
            suma += i
        else:
            suma -= i
        ile += 1
    print(suma)

przemienna(listaa)
'''
#------zad7------
lista =[1,2,3,4,5,6,7,9,0]
size = len(lista)
while size<10:
    liczba = input("Podaj liczbe: ")
    ile=0;
    for i in lista:
        if i==liczba:
            ile += 1
        else:
            ile=0
    if ile == 0:
        lista.append(liczba)
        print(lista)
print(lista)

