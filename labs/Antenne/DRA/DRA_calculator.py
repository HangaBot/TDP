# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:03:04 2019

@author: alfonso Breglia
Description: Dielectric resonator calculator 
"""

import numpy as np


eps = 3.18

c = 299792458.0
f0 = 9.5 * 10**9#[Hz]

a = 5 *10**(-3)#[m]
h = 5 *10**(-3)#[m]

lambda_ = c / f0  #[m]

kx = np.pi/a
kz = np.pi/(2*h)
#print(kx)
#print(kz)

ky0 = np.sqrt(kx**2 + kz**2)
ky  =  np.sqrt(np.abs((f0 * 2* np.pi *np.sqrt(eps)/c )**2 - (kx**2 + kz**2)))
#print(ky)

d = 2/ky *np.tanh(ky0/ky)

print(a*1000, d*1000, h*1000)
