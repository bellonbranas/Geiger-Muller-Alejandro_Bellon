#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:02:02 2020

@author: alejandrobellonbranas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def funcion(x,a,b):
    f=a/((x+b)**2)
    return f
excel=pd.ExcelFile('Python.xlsx')
df = excel.parse('Hoja1')
v1=df['ruido2']
v2=df['s(ruido2)']
v3=df['Distancia (cm)']
v1=np.array(v1)
v2=np.array(v2)
v3=np.array(v3)
part=np.zeros(20)
dist=np.zeros(20)
error=np.zeros(20)
for i in range(20):
    part[i]=v1[i]
    error[i]=v2[i]
    dist[i]=v3[i]

x_new = np.linspace(0,11, 120)
parameters5, cov_matrix5 = curve_fit(funcion, dist, part, p0=[355., 1.],sigma=error,absolute_sigma=False)
plt.close('all')
plt.figure(1)
plt.plot(x_new, funcion(x_new, *parameters5), color='black')
plt.errorbar(dist,part,yerr=error,xerr=0,color='red',ecolor='tomato',fmt=".")
plt.xlabel(r'd(cm)')
plt.ylabel(r'$n (cuentas\cdot s^{-1})$')
plt.show()
print('Ajuste funcion:')
print('a,b')
print(parameters5)
print('s(a),s(b)')
print(np.sqrt(np.diag(cov_matrix5)))