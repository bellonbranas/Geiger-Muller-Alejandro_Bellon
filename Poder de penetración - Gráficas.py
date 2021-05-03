#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:18:06 2020

@author: alejandrobellonbranas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from scipy.special import factorial
def linea(x,a,b):
    y=a+b*x
    return y
def polinomio(x,aa,bb,cc,dd):
    yy=aa+bb*x+cc*x**2+dd*x**3
    return yy
def exponencial(x,y0,f,k):
    exp=y0+f*(np.e**(-(x*k)))
    return exp
def expcorrect(x,A,B,C,D):
    expcor=A+B*(np.e**(-(x*C)))+D*x
    return expcor
    
excel=pd.ExcelFile('Python.xlsx')
df = excel.parse('Hoja1')
v1=df['Hojas']
v2=df['ruido']
v3=df['s(ruido)']
v1=np.array(v1)
v2=np.array(v2)
v3=np.array(v3)
part=np.zeros(20)
hojas=np.zeros(20)
partlog=np.zeros(20)
errorpart=np.zeros(20)
errorpartlog=np.zeros(20)
for i in range (20):
    part[i]=v2[i]
    hojas[i]=v1[i]
    partlog[i]=np.log(part[i])
    errorpart[i]=v3[i]
    errorpartlog[i]=errorpart[i]/part[i]

x_new = np.linspace(0,21, 120)
plt.close('all')

'''AJUSTE A UNA LÍNEA'''
'''====================================================================================================='''
parameters, cov_matrix = curve_fit(linea, hojas, partlog, p0=[5., 1.],sigma=errorpartlog,absolute_sigma=False)
plt.figure(1)
plt.plot(x_new, linea(x_new, *parameters), color='black')
plt.errorbar(hojas,partlog,yerr=errorpartlog,xerr=0,color='red',ecolor='tomato',fmt=".")
plt.xlabel(r'Número de hojas')
plt.ylabel('log(n)')
plt.show()



'''AJUSTE A UN POLINOMIO DE GRADO 3'''
'''====================================================================================================='''
parameters2, cov_matrix2 = curve_fit(polinomio, hojas, partlog, p0=[5., 1.,1.,1.],sigma=errorpartlog,absolute_sigma=False)
plt.figure(2)
plt.plot(x_new, polinomio(x_new, *parameters2), color='black')
plt.errorbar(hojas,partlog,yerr=errorpartlog,xerr=0,color='red',ecolor='tomato',fmt=".")
plt.xlabel(r'Número de hojas')
plt.ylabel('log(n)')
plt.show()



'''AJUSTE A UNA EXPONENCIAL'''
'''====================================================================================================='''
parameters3, cov_matrix3 = curve_fit(exponencial, hojas, part, p0=[10., 90.,0.],sigma=errorpart,absolute_sigma=False)
plt.figure(3)
plt.plot(x_new, exponencial(x_new, *parameters3), color='black')
plt.errorbar(hojas,part,yerr=errorpart,xerr=0,color='red',ecolor='tomato',fmt=".")
plt.xlabel(r'Número de hojas')
plt.ylabel(r'$n (cuentas\cdot s^{-1})$')
plt.show()



'''AJUSTE A UNA EXPONENCIAL CORREGIDA'''
'''====================================================================================================='''
parameters4, cov_matrix4 = curve_fit(expcorrect, hojas, part, p0=[35., 90.,1.,-1.],sigma=errorpart,absolute_sigma=False)
plt.figure(4)
plt.plot(x_new, expcorrect(x_new, *parameters4), color='black')
plt.errorbar(hojas,part,yerr=errorpart,xerr=0,color='red',ecolor='tomato',fmt=".")
plt.xlabel(r'Número de hojas')
plt.ylabel(r'$n (cuentas\cdot s^{-1})$')
plt.show()


print('''=========================================================================================''')
print('Ajuste lineal:')
print('a,b')
print(parameters)
print('s(a),s(b)')
print(np.sqrt(np.diag(cov_matrix)))
print('''=========================================================================================''')
print('Ajuste polinómico:')
print('a,b,c,d')
print(parameters2)
print('s(a),s(b),s(c),s(d)')
print(np.sqrt(np.diag(cov_matrix2)))
print('''=========================================================================================''')
print('Ajuste exponencial:')
print('a,b,c')
print(parameters3)
print('s(a),s(b),s(c)')
print(np.sqrt(np.diag(cov_matrix3)))
print('''=========================================================================================''')
print('Ajuste exponencial corregido:')
print('a,b,c,d')
print(parameters4)
print('s(a),s(b),s(c),s(d)')
print(np.sqrt(np.diag(cov_matrix4)))
print('''=========================================================================================''')









