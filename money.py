import math


# Compound interest
#
# t : time periods
# r : interest rate
def T(t,r):
  return (1+r)**t
  

# Creates list of compound interest factors.
#
# Returns:
#   (i+r)**0, (i+r)**1, ... , (i+r)**(n-1)  if n>0
#   (i+r)**0, (i+r)**-1, ... , (i+r)**(n+1)  if n<0
#
# Parameters
#   r: interest rate
#   n: number of periods
#
# Example: 
#   get_time_factors(1.5, 5): [1.0, 2.5, 6.25, 15.625, 39.0625] 
#   get_time_factors(1, -4): [1, 0.5, 0.25, 0.125] 
#   get_time_factors(1, 6): [1, 2, 4, 8, 16, 32] 
#  
def get_time_factors(r, n):
  step = -1 if n<0 else 1
  return [ T(i,r) for i in range(0, n, step) ]
  
# Dot product between to vectors
def dot(A, B):
  return sum( [ a*b for a,b in zip(A,B) ] )


# Net Present Value 
# r: interest rate
# C: List of cash flows
def npv(r, C):
  return dot(C, get_time_factors(r, -len(C)) )
  
# Future Value
# r: interest rate
# C: List of cash flows
def fv(r, C):
  return dot(C,  reversed(get_time_factors(r, len(C))) )




