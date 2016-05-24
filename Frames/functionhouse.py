#this is the warehouse of the functions.
#we defined the pysical algorithm functions here.
#at the 19:48 of 4.13.2015
#by hanss

import numpy as np
import scipy as sp
import sympy as yp

class nuetron_rective(object):
      def __init__(self):
          pass

      def sigma_a_i(self,energy,element):
          '''Here's the micro rective cross's function,
             sigma_a_i means the rective cross value
             when the nuetron meets the 'i' element.
             this function is useful only when "energy<1ev"
             ----------------------------------------------
             various elements correspond various coefficient'''             
          if energy > 1:
             print 'error! energy must be under 1ev! '
          coefficient={'H':0.332,'H2O':0.664,'He':0.05,'C':0.0034,'Na':0.530}
          sigma_a_i = coefficient[element]*np.sqrt(energy)
          return sigma_a_i

      def Breit_Wigner(self,energy,E_r,rec_type,r,p):
          '''Here's the famous W-S formula, we use this to
             calculate the resonance rective cross, according
             to the situation, the 'r' or 'p' equals to 1 or
             0, means if the rective is on.
             -----------------------------------------------'''         
          delta_0=3.98*10**4
          tao_r = 0.022
          tao_p = 2.63
          tao_n = 0.026
          tao = tao_n+r*tao_r+p*tao_p
          sigma_x = 0
          if rec_type == r:
              sigma_x = delta_0*(tao_r/tao)*np.sqrt(E_r/energy)*(tao**2/(tao**2+4*((energy-E_r)**2)))
          elif rec_type == p:
              sigma_x = delta_0*(tao_p/tao)*np.sqrt(E_r/energy)*(tao**2/(tao**2+4*((energy-E_r)**2)))
          return sigma_x

      def Fuel_resonance_nuetron_flex(self,energy,S,V,lamda):
          '''About the nuetron resonance, in the fuel section,
             this similar formula is abstracted from the feul
             piece's nuetron moderator equation.Which means:
             1 mol nuetrons to correspond the feul piece with
             the volume is 'V' and the surface area is 'S',the
                           ---                         ---
             resonance energy=6.67ev,how much the resonance
             nuetron average flex is.
             lamda=1 regarding to NR and lamda=0 regarding to
             -------                     -------
           NRIM.'''
          E = energy
          delta_a_f = 1.1977/np.sqrt(E)
          delta_p_f = self.Breit_Wigner(E,6.67,'p',0,1)
          delta_s_f = 8.9
          delta_e = S/(V*2.4088*10**24)
          Fi_f = (lamda*delta_p_f+delta_e)/((delta_a_f+lamda*delta_s_f+delta_e)*E)
          return Fi_f

      def resonance_integral(self,S_f,M,T,f):
          '''Here's the effective resonance integral's half
             experience fomula, depends on the fuel piece's
             average temprature T, fuel piece's surface area
             S_f, mass M, and the fuel type(U or UO2).'''
          a = 0
          b = 0
          if f == 'U':
              a = 2.8
              b = 27.1
          elif f == 'UO2':
              a = 5.35
              b = 26.6

          I = (a+b*np.sqrt(S_f/M))*(1+(0.0058+0.005*S_f/M)*(np.sqrt(T)-17.12))
          return I


      def delta_a_f(self,energy):
          return 1.1977/np.sqrt(energy)
        

      def delta_e(self,S,V):
          return S/(V*2.4088*10**24)


      def inaverage_fence_resonance_integral(self,energy,S,V,lamda,delta_E):
          '''It's in the same situation with the function
             Fuel_resonance_nuetron_flex
             -------------------------------------------'''
          I = yp.integral(Fuel_resonance_nuetron_flex(energy,S,V,lamda).Fi_f*delta_e(S,V),E,0,delta_E)
          return I


      def slower_issue_nuetron_similar(self,t,T,similar_type,tho_0):
          ''' t --------------- time.
              T -------------- reactor core reactive cycle time.
              similar_type ------------ 'const' or 'single_group'.
              n_0 --------------- the nuetron density when t = 0.
              '''
           
          k_eff = 0.98
          beta = 0.0065
          l = 1.01*10**(-4)
          lamda = 0.078
          n_0 = 1
          alif = l/k_eff
          tho = 0
          if similar_type == 'const':
             tho = tho_0
             n = (n_0/(tho-beta))*tho*np.exp((tho-beta)*t/alif-beta)

          
          elif similar_type == 'singlegroup':
             tho = alif/T+beta/(T*lamda+1)
             n = (n_0/(beta-tho))*(beta*np.exp(lamda*tho*t/(beta-tho))-tho*np.exp((tho-beta)*t/alif))

          return n                           
              
              
          





















        











        



















          
