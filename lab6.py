import numpy as np
# #zad1
# a = np.arange(20)*4
# print(a)
#
# a = np.arange(4,84,4)
# print(a)
# #zad2
# a = np.arange(10,dtype='float')
# print(a)
# print(a.dtype)
# b = np.fromiter(a,dtype='int32')
# print(b)
# print(b.dtype)
#zad3
# def funkcja(n):
#     try:
#         a = np.arange(n,n)
#         print(np.power(2,a))
#     except ValueError:
#         print("Podano złą liczbe.")
#
# funkcja(4)
#zad4
# def funkcja(a,b):
#     try:
#         a = np.arange(b)+1
#         print(np.power(2,a))
#     except ValueError:
#         print("Podano złą liczbe.")
#
# funkcja(2,4)
#zad5
def dlugosc(n):
    a = np.arange(n)
    b = np.flip(a,0)
    print(np.diag([b for b in range(n)],-2))
dlugosc(4)