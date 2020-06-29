import matplotlib.pyplot as pit
import scipy.io.wavfile
import numpy as np
rate, data = scipy.io.wavfile.read("exemple.wav")
plot1 = pit.figure("espace temporelle")
pit.plot(data)
plot2 = pit.figure("espace frequentielle")
pit.plot(np.fft.fft2(data))
pit.show()