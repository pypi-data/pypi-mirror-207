from cmath import polar as pol
from math import pi

f = 2*pi*60

def setFrequency(freq):
    f = freq

def phasorToFunction(z,freq=f):
    p = pol(z)
    return("f(t) = {}cos({}t + {})".format(p[0],f,p[1]))

def capacitor(c,unit="uf"):
    unitDict = {"f":1,"mf":10**(-3),"uf":10**(-6),"nf":10**(-9)}
    try:
        factor = unitDict[unit]
    except:
        raise Exception("Improper Units")
    return (1/complex(0,f*c*factor))

def resistor(r,unit="kohm"):
    unitDict = {"ohm": 1, "kohm": 10 ** (3)}
    try:
        factor = unitDict[unit]
    except:
        raise Exception("Improper Units")
    return complex(factor*r,0)

def inductor(l,unit="mh"):
    unitDict = {"h":1,"mh":10**(-3),"uh":10**(-6)}
    try:
        factor = unitDict[unit]
    except:
        raise Exception("Improper Units")
    return complex(0,f*l*factor)


def totalZpar(x):
    s = x[0]*x[1]/(x[0]+x[1])
    for element in x[2:]:
        s = s*element/(s+element)
    return s


