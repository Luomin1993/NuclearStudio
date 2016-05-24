# -*- coding: utf-8 -*-

from enthought.traits.api import Code, HasTraits, Float, Property, cached_property, Int
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import functionhouse
fh=functionhouse.nuetron_rective()

class draft(HasTraits):
    energy=Float(0.5)
    element=Code('H')

    sigma_a_i = Property(depends_on=['energy', 'element'])  

    
    @cached_property  
    def _get_sigma_a_i(self): 
        return fh.sigma_a_i(self.energy,self.element)
    def draft_y(self,energy):       
          
        sigma_a_i = 0.332*np.sqrt(energy)
        return sigma_a_i
        


if __name__ == "__main__":
    r = draft()
    r.edit_traits()
    r.configure_traits()

    e = np.linspace(0, 0.003, 0.1)
    y = r.draft_y(e)
    plt.figure(1)
    plt.plot(e, y)
    plt.xlabel("Energy")
    plt.ylabel("micro rective cross area")
    plt.show()
    
