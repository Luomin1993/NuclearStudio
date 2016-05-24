# -*- coding: utf-8 -*-

from enthought.traits.api import Code, HasTraits, Float, Property, cached_property, Int
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import functionhouse
fh=functionhouse.nuetron_rective()

class draft(HasTraits):
    t=Float(0)
    T=Float(68)
    similar_type=Code('singlegroup')
    tho_0=Float(0.5)

    n = Property(depends_on=['t', 'T','similar_type','tho_0'])  

    
    @cached_property  
    def _get_n(self): 
        return fh.slower_issue_nuetron_similar(self.t,self.T,self.similar_type,self.tho_0)
    def draft_y(self,t):       
          tho=0.5
          T=68
          tho_0=0.5
          k_eff =0.98
          beta =0.0065
          l =1.01*10**(-4)
          lamda =0.078
          n_0 =1
          alif = l
          n = (n_0/(beta-tho))*(beta*np.exp(lamda*tho*t/(beta-tho))-tho*np.exp((tho-beta)*t/alif))
          return n
        


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
    
