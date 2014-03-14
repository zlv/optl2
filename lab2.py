from math import *

class Poly :
    coef = []
    def __init__(self, coef0) :
        self.coef = coef0

    def eval(self, x, iDerivative=0) :
        sum = 0
        for i in range(0, len(self.coef)-iDerivative) :
            sum += self.coef[i+iDerivative]*self.find_der_mult(i+iDerivative,iDerivative)*(x**i)
        return sum

    def find_der_mult(self, ix, iDerivative) :
        if iDerivative==0 :
            return 1
        return ix*self.find_der_mult(ix-1,iDerivative-1)

def Bolcano(a, b, poly, eps, x, y) :
    x[0] = (a+b)/2
    der = poly.eval(x[0],1)
    while abs(der)>eps :
        if der>0 :
            b = x[0]
        else :
            a = x[0]
        x[0] = (a+b)/2
        der = poly.eval(x[0],1)
    y[0] = poly.eval(x[0])

a = 0.
b = 10.
poly = Poly([0,-12,2])
eps = 1e-5
x = [0]
y = [0]
Bolcano(a,b,poly,eps,x,y)
print(x)
