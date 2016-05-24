# -*- coding: utf-8 -*-

from enthought.traits.api import Code, HasTraits, Float, Property, cached_property, Int
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import functionhouse
fh=functionhouse.nuetron_rective()

class draft(HasTraits):
    energy = Float(0.5)
    S = Float(4.0)
    V = Float(5.0)
    lamda = Float(1)

    Fi_f = Property(depends_on=['S', 'V','lamda','E','delta_a_f','delta_p_f','delta_s_f','delta_e'])  

    
    @cached_property  
    def _get_Fi_f(self): 
        return fh.Fuel_resonance_nuetron_flex(self.energy,self.S,self.V,self.lamda)
    def draft_y(self,energy):       
          S = 4.0
          V = 5.0
          lamda = 1
          E = energy
          delta_p_f = fh.Breit_Wigner(E,6.67,'p',0,1)
          delta_s_f = 8.9
          delta_e = S/(V*2.4088*10**24)
          delta_a_f = 1.1977/np.sqrt(E)
          Fi_f = (lamda*delta_p_f+delta_e)/((delta_a_f+lamda*delta_s_f+delta_e)*E)
          return Fi_f
        


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
    
