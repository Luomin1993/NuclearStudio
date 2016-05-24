# -*- coding: utf-8 -*-

from enthought.traits.api import Code, HasTraits, Float, Property, cached_property, Int
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import functionhouse
fh=functionhouse.nuetron_rective()

class draft(HasTraits):
    S_f=Float(6.67)
    f=Code('r')
    M=Float(6.67)
    T=Float(6.67)

    I = Property(depends_on=['S_F', 'f','M','T'])  

    
    @cached_property  
    def _get_I(self): 
        return fh.resonance_integral(self.S_f,self.M,self.T,self.f)
    def draft_y(self,S_f):       
          a=2.8
          b=27.1
          M=6.67
          T=6.67
          I = (a+b*np.sqrt(S_f/M))*(1+(0.0058+0.005*S_f/M)*(np.sqrt(T)-17.12))
          return I
        


if __name__ == "__main__":
    r = draft()
    r.edit_traits()
    r.configure_traits()

    e = np.linspace(0, 0.003, 0.1)
    y = r.draft_y(e)
    plt.figure(1)
    plt.plot(e, y)
    plt.xlabel("Energy")
    plt.ylabel("wave length")
    plt.show()
    
