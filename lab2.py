from math import *

class Poly :
	coef = []
	def eval(x, iDerivative=0) :
		sum = 0
		for i in range(0, len(coef)-iDerivative) :
			sum += coef[i+iDerivative]*find_der_mult(i+iDerivative,iDerivative)*(x^i)
	def find_der_mult(ix,iDerivative) :
		if iDerivative==0 :
			return 1
		return ix*find_der_mult(ix-1,iDerivative-1)

def eval(x, i=0) :
    if i==0 :
        return 3*x*x-15*x
    elif i==1 :
        return 6*x-15

def brute_force(a, b, n, minx, miny) :
    print('brute_force:')
    inc=(b-a)/(n+1)
    minx[0] = a
    miny[0] = eval(a);
    x=a+inc
    while (x<=b) :
        y = eval(x)
        if y<miny[0] :
            minx[0] = x
            miny[0] = y
        x += inc

def diho(a, b, eps, minx, miny) :
    print('dihotomy:')
    while (b-a>eps) :
        c = (a+b) / 2
        if eval(b) > eval(a) :
            b = c
        else :
            a = c
    minx[0] = (a+b)/2
    miny[0] = eval(minx[0]);

def golden(a, b, eps, minx, miny) :
    print('golden ratio:')
    while (b-a>eps) :
        ratio = (b-a)/((sqrt(5)+1)/2)
        x1 = b-ratio
        x2 = a+ratio
        if eval(x1) > eval(x2) :
            a = x1
        else :
            b = x2
    minx[0] = (a+b)/2
    miny[0] = eval(minx[0]);

fibo_arr = [0,1]
def fibonacci(n) :
    return fibo_arr[n]

def init_fibo(n) :
    for i in range(2,n+1) :
        fibo_arr.append(fibonacci(i-1)+fibonacci(i-2))

def fibo(a, b, n, minx, miny) :
    print('Fibonacci:')
    x1 = a+(b-a)*fibonacci(n-2)/fibonacci(n)
    x2 = a+(b-a)*fibonacci(n-1)/fibonacci(n)
    y1 = eval(x1)
    y2 = eval(x2)
    while (n>1) :
        if y1 > y2 :
            a = x1
            x1 = x2
            minx[0] = x1
            x2 = b-(x1-a)
            y1 = y2
            y2 = eval(x2)
        else :
            b = x2
            x2 = x1
            minx[0] = x2
            x1 = a+(b-x2)
            y2 = y1
            y1 = eval(x1)
        n-=1
    miny[0] = eval(minx[0]);

x = [0.]
y = [0.]
brute_force(0., 10., 10000, x, y)
print(x)
diho(0., 10., 1e-5, x, y)
print(x)
golden(0., 10., 1e-5, x, y)
print(x)
n = 1000
init_fibo(n)
fibo(0., 10., n, x, y)
print(x)
