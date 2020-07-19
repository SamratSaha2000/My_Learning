#                   Integration by trapezoidal method:
#Roll no:

#Registration no: 

from math import *
def f(x):
	return((1-x**2)*tan(x) - x )

def bisection(f,a,b,accur):
	if(f(a)*f(b)>0):
		print("f(a)f(b)< 0 not satisfied in the range [a,b]")
		return None

	
	while((abs(a-b))>accur):
		k=(a+b)/2
		if (f(a)*f(b)<0):
			b=k
		elif(f(a)*f(b)>0):
			a=k
		else:
			if (f(a)==0.0):
				k=a
			break

		print("the root is with in the interval")
		return(k)
m=5
n=7
t=.00000000000000000000000000000000000000001
print(bisection(f,m,n,t))
#OYUTPUT OF THIS :
#the root is with in the interval
#2.5



