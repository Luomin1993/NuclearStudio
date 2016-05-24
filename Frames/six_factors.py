# -*- coding: utf-8 -*-


from enthought.traits.api import HasTraits, Float, Property, cached_property

class Rectangle(HasTraits):
    kesai = Float(1.05) 
    p = Float(0.9)
    f = Float(0.882)
    nita = Float(1.335)
    alif_s = Float(0.952)
    alif_d = Float(0.94)

    
    k_eff = Property(depends_on=['kesai', 'p','f','nita','alif_s','alif_d'])  

    
    @cached_property  
    def _get_k_eff(self): 
        
        print 'recalculating'
        return self.p*self.f*self.kesai*self.nita*self.alif_s*self.alif_d

if __name__ == "__main__":
    r = Rectangle()
    
    r.edit_traits()
    r.configure_traits()
    
