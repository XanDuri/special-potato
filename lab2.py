#zad1
lista=['Piłka nożna','Piłka siatkowa','Sport żużlowy','Skoki narciarskie','Piłka ręczna','Koszykówka']

print(lista)

lista.reverse()

print(lista)

lista.append('Futsal')
lista.append('Hokej na lodzie')

print(lista)

#zad2
slownik={'Dz. U':'Dziennik Ustaw','M.P.':'Monitor Polski','MSiG':'Monitor Sądowy i Gospodarczy','Dz.Urz.NBP':'Dziennik Urzędowy Narodowego Banku Polskiego'}
print(slownik['M.P.'])

#zad3
slownikgier={'2L8':'za późno (ang. Too Late)','4U':'dla Ciebie (ang. For You)','Acc':'konto (ang. Account)','AFK':'zajęty, z dala od klawiatury (ang. Away From Keyboard)'}
print(len(slownikgier))

#zad4
zdanie=input('Podaj zdanie: ')
ile=0
ile=int(ile)
for x in zdanie:
    if x=='a':
        ile+=1
print(ile)

#zad5
a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")
a=int(a)
b=int(b)
c=int(c)
suma=a**b+c
f = open("liczby.txt", "a")
f.write("a^b+c="+str(suma))
f.close()

f = open("liczby.txt", "r")
print(f.readline())

#zad6
a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print("a jest większe od b i c")
elif b>a and b>c:
    print("b jest większe od a i c")
elif c>a and c>b:
    print("c jest większe od b i a")
else:
    print("a, b i c są równe")

#zad7
listakwadrat=[2.4,5,8,2,9.1,4.5]
for x in listakwadrat:
    print(x**x)

#zad8
listaa=[]
x=0
while x<10:
    a=input("Podaj liczbe: ")
    a=int(a)
    if a%2==0:
        listaa.append(a)
    x+=1
print(listaa)

#zad9
import math
x=input("Podaj liczbe: ")
x=int(x)
if x<0:
    print("Blad. Nie można zpotegować liczb ujemnych")
else:
    print(math.sqrt(x))