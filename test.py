import ModulationPy, scipy.io.wavfile
import matplotlib.pyplot as pit
import numpy as np
rate, data = scipy.io.wavfile.read("exemple.wav")
data1d = data.flatten()
data1db = [bin(x) for x in data1d]
qam = ModulationPy.QAMModem(16, gray_map=False, bin_input=True).modulate(data1db)
qam.plot_const()
plot1 = pit.figure("espace temporelle")
pit.plot(data)
plot2 = pit.figure("espace frequentielle")
pit.plot(np.fft.fft2(data))
pit.show()
