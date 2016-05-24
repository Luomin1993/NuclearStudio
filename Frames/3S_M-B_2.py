# -*- coding: utf-8 -*-
import numpy as np
from enthought.mayavi import mlab

const = 2.19967e34
x, y = np.ogrid[0:7000000:200j, 500:1500:100j]
s = const*np.exp(-x/y)*np.sqrt(x)/(y**1.5)
surface = mlab.contour3d(s)
surface.contour.maximum_contour = 15
surface.contour.number_of_contours = 10
surface.actor.property.opacity = 0.4
mlab.figure()

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.figure()

field = mlab.pipeline.scalar_field(s)
mlab.pipeline.volume(field, vmin=1.5, vmax=80)
cut = mlab.pipeline.scalar_cut_plane(field.children[0], plane_orientation="y_axes")
cut.enable_contours = True
cut.contour.number_of_contours = 40
mlab.gcf().scene.background = (0.8, 0.8, 0.8)
mlab.show()
