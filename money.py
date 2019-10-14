import math


# Compound interest
def T(t,r):
  return (1+r)**t


# Net Present Value 
# r: interest rate
# C: List of cash flows
def NPV(r, C):
  s = 0;
  for i in range(len(C)):
    s += C[i] / T(i, r)
  return s


# Future Value
# r: interest rate
# C: List of cash flows
def FV(r, C):
  s = 0;
  for i in range(len(C)):
    s += C[i] * T(i, r)
  return s

