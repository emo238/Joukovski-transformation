# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:42:30 2019

@author: Emeric Villette
"""

import numpy as np
import matplotlib.pyplot as plt

theta=np.linspace(0,2*np.pi,100)

#bonne chance

r=1    #1   #1
a=1.2    #1.2 #1.08
xc=0.1 #0.1 #0.1
yx=0.1 #0.1 #0.2
#%% --------------- Initialisation ---------------
"""
Here we define the circle that we are going to transform
An important parameter of the joukovski transformation is 
the center of the circle that you want to transform
"""

X_center = 0.1
Y_center = 0.1

x=r*np.cos(theta)+X_center
y=r*np.sin(theta)+Y_center

plt.plot(x,y)

z=[]
"""
We then convert each point coordinates into a complex number
"""
for i in range(0,len(x)):
    z.append(complex(x[i],y[i]))

#%% --------------- Beginning ---------------

def f(z):
    z1=[]
    x1=[]
    y1=[]
    for i in range(0,len(z)):
        try:
            z1.append((z[i]+a/z[i]))
            x1.append(z1[i].real)
            y1.append(z1[i].imag)
        except:
            print(z[i])
    return(x1,y1)
    
x1, y1 = f(z)

plt.plot(x1,y1)
plt.show()
plt.axis('equal')