from math import e

def cosh(z):
    return 0.5*(e**z+e**-z)

def sinh(z):
    return 0.5*(e**z-e**-z)

def tanh(z):
    return sinh(z)/cosh(z)

def cos(z):
    return 0.5*(e**(z*complex(0,1))+e**(-z*complex(0,1)))

def sin(z):
    return 0.5*(e**(z*complex(0,1))-e**(-z*complex(0,1)))*complex(0,-1)

def tan(z):
    return sin(z)/cos(z)
