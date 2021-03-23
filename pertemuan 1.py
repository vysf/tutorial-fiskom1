# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:38:13 2021

@author: USER
"""
import numpy as np

f = lambda x: x**2

a = 0   # batas awal
b = 1   # batas akhir
n = 5   # jumlah selang

def trapesium_komposit(f, a, b, n):
    h = (b-a)/n
    
    dx = np.arange(a,b,h)
    
    result = 0
    for i in range(1, n):
        result += f(dx[i])
    
    return (h/2) * (f(a) + (2*result) + f(b))

trapesium_komposit1 = trapesium_komposit(f, a, b, n)
print(f'integral metode trapesium komposit: {trapesium_komposit1}')

def titik_tengah(f, a, b, n):
    h = (b-a)/n
    result = 0
    
    for i in range(0,n):
        result += f(a + (h/2) + (i*h))
    
    result *= h
    return result

titik_tengah1 = titik_tengah(f, a, b, n)
print(f'integral metode titik tengah: {titik_tengah1}')


def simpson13_komposit(f, a, b, n):
    h = (b-a)/n
    dx = np.arange(a,b,h)
    
    genap = 0
    ganjil = 0
    
    for i in range(1,n):
        if i%2 == 0:
            genap += f(dx[i])
        else:
            ganjil += f(dx[i])
    
    return (h/3) * (f(a) + (4*genap) + (2*ganjil) + f(b))

simpson = simpson13_komposit(f, a, b, n)
print(f'integral metode simpson 1/3: {simpson}')
print('\n')

def error_relatif(nilai_eksak, nilai_pendekatan):
    return np.abs((nilai_eksak - nilai_pendekatan)/nilai_eksak) * 100

nilai_eksak = 1/3

error_trapesium = error_relatif(nilai_eksak, trapesium_komposit1)
print(f'error metode trapesium komposit: {error_trapesium}%')

error_midpoint = error_relatif(nilai_eksak, titik_tengah1)
print(f"error metode titik tengah: {error_midpoint}%")

error_simpson = error_relatif(nilai_eksak, simpson)
print(f"error metode simpson 1/3: {error_simpson}%")
































