# -*- coding: utf-8 -*-
"""
演示matplotlib的三维绘图功能。
"""
import numpy as np
import mpl_toolkits.mplot3d 
import matplotlib.pyplot as plt
from scipy import constants as C

const = 2.19967e34
x, y = np.mgrid[0:7000000:200j, 500:1000:50j] 
z = const*np.exp(-x/y)*np.sqrt(x)/(y**1.5)

ax = plt.subplot(111, projection='3d') 
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap = plt.cm.Blues_r) 
ax.set_xlabel("Energy(eV)")
ax.set_ylabel("Temprature(k)")
ax.set_zlabel("N")
plt.show()
