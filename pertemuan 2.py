# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 09:25:11 2021

@author: USER
"""
import numpy as np

def beda_maju(f,xi,h):
    '''
    f: fungsi yang diturunkan
    xi: titik yang diinginkan
    h: interval x
    '''
    return (f(xi+h) - f(xi))/h

def beda_mundur(f,xi,h):
    '''
    f: fungsi yang diturunkan
    xi: titik yang diinginkan
    h: interval x
    '''
    return (f(xi) - f(xi-h))/h

def beda_tengah(f,xi,h):
    '''
    f: fungsi yang diturunkan
    xi: titik yang diinginkan
    h: interval x
    '''
    return (f(xi+h) - f(xi-h))/(2*h)

def beda_tengah_orde_2(f,xi,h):
    return (f(xi+h) - (2*f(xi)) + f(xi-h))/h**2

def mclaurin(f,xi,h):
    return (1/(12*h)) * (f(xi-(2*h)) - (8*f(xi-h)) + (8*f(xi+h)) - f(xi+(2*h)))

def error_relatif(nilai_eksak, nilai_pendekatan):
    return np.abs((nilai_eksak - nilai_pendekatan)/nilai_eksak) * 100

f = lambda x: (x**3 - (4*x*np.sin(x**2))) / ((8*x*np.exp(x)) - (5*np.log(x)))
h = 0.01
xi = 1

metode_2_titik_maju = beda_maju(f,xi,h)
metode_2_titik_mundur = beda_mundur(f,xi,h)
metode_3_titik_tengan = beda_tengah(f,xi,h)

metode_5_titik = mclaurin(f,xi,h)

print('metode 2 titik')
print(f'beda maju = {metode_2_titik_maju}')
print(f'beda mundur = {metode_2_titik_mundur}')
print('\n')

print('metode 3 titik')
print(f'beda tengah = {metode_3_titik_tengan}')
print('\n')

print(f'metode 5 titik = {metode_5_titik}')
print('\n')
print('===============================================')


y = lambda x: np.sin(x)
y_analitik = lambda x: np.cos(x)

metode_3_titik = beda_tengah(y,xi,h)
print('metode 3 titik')
print(f"y' = {metode_3_titik}")
error_metode_3_titik = error_relatif(y_analitik(1), metode_3_titik)
print(f'error untuk metode 3 titik\n{error_metode_3_titik}%')
print('\n')

metode_5_titik1 = mclaurin(y,xi,h)
print('metode 5 titik')
print(f"y' = {metode_5_titik1}")
error_metode_5_titik = error_relatif(y_analitik(1), metode_5_titik1)
print(f'error untuk metode 5 titik\n{error_metode_5_titik}%')
print('===============================================')


y_analitik_orde_2 = lambda x: -np.sin(x)

turunan_kedua = beda_tengah_orde_2(y,xi,h)
print(f'y" = {turunan_kedua}\n')
error_turunan_kedua = error_relatif(y_analitik_orde_2(1), turunan_kedua)
print(f'error untuk turunan kedua\n{error_turunan_kedua}%')
























