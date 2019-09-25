
# Net Present Value

import matplotlib.pyplot as plt
import numpy

# x = numpy.arange(0,10,0.5)
# y = [ i*i for i in x]
# y = [ 30*(1/(1+xi) + (1/((1+xi)**2)) ) for xi in x]

# plt.plot(x, y)
# plt.show()


def cp(ytm, C, FV, n):

  CP = 0
  for i in range(n):
    den = (1+ytm)**(i+1)
    CP += C/den
    if i+1==n:
        CP += FV/den
  return CP

def binsearch(L, R, f, x, n):
  for i in range(n):
    h = (L+R)/2
    if f(h)<=x :
        L = h
    else:
        R = h
  return L

def test1():
  FV = 1000
  CP = 950
  C = 30
  n = 3

  ytm = binsearch(0, 0.50, lambda y: -cp(y, C, FV, n), -CP, 20)

  print("YTM:  %.2f" % (round(ytm*10000)/100), "%" )

  NCP = cp(ytm, C, FV, n)
  print("NCP: ", NCP)

test1()
