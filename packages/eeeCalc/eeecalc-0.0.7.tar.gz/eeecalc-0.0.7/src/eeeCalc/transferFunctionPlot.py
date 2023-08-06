import matplotlib.pyplot as plt
from math import log10 as log
from math import pi
import numpy as np
from cmath import polar as pol

def transferFunctionPlot(sDomainFunc,lowerLog=-1,upperLog=7,pointsPerDecade=2000,Hz=False,dB=True,degrees=True,saveFig=False,fileName="transferPlot.png"):
    """
    :param sDomainFunc: Function to be plotted
    :param lowerLog: log base 10 of the lower bound for frequency
    :param upperLog: log base 10 of the upper bound for frequency
    :param pointsPerDecade: data points calculated per decade
    :param Hz: True uses Hz for frequency, False uses rad/s for frequency
    :param dB: True uses dB for magnitude, False uses just log base 10 of gain for magnitude
    :param degrees: True uses degrees for phase, False uses radians for phase
    :param saveFig: True saves fig, False displays it
    :param fileName: Name of file to be saved - default is "transferPlot.png"
    :return: nothing - plot is either displayed or saved
    """
    pointsTot = pointsPerDecade*(upperLog-lowerLog)
    inp = np.linspace(lowerLog,upperLog,pointsTot)
    x = np.zeros(pointsTot)
    yMag = np.zeros(pointsTot)
    yPhase = np.zeros(pointsTot)
    jwFunc = lambda x : sDomainFunc(x*complex(0,1))

    magMult = 1
    if dB:
        magMult = 20

    phaseMult = 1
    if degrees:
        phaseMult = 180/pi

    for i,val in enumerate(inp):
        yMag[i] = magMult*log(pol(jwFunc(10 ** val))[0])
        yPhase[i] = phaseMult*pol(jwFunc(10 ** val))[1]

    if Hz:
        xunit = "Hz"
    else:
        xunit = "rad/s"

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    ax1 = plt.subplot()
    l1, = ax1.plot(inp,yMag, color='blue')
    ax2 = ax1.twinx()
    l2, = ax2.plot(inp,yPhase, color='orange')
    plt.legend([l1, l2], ["Magnitude", "Phase"])



    ax1.set_xlabel("Frequency in {}".format(xunit))


    if dB:
        ax1.set_ylabel("Gain in dB")
    else:
        ax1.set_ylabel("Gain")

    if degrees:
        ax2.set_ylabel("Phase shift in degrees")
    else:
        ax2.set_ylabel("Phase shift in radians")

    if saveFig:
        plt.savefig(fileName)
    else:
        plt.show()


def transientPlot(tFunc,inp,numFourierTerms=1000):
    return
