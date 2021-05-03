#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:38:28 2020

@author: alejandrobellonbranas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


excel=pd.ExcelFile('Python.xlsx')

df = excel.parse('Hoja1')
v0=df['Ángulo']
v1=df['noiman']
v2=df['s(noiman)']
v3=df['iman']
v4=df['s(iman)']
v5=df['imanaluminio']
v6=df['s(imanaluminio)']
v7=df['aluminio']
v8=df['s(aluminio)']
v0=np.array(v0)
v1=np.array(v1)
v2=np.array(v2)
v3=np.array(v3)
v4=np.array(v4)
v5=np.array(v5)
v6=np.array(v6)
v7=np.array(v7)
v8=np.array(v8)
p1=np.zeros(7)
p2=np.zeros(7)
p3=np.zeros(7)
p4=np.zeros(7)
sp1=np.zeros(7)
sp2=np.zeros(7)
sp3=np.zeros(7)
sp4=np.zeros(7)
ang=np.zeros(7)
for i in range(1,8):
    ang[i-1]=v0[i]
    p1[i-1]=v1[i]
    p2[i-1]=v3[i]
    p3[i-1]=v5[i]
    p4[i-1]=v7[i]
    sp1[i-1]=v2[i]
    sp2[i-1]=v4[i]
    sp3[i-1]=v6[i]
    sp4[i-1]=v8[i]
plt.close('all')
plt.figure(1)    
plt.errorbar(ang,p1,yerr=sp1,color='black',ecolor='black',fmt="o",label='Sin campo EM')    
plt.errorbar(ang,p2,yerr=sp2,color='red',ecolor='red',fmt="o",label='Con campo EM')
plt.xlabel(r'Ángulo(º)')
plt.ylabel(r'$n (cuentas\cdot s^{-1})$')
plt.legend()
plt.figure(2)   
plt.errorbar(ang,p3,yerr=sp3,color='black',ecolor='black',fmt="o",label='Sin campo EM')    
plt.errorbar(ang,p4,yerr=sp4,color='red',ecolor='red',fmt="o",label='Con campo EM')
plt.xlabel(r'Ángulo(º)')
plt.ylabel(r'$n (cuentas\cdot s^{-1})$')
plt.legend()
plt.show()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    