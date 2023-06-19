# %%
import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from math import sqrt

df = pandas.read_csv("meting zaklamp 19-06.csv", delimiter=",", header=11)
# debug = df[df.columns[5]]
# print("hello")
print(df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
df.plot(df.columns[0], df.columns[1])

#%%
def pixel_to_wave(pixel, calibration):
    return calibration[3]*pixel**3 + calibration[2]*pixel**2 + calibration[1]*pixel + calibration[0]


def time_to_pixel(time):
    return 531.1077 * time * 1000
awnser = (455.437295891728, 0.0990275839844787, -1.91594053559167e-5, 2.641851052438e-9)

print(pixel_to_wave(time_to_pixel(6.59/1000), awnser))
print(pixel_to_wave(time_to_pixel(5.75/1000), awnser))
print(pixel_to_wave(time_to_pixel(3.46/1000), awnser))
print(pixel_to_wave(time_to_pixel(4.35/1000), awnser))

#%%
wavelength = [pixel_to_wave(time_to_pixel(u), awnser) for u in df[df.columns[0]]]

plt.plot(wavelength, df[df.columns[1]])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Flashlight spectrum")