import pandas as pd
import numpy as np
#zad1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
#zad2
# print(df.loc[df['Liczba']>1000])
#
# imie = df.loc[df['Imie']=='ŁUKASZ']
# print(imie)
#
# m = df.loc[df['Plec']=='M']
# k = df.loc[df['Plec']=='K']
# mm = m[['Liczba']]
# mk = k[['Liczba']]
# print(f'Suma dziewcząt:{mk.sum()}\n Suma chłopców:{mm.sum()}\n')

# m = df.loc[df['Rok']<=2005]
# mk = m[['Liczba']]
# print(mk.sum())
#
# liczba = df[['Liczba']]
# print(liczba.sum())

# m = df.loc[df.groupby(["Rok", "Plec"])["Liczba"].idxmax()]
# print(m)
#
# m = df.loc[df.groupby(["Plec"])["Liczba"].idxmax()]
# print(m)
#zad3
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
print(df)

# m = np.unique(df[['Sprzedawca']])
# m = df.drop_duplicates(['Sprzedawca'])[['Sprzedawca']]
# print(m)

# m = df['Utarg'].nlargest(n=5)
# print(m)

# m = df.groupby(['Sprzedawca']).count()
# print(m)

# m = df.groupby(['Kraj']).count()
# print(m)

# filter1 = (df['Data zamowienia'] > '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
# filter2 = df['Kraj']=='Polska'
#
# print(df.loc[filter1 & filter2].count())

# filter1 = (df['Data zamowienia'] > '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
# print(df.loc[filter1]['Utarg'].mean())

filter1 = (df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] < '2005-01-01')
print(df.loc[filter1])

filter2 = (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] < '2006-01-01')
print(df.loc[filter2])

df.loc[filter1].to_csv('zamówienia_2004.csv', sep=';', decimal=',')
df.loc[filter2].to_csv('zamówienia_2005.csv', sep=';', decimal=',')