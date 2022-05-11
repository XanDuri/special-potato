import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# #zad2,1
# t=np.arange(1,20,1)
# s=1/t
# plt.plot(t,s,'g>:')
# plt.legend(labels=['f(x) = 1/x'])
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.title("Wykres funkcji f(x) dla x [1, 20]")
# plt.xlim(0,20.)
# plt.ylim(0,1.)
# plt.show()

# #zad3
# t=np.arange(0,30,0.1)
# a=np.sin(t)
# b=np.cos(t)
# plt.plot(t,a,t,b)
# plt.legend(labels=['sin(x)','cos(x)'])
# plt.show()

#zad4
df = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
print(df)
t = np.arange(0,1,0.1)
x = df[['sepal length']]
y = df[['sepal width']]
s = 
print(x)
# plt.plot()
# plt.show()