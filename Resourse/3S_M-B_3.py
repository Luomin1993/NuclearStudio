# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

const = 2.19967e34
x, y = np.mgrid[0:700:200j, 300:1500:200j]
z = np.exp(-x/y)*np.sqrt(x)/(y**1.5)
c = const*z

pl = mlab.mesh(x, y, z, scalars=c) 
mlab.axes(xlabel='Energy(eV)', ylabel='Temprature(k)', zlabel='N/2.19967e34')
mlab.outline(pl)
mlab.show()
