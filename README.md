# data_management
for easy calculations of binomial and hypergeometry distributions in MDM4UI

/* DISCLAIMER
I DO NOT TAKE ANY RESPONSIBLITITY OF GETTING LOW SCORES OR FORGETTING FORMULAS
ON TESTS BECAUSE YOU DID NOT PRACTICE SOLVING THE PROBLEMS BY HAND.
YOU ARE THE ONE WHO IS TAKING FULL RESPONSIBILITY FOR USING THIS PROGRAM.
*/

General keywords:
  v: value 
  s: sum of the P(X) in the range given 
  k: 1 - Sum(P(X)) in the given range (it overrides 's' function!)
  
HOW TO USE binomial.py:
  1. execute binomial.py.
  2. type in "v x n p" to calculate value. (x = # of sucesses you want, n = # of samples, p = probability)
  WARNING: probability does not support fractions !!! 
  3. for sum, type in "s end n p start" 
     (the range is inclusive, so it calculates sum of P(X=x) which is start =< x <= end)   
  4. for command 'k', it is same as 'sum' above, but just it subtracts the sum from 1.
      
HOW TO USE hypergeometry.py:
  1. execute hypergeometry.py
  2. type in "v x k n N" to calculate value. (x = # of sucesses you want, k = # of successes, n = # of samples, N = # of population)
  3. for sum, type in "s end k n N start"
       (the range is inclusive, so it calculates sum of P(X=x) which is start =< x <= end)
  4. for command 'k', it is same as 'sum' above, but just it subtracts the sum from 1.


I wish this program would help many people who is having a hard time solving distribution problems.
