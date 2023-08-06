import numpy as np
from numpy import pi
from matplotlib import pyplot as plt


def showImage(m, mainTitle, subTitle, unwrapPhase=0):
    # prints the type of matrix
    # print(m.dtype)
    # creates a figure
    fig = plt.figure()
    # add a grid 1x2 in the 2nd subplot position
    fig.add_subplot(1, 2, 1)
    # plots the magnitude
    plt.imshow(np.abs(m), cmap='gray', interpolation='nearest', vmin=0)
    plt.suptitle(mainTitle)
    plt.title(subTitle + ' Magnitude')
    plt.colorbar()
    # add a grid 1x2 in the 2nd subplot position
    fig.add_subplot(1, 2, 2)
    # if the phase parameter is not provided, the code inside the if will be executed
    phase = np.angle(m)
    if unwrapPhase != 0:
        phase = np.unwrap(np.angle(m))
        # use phase at zero frquency as 0
        i0 = int(phase.shape[0] / 2)
        i1 = int(phase.shape[1] / 2)
        phase0 = phase[i0, i1]
        phase -= phase0
    # plots the phase of the complex numbers
    plt.imshow(phase, cmap='gray', interpolation='nearest')
    plt.title(subTitle + ' Phase')
    plt.colorbar()
    plt.show(block=False)

def showPlot(m, mainTitle):
    #print(m.real)
    real = m.real
    imag = m.imag
    #print(m.imag)
    # creates a figure
    fig = plt.figure()
    plt.suptitle(mainTitle)
    # add a grid 1x2 in the 2nd subplot position
    fig.add_subplot(1, 2, 1)
    plt.plot(real, color = 'blue')
    plt.title('Real')
    fig.add_subplot(1, 2, 2)
    plt.title('Imaginary')
    plt.plot(imag, color = 'blue')
    plt.show(block=False)