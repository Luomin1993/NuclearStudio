# -*- coding: utf-8 -*-

from enthought.traits.api import Code, HasTraits, Float, Property, cached_property, Int
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import functionhouse
fh=functionhouse.nuetron_rective()

class draft(HasTraits):
    energy=Float(0.5)
    E_r=Float(6.67)
    rec_type=Code('r')
    r=Int(1)
    p=Int(0)

    Breit_Wigner = Property(depends_on=['energy', 'E_r','rec_type','r','p'])  

    
    @cached_property  
    def _get_Breit_Wigner(self): 
        return fh.Breit_Wigner(self.energy,self.E_r,self.rec_type,self.r,self.p)
    def draft_y(self,energy):       
          E_r=6.67
          r=1
          p=0
          delta_0=3.98*10**4
          tao_r = 0.022
          tao_p = 2.63
          tao_n = 0.026
          tao = tao_n+r*tao_r+p*tao_p
          sigma_x = delta_0*(tao_r/tao)*np.sqrt(E_r/energy)*(tao**2/(tao**2+4*((energy-E_r)**2)))
          return sigma_x
        


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
    
