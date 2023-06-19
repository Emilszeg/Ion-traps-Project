# %%
import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from math import sqrt

df = pandas.read_csv("cal 19-06.csv", delimiter=",", header=11)
# debug = df[df.columns[5]]
# print("hello")
print(df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
df.plot(df.columns[0], df.columns[1])

#%%
valleys = scipy.signal.find_peaks(-df[df.columns[1]], threshold=0.01, height=-2.55)[0]
print(valleys)
print(df[df.columns[1]][valleys[0]])
d = {'seconds': df[df.columns[0]][valleys], 'voltage': df[df.columns[1]][valleys]}
valley_dataframe = pandas.DataFrame(data=d).reset_index()
valley_dataframe

#%%
df.plot(df.columns[0], df.columns[1])
plt.scatter(df[df.columns[0]][valleys], df[df.columns[1]][valleys], c="r")
#%%
# valley_dataframe.plot(valley_dataframe.columns[0], valley_dataframe.columns[1])
valleys2 = scipy.signal.find_peaks(-valley_dataframe[valley_dataframe.columns[2]], width=40, distance=30, height=-2.55)[0]
print(valleys2)
print(valley_dataframe[valley_dataframe.columns[2]][valleys2])
valley_dataframe.plot(valley_dataframe.columns[1], valley_dataframe.columns[2])
plt.scatter(valley_dataframe[valley_dataframe.columns[1]][valleys2], valley_dataframe[valley_dataframe.columns[2]][valleys2], c="r")

#%%
df.plot(df.columns[0], df.columns[1])
plt.scatter(df[df.columns[0]][valley_dataframe[valley_dataframe.columns[0]][valleys2]], df[df.columns[1]][valley_dataframe[valley_dataframe.columns[0]][valleys2]], c="r")
#%%
def pixel_to_wave(pixel, calibration):
    return calibration[3]*pixel**3 + calibration[2]*pixel**2 + calibration[1]*pixel + calibration[0]


def time_to_pixel(time):
    return 531.1077 * time * 1000
wave = [585.25, 609.62, 639.23, 650.23]
print(valley_dataframe.iloc[valleys2[[0, 1, 3, 4]]])
pixel = [time_to_pixel(u) for u in valley_dataframe[valley_dataframe.columns[1]][valleys2[[0, 2, 3, 4]]]]
import sympy
print(pixel)
p, S, B, C, D = sympy.symbols('p S B C D')
equ = S + p * B + p**2 * C + p**3 * D
system_equations = [equ.subs(p, pixel[0]) - wave[0], equ.subs(p, pixel[1]) -
                    wave[1], equ.subs(p, pixel[2])-wave[2], equ.subs(p, pixel[3])-wave[3]]

awnser = sympy.nonlinsolve(system_equations, [S, B, C, D])
print(awnser)

print(pixel_to_wave(time_to_pixel(6.59/1000), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(4.52/1000), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(3.46/1000), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(4.35/1000), awnser.args[0]))

#%%
px = np.linspace(0, 3500, 10000)

lam = pixel_to_wave(px, awnser.args[0])

plt.plot(px, lam)
plt.xlabel("Pixel")
plt.ylabel("Wavelength (nm)")
plt.title("Calibration curve")

#%%
print(df[df.columns[0]])
#%%
wavelength = [pixel_to_wave(time_to_pixel(u), awnser.args[0]) for u in df[df.columns[0]]]

plt.plot(wavelength, df[df.columns[1]])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage (V)")
plt.title("Calibration curve")