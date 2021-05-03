#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:01:00 2020

@author: alejandrobellonbranas
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
excel=pd.ExcelFile('Python.xlsx')
df = excel.parse('Hoja1')
aux=df['N']
aux2=df['poisincert']
aux=np.array(aux)
aux2=np.array(aux2)
part=np.zeros(len(aux))
incert=np.zeros(len(aux2))
for i in range (len(aux)):
    part[i]=aux[i]
    incert[i]=aux2[i]
part.reshape(1,150)
def poisson(k, lamb):
    return 150*(lamb**k/factorial(k))*np.exp(-lamb)
plt.close('all')
fig, ax = plt.subplots()
ax.hist(aux,bins=30,alpha=0.3,color='red')
y,x=np.histogram(aux,bins=30)
x = x + (x[1]-x[0])/2
x = np.delete(x,-1)
parameters, cov_matrix = curve_fit(poisson, x,y, p0=[30.])
x_new = np.linspace(10,50, 100)
ax.plot(x_new, poisson(x_new, *parameters), color='black')
#ax.plot(x_new,poisson(x_new,25),color='red')
plt.xlabel(r'$n (cuentas\cdot (5s)^{-1})$')
plt.ylabel('Frecuencia')
plt.show()
