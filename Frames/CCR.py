import numpy as np
import scipy as sp
import sympy as yp

class CCR(object):
	"""docstring for CCR"""
	def __init__(self, value):
		super(CCR, self).__init__()
		self.value = value

	def st(X,Y,m,n,s,judge):
            lamda_init = []
            for j in range(0,n-1):
		    lamda_init.append(1/n)

	    lamda = np.mat('')	

            temp_1 = A*lamda
	    temp_2 = X[judge-1].I
	    seta = temp_1*temp_2
	    st_1 = Y*lamda
            st_2 = sum(lamda)
            cons = ({'type': 'ineq', 'fun': lambda st_1:Y[judge-1] },{'type': 'eq', 'fun': lambda st_2:1})
            res = sp.optiminaze.minisize(seta,lamda_init,args = lamda,constraints = cons)


		
