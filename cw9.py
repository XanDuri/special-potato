import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
# print(ts)
# ts.plot()
# # plt.savefig('wykres.png')
# plt.show()

# dane = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela','New Delhi', 'Brasilia','Warszawa'],
#         'Populacja':[147347,3654546,967235,563496],
#         'Kontynet':['Europa','Azja','Ameryka Połódniowa','Europa']}
#
# df = pd.DataFrame(dane)
# grupa = df.groupby('Kontynet').agg({'Populacja':['sum']})
#
# grupa.plot(kind='bar',ylabel='Populacja w mld', xlabel='Kontynent',rot=0, legend=True, title='Populacja dla kontynentów',color='green')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

# df = pd.read_csv('dane.csv', header=0,sep=';',decimal='.')
# print(df)
#
# grupa = df.groupby('Imie i Nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6))
# plt.legend(loc='upper left')
# plt.show()

df = pd.DataFrame(ts)
print(df)
df['Średnia krocząca'] = df.rolling(window=50).mean()
print(df)
df.plot()
plt.legend(['Wartości','Średnai krocząca'])
plt.show()