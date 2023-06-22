# %%
import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from math import sqrt

# df = pandas.read_csv(".\laser measurments\\no feedback no lasing 25mA 19-06.csv", delimiter=",", header=11)
df1 = pandas.read_csv("no fb lasing 28mA 19-06.csv", delimiter=",", header=11)
df2 = pandas.read_csv("no feedback no lasing 25mA 19-06.csv", delimiter=",", header=11)
# debug = df[df.columns[5]]
# print("hello")
print(df1.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
df1.plot(df1.columns[0], df1.columns[1])

#%%
def pixel_to_wave(pixel, calibration):
    return calibration[3]*pixel**3 + calibration[2]*pixel**2 + calibration[1]*pixel + calibration[0]


def time_to_pixel(time):
    return 531.1077 * time * 1000
awnser = (477.954995157329, 0.0679395645886716, -5.0904350757044e-6, 5.55365871246419e-10)

print(pixel_to_wave(time_to_pixel(6.59/1000), awnser))
print(pixel_to_wave(time_to_pixel(5.75/1000), awnser))
print(pixel_to_wave(time_to_pixel(3.46/1000), awnser))
print(pixel_to_wave(time_to_pixel(4.35/1000), awnser))

#%%
wavelength1 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df1[df1.columns[0]]]
wavelength2 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df2[df2.columns[0]]]

plt.plot(wavelength1, df1[df1.columns[1]])
plt.plot(wavelength2, df2[df2.columns[1]])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage of CCD (V)")
plt.title("Laser spectrums no feedback at different currents")
plt.legend(["28mA", "25mA"])
# plt.savefig(".\Results laser spectrum\\no feedback lasers.png")


#%%
avaraged1 = []
avaraged2 = []
avarage_length = 100
fig = plt.figure(figsize=(10, 6))
plt.rcParams.update({'font.size': 18})
for i in range(0, len(wavelength1), avarage_length):
    avaraged1.append((-np.mean(df1[df1.columns[1]][i:i+avarage_length]) + df1[df1.columns[1]][400000])/0.4069576699999997)
plt.plot(wavelength1[::avarage_length][4900:5800], avaraged1[4900:5800])
for i in range(0, len(wavelength2), avarage_length):
    avaraged2.append((-np.mean(df2[df2.columns[1]][i:i+avarage_length])+ np.mean(df2[df2.columns[1]][490000:490000+avarage_length]))/0.4069576699999997)
print(df2[df2.columns[1]][4900])
plt.plot(wavelength2[::avarage_length][4900:5800], avaraged2[4900:5800])
print(avaraged2[4900])
plt.legend(["28mA", "25mA"])
plt.xlabel("Wavelength (nm) $\pm 10$nm")
plt.ylabel("Relative intensity")
plt.title("Avaraged Laser spectrum no feedback lasing at 25mA")
plt.savefig(".\Results laser spectrum\\no feedback lasers avaraged relative.svg")
peak_dataframe1 = pandas.DataFrame(data={"wavelength": wavelength1[::avarage_length][4900:5800], "voltage": avaraged1[4900:5800]})
peak_dataframe2 = pandas.DataFrame(data={"wavelength": wavelength2[::avarage_length][4900:5800], "voltage": avaraged2[4900:5800]})
print(peak_dataframe1)
peak1 = scipy.signal.find_peaks(peak_dataframe1[peak_dataframe1.columns[1]], height=0.3, distance=100)[0]
peak2 = scipy.signal.find_peaks(peak_dataframe2[peak_dataframe2.columns[1]], height=0.1, distance=100)[0]
print(peak1)
#%%
plt.plot(wavelength1[::avarage_length][4900:5800], avaraged1[4900:5800], label="28mA")
plt.plot(wavelength2[::avarage_length][4900:5800], avaraged2[4900:5800], label="25mA")
plt.scatter(peak_dataframe1[peak_dataframe1.columns[0]][peak1], peak_dataframe1[peak_dataframe1.columns[1]][peak1], c="r")
plt.scatter(peak_dataframe2[peak_dataframe2.columns[0]][peak2], peak_dataframe2[peak_dataframe2.columns[1]][peak2], c="r")
result_half1 = scipy.signal.peak_widths(peak_dataframe1[peak_dataframe1.columns[1]], peak1, rel_height=0.5)
result_half2 = scipy.signal.peak_widths(peak_dataframe2[peak_dataframe2.columns[1]], peak2, rel_height=0.5)
plt.hlines(y = result_half1[1], xmin=peak_dataframe1[peak_dataframe1.columns[0]][int(result_half1[2])], xmax=peak_dataframe1[peak_dataframe1.columns[0]][int(result_half1[3])], color="C2", label="FWHM")
plt.hlines(y = result_half2[1], xmin=peak_dataframe2[peak_dataframe2.columns[0]][int(result_half2[2])], xmax=peak_dataframe2[peak_dataframe2.columns[0]][int(result_half2[3])], color="C2")
# plt.legend(["28mA", "25mA", "FWHM"])
plt.legend()
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage of CCD (V)")
plt.title("Avaraged Laser spectrum no feedback lasing at different currents")
#%%
print(peak_dataframe1[peak_dataframe1.columns[1]][peak1[0]])
#%%
print("FWHM of peak at 25mA", peak_dataframe2[peak_dataframe2.columns[0]][int(result_half2[3])] - peak_dataframe2[peak_dataframe2.columns[0]][int(result_half2[2])], "nm")
print("FWHM of peak at 28mA", peak_dataframe1[peak_dataframe1.columns[0]][int(result_half1[3])] - peak_dataframe1[peak_dataframe1.columns[0]][int(result_half1[2])], "nm")