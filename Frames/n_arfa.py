# -*- coding: utf-8 -*-
"""
使用带缓存和监听功能的Property属性
"""

from enthought.traits.api import HasTraits, Float, Property, cached_property

class n_gama_process(HasTraits):
    X_A = Float(238.0)
    n_A = Float(1.0)
    X_Z = Float(92.0)
    n_Z = Float(0.0)

    #area是一个属性，当width,height的值变化时，它对应的_get_area函数将被调用
    Y_A = Property(depends_on=['X_A'])
    Y_Z = Property(depends_on=['X_Z'])

    # 通过cached_property修饰器缓存_get_area()的输出
    @cached_property  
    def _get_Y_A(self): 
        "area的get函数，注意此函数名和对应的Proerty名的关系"
        print '(n,gama) rective is on'
        return self.X_A+1
    def _get_Y_Z(self): 
        "area的get函数，注意此函数名和对应的Proerty名的关系"
        print 'one gama is on'
        return self.X_Z
    
if __name__ == "__main__":
    n_g = n_gama_process()
    n_g.edit_traits()
    n_g.configure_traits()
    
