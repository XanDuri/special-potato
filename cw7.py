import math

import numpy as np

# a = np.array([12,34,567,234])
# b = np.arange(4)
#
# c = a + b
#
# print(c)
# print(b**2)
#
# print(np.exp(b))
# print(np.sqrt(b))
# d = np.sqrt(b)
# e = d + b
# print(e)
#
# a = np.arange(12).reshape((3,4))
# print(a)
# print('')
# print(a.sum())
# print('')
# print(a.sum(axis=0))
# print('')
# print(a.sum(axis=1))
# print('')
# print(a.cumsum(axis=1))

# a = np.arange(3)
# b = np.arange(3)
#
# print(a.dot(b))
#
# c = np.array([[2, 3, 6], [5, 1, 3]])
# d = np.array([[1, 4], [2, 1], [3, 5]])
# e = c.dot(d)
# print(e)

# a = np.arange(6).reshape(3, 2)
# print(a)
# # for b in a:
# #     for c in b:
# #         print(c)
# #     print(b)
# for b in a.flat:
#     print(b)

# a = np.arange(6)
# print(a)
# b = a.reshape((3,2))
# c = a.reshape((2,3))
# print(b)
# print(c)
# d = c.ravel()
# print(d)
# e = c.T
# print(e)
#========================lab 7==========================
# #zad1
# a = np.array([1,2,3])
# b = np.array([3,2,1])
# print(a*b)
#zad2
# a = np.arange(9).reshape(3,3)
# b = np.arange(16).reshape(4,4)
# print(a)
#
# print('')
# max = a[0,0]
# for c in a:
#     print(c)
#     for d in c:
#         if max<d:
#             max=d
#     print(max)
# print('')
# max = a[0,0]
# for c in b:
#     print(c)
#     for d in c:
#         if max<d:
#             max=d
#     print(max)
# print('')
#
# max = a[0,0]
# for c in a:
#     for i in range(0,2):
#         if max<c[i]:
#             max=c[i]
#     print(max+1)
# print('')
# max = a[0,0]
# for c in b:
#     for i in range(0,3):
#         if max<c[i]:
#             max=c[i]
#     print(max+1)
#zad3
# a = np.array([12,34,567,234])
# b = np.arange(1,5,1)
# print(a/b)
#zad4
# a = np.array([1,2,3])
# # b = np.array([-3,2.3,math.sqrt(5)])
# # print(a*b)
#zad5
# a = np.array([[2,4,7],[6,8,4]])
# a = np.sin(a)
# print(a)
#zad6
# b = np.array([[2,4,7],[6,8,4]])
# b = np.cos(b)
# print(b)
#zad7
# print(b+a)
#zad8
# a = np.arange(9).reshape(3,3)
# for i in range(0,3):
#     for b in a:
#         print(b[i])
#     print('')
#zad9
# a = np.arange(9).reshape(3,3)
# for b in a.flat:
#     print(b)
#zad10
# a = np.arange(81).reshape(9,9)
# print(a)
#zad11
# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print(np.ravel(a))
# a = a.reshape((3,4))
# print(a)
# print(np.ravel(a))
# a = a.reshape((4,3))
# print(a)
# print(np.ravel(a))
# a = a.reshape((2,6))
# print(a)
# print(np.ravel(a))