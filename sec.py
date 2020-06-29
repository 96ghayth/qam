import matplotlib.pyplot as pit
import scipy.io.wavfile
import numpy as np
rate, data = scipy.io.wavfile.read("exemple.wav")
pit.subplots(nrows=2, ncols=2)

fdata = np.copy(data, order='k')


class mype(pit):
    def __init__(self, pit):
        pit.figure()
        super.__init__(self,pit)

    def plot1(self):
        pit.title("espace temporelle")
        pit.xlabel("temp")
        pit.ylabel("amplitude")
        pit.subplot(data)

    def plot2(self):
        pit.subplot(np.fft.fft2(fdata))


mype.plot1()
mype.plot2()
mype.show()
