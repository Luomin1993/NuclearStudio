classdef BCC
   properties
      Model = 'BCC';
      SampleNumber = 0;
      Company
      Insult
   end
   
   properties (Dependent)
      Modulus
   end
   
   methods
      function [x,y] = st(X,Y,judge)
         [m,n] = size(X);
         [s,n] = size(Y);
         seta = inv(X(judge)*X);
         c = seta;
         a = Y;
         b = Y[judge];
         lamda = linprog(c,a,b,[],[],zeros(n,1));
         lamda = lamda'
         x = X[judge]*lamda
         y = Y[judge]*lamda     
      end % Material set function
      
      function seta = SETA()
      end % Modulus get function
   end
end % classdef