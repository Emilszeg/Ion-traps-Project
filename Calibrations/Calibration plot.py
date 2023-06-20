import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from math import sqrt
def pixel_to_wave(pixel, calibration):
    return calibration[3]*pixel**3 + calibration[2]*pixel**2 + calibration[1]*pixel + calibration[0]


def time_to_pixel(time):
    return 531.1077 * time * 1000
df = pandas.read_csv(".\Calibrations\cal 19-06.csv", delimiter=",", header=11)
valleys = scipy.signal.find_peaks(-df[df.columns[1]], threshold=0.01, height=-2.55)[0]
print(valleys)
print(df[df.columns[1]][valleys[0]])
d = {'seconds': df[df.columns[0]][valleys], 'voltage': df[df.columns[1]][valleys]}
valley_dataframe = pandas.DataFrame(data=d).reset_index()

awnser = (477.954995157329, 0.0679395645886716, -5.0904350757044e-6, 5.55365871246419e-10)

plt.plot(pixel_to_wave(time_to_pixel(valley_dataframe[valley_dataframe.columns[1]]), awnser), valley_dataframe[valley_dataframe.columns[2]])
plt.show()