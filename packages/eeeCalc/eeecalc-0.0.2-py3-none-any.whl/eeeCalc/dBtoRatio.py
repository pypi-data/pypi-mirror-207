from math import log10

def volRatioToDB(vol):
    return(20*log10(vol))

def powRatioToDB(pow):
    return(10*log10(pow))

def dBToVolRatio(db):
    return(10**(db/20))

def dBToPowRatio(db):
    return(10**(db/10))
