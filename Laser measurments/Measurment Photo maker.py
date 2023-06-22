# %%
import pandas
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import scipy.signal
from math import sqrt

# df = pandas.read_csv(".\laser measurments\\no feedback no lasing 25mA 19-06.csv", delimiter=",", header=11)
df_5_03 = pandas.read_csv("fb 28mA zoom photo 65 19-06.csv", delimiter=",", header=11)
df_5_07 = pandas.read_csv("fb 28mA photo 66 19-06.csv", delimiter=",", header=11)
df_5_14 = pandas.read_csv("fb 28mA photo 67 19-06.csv", delimiter=",", header=11)
df_5_23 = pandas.read_csv("fb 28mA photo 68 19-06.csv", delimiter=",", header=11)
df_5_35 = pandas.read_csv("fb 28mA photo 69 19-06.csv", delimiter=",", header=11)
df_5_42 = pandas.read_csv("fb 28mA photo 70 19-06.csv", delimiter=",", header=11)
df_5_45 = pandas.read_csv("fb 28mA photo 71 19-06.csv", delimiter=",", header=11)
# debug = df[df.columns[5]]
# print("hello")

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
wavelength_5_03 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_03[df_5_03.columns[0]]]
wavelength_5_07 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_07[df_5_07.columns[0]]]
wavelength_5_14 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_14[df_5_14.columns[0]]]
wavelength_5_23 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_23[df_5_23.columns[0]]]
wavelength_5_35 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_35[df_5_35.columns[0]]]
wavelength_5_42 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_42[df_5_42.columns[0]]]
wavelength_5_45 = [pixel_to_wave(time_to_pixel(u), awnser) for u in df_5_45[df_5_45.columns[0]]]

plt.plot(wavelength_5_03, -df_5_03[df_5_03.columns[1]] + df_5_03[df_5_03.columns[1]][0])
plt.plot(wavelength_5_07, df_5_07[df_5_07.columns[1]])
plt.plot(wavelength_5_14, df_5_14[df_5_14.columns[1]])
plt.plot(wavelength_5_23, df_5_23[df_5_23.columns[1]])
plt.plot(wavelength_5_35, df_5_35[df_5_35.columns[1]])
plt.plot(wavelength_5_42, df_5_42[df_5_42.columns[1]])
plt.plot(wavelength_5_45, df_5_45[df_5_45.columns[1]])
plt.xlabel("Wavelength (nm)")
plt.ylabel("Voltage of CCD (V)")
plt.title("Laser spectrums no feedback at different currents")
plt.legend(["5.03", "5.07", "5.14", "5.23", "5.35", "5.42", "5.45"])
# plt.savefig(".\Results laser spectrum\\no feedback lasers.png")


#%%

laag_awnser = ( 385.1606129985135 ,  0.20507857375061167 ,  -7.082912427871432e-05 ,  1.0637860565863035e-08 )
hoog_awnser = ( 571.3360064523338 ,  -0.06993891669523987 ,  6.094958265140709e-05 ,  -9.567140742623202e-09 )

avaraged_5_03 = []
avaraged_5_07 = []
avaraged_5_14 = []
avaraged_5_23 = []
avaraged_5_35 = []
avaraged_5_42 = []
avaraged_5_45 = []

avarage_length = 1000
for i in range(0, len(wavelength_5_03), avarage_length):
    avaraged_5_03.append((-np.mean(df_5_03[df_5_03.columns[1]][i:i+avarage_length])+ df_5_03[df_5_03.columns[1]][0])/0.8444078590000001)
    avaraged_5_07.append((-np.mean(df_5_07[df_5_07.columns[1]][i:i+avarage_length])+ df_5_07[df_5_07.columns[1]][0])/0.8444078590000001)
    avaraged_5_14.append((-np.mean(df_5_14[df_5_14.columns[1]][i:i+avarage_length])+ df_5_14[df_5_14.columns[1]][0])/0.8444078590000001)
    avaraged_5_23.append((-np.mean(df_5_23[df_5_23.columns[1]][i:i+avarage_length])+ df_5_23[df_5_23.columns[1]][0])/0.8444078590000001)
    avaraged_5_35.append((-np.mean(df_5_35[df_5_35.columns[1]][i:i+avarage_length])+ df_5_35[df_5_35.columns[1]][0])/0.8444078590000001)
    avaraged_5_42.append((-np.mean(df_5_42[df_5_42.columns[1]][i:i+avarage_length])+ df_5_42[df_5_42.columns[1]][0])/0.8444078590000001)
    avaraged_5_45.append((-np.mean(df_5_45[df_5_45.columns[1]][i:i+avarage_length])+ df_5_45[df_5_45.columns[1]][0])/0.8444078590000001)

errorx_5_03 = []
errorx_5_07 = []
errorx_5_14 = []
errorx_5_23 = []
errorx_5_35 = []
errorx_5_42 = []
errorx_5_45 = []

errory_5_03 = []
errory_5_07 = []
errory_5_14 = []
errory_5_23 = []
errory_5_35 = []
errory_5_42 = []
errory_5_45 = []
for i in range(len(avaraged_5_03)):
    errorx_5_03.append(abs(pixel_to_wave(time_to_pixel(df_5_03[df_5_03.columns[0]][i*avarage_length]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_03[df_5_03.columns[0]][i*avarage_length]), hoog_awnser)))
    # errorx_5_07.append(wavelength_5_07[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_07[df_5_07.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_07[df_5_07.columns[0]]), hoog_awnser)))
    # errorx_5_14.append(wavelength_5_14[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_14[df_5_14.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_14[df_5_14.columns[0]]), hoog_awnser)))
    # errorx_5_23.append(wavelength_5_23[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_23[df_5_23.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_23[df_5_23.columns[0]]), hoog_awnser)))
    # errorx_5_35.append(wavelength_5_35[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_35[df_5_35.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_35[df_5_35.columns[0]]), hoog_awnser)))
    # errorx_5_42.append(wavelength_5_42[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_42[df_5_42.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_42[df_5_42.columns[0]]), hoog_awnser)))
    # errorx_5_45.append(wavelength_5_45[i*avarage_length] + abs(pixel_to_wave(time_to_pixel(df_5_45[df_5_45.columns[0]]), laag_awnser) - pixel_to_wave(time_to_pixel(df_5_45[df_5_45.columns[0]]), hoog_awnser)))

    errory_5_03.append(np.std(df_5_03[df_5_03.columns[1]][i:i+avarage_length]))
    errory_5_07.append(np.std(df_5_07[df_5_07.columns[1]][i:i+avarage_length]))
    errory_5_14.append(np.std(df_5_14[df_5_14.columns[1]][i:i+avarage_length]))
    errory_5_23.append(np.std(df_5_23[df_5_23.columns[1]][i:i+avarage_length]))
    errory_5_35.append(np.std(df_5_35[df_5_35.columns[1]][i:i+avarage_length]))
    errory_5_42.append(np.std(df_5_42[df_5_42.columns[1]][i:i+avarage_length]))
    errory_5_45.append(np.std(df_5_45[df_5_45.columns[1]][i:i+avarage_length]))
#%%
print(len(errory_5_03))
print(len(avaraged_5_03))
print(errorx_5_03)
print(abs(pixel_to_wave(2000, laag_awnser) - pixel_to_wave(2000, hoog_awnser)))
# print([wavelength_5_03[::avarage_length][i] + errorx_5_03[i] for i in range(len(avaraged_5_03))])

#%%
gs = gridspec.GridSpec(4, 1, height_ratios=[4, 4, 4, 4]) 
plt.rcParams.update({'font.size': 22})

fig = plt.figure(figsize=(15, 15))
ax1 = plt.subplot(gs[0])
plt.title("Averaged Laser spectrum no feedback lasing at 25mA")
ax2 = plt.subplot(gs[1], sharex=ax1)
ax3 = plt.subplot(gs[2], sharex=ax1)
ax4 = plt.subplot(gs[3], sharex=ax1)
print(avaraged_5_07[100])
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax2.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklabels(), visible=False)
# ax2.yaxis.get_major_ticks()[-1].label1.set_visible(False)
# ax2.yaxis.get_major_ticks()[-1].label1.set_visible(False)
# ax3.yaxis.get_major_ticks()[-1].label1.set_visible(False)
plt.subplots_adjust(hspace=.0)
# ax1 = fig.add_subplot(411)
# ax2 = fig.add_subplot(412, sharex=True)
# ax3 = fig.add_subplot(413, sharex=ax2)
# ax4 = fig.add_subplot(414, sharex=ax3)
ax1.plot(wavelength_5_03[::avarage_length], avaraged_5_03)
ax1.fill_between(wavelength_5_03[::avarage_length], [avaraged_5_03[i] + errory_5_03[i] for i in range(len(avaraged_5_03))], [avaraged_5_03[i] - errory_5_03[i] for i in range(len(avaraged_5_03))], alpha=0.5)
# ax1.fill_betweenx(avaraged_5_03, x1=[wavelength_5_03[500:len(wavelength_5_03):avarage_length][i] + 0.1*errorx_5_03[i] for i in range(len(avaraged_5_03))], x2=[wavelength_5_03[500:len(wavelength_5_03):avarage_length][i] - 0.001*errorx_5_03[i] for i in range(len(avaraged_5_03))], alpha=0.5,facecolor='red')
# ax1.fill_betweenx(avaraged_5_03, [630+i*0.001 for i in range(len(avaraged_5_03))], [625+i*0.001 for i in range(len(avaraged_5_03))], alpha=0.5)
# plt.plot(wavelength_5_07[::avarage_length], avaraged_5_07)
# plt.plot(wavelength_5_14[::avarage_length], avaraged_5_14)
ax2.plot(wavelength_5_23[::avarage_length], avaraged_5_23)
ax3.plot(wavelength_5_35[::avarage_length], avaraged_5_35)
ax4.plot(wavelength_5_42[::avarage_length], avaraged_5_42)
ax1.set_ylim([-0.1, 2.3])
ax2.set_ylim([-0.1, 2.3])
ax3.set_ylim([-0.1, 2.3])
ax4.set_ylim([-0.1, 2.3])
ax1.yaxis.set_ticks(np.arange(0, 2.3, 0.5))
ax2.yaxis.set_ticks(np.arange(0, 2.3, 0.5))
ax3.yaxis.set_ticks(np.arange(0, 2.3, 0.5))
ax4.yaxis.set_ticks(np.arange(0, 2.3, 0.5))
ax1.legend(["$16.97^\circ$"])
ax2.legend(["$16.77^\circ$"])
ax3.legend(["$16.65^\circ$"])
ax4.legend(["$16.58^\circ$"])
# ax4.plot(wavelength_5_45[::avarage_length], avaraged_5_45)
# plt.legend(["28mA", "25mA"])
fig.text(0.06, 0.5, 'Relative intensity', va='center', rotation='vertical')
plt.xlabel("Wavelength (nm) $\pm 10$nm")
# plt.ylabel("Voltage of CCD (V)")
plt.savefig(".\Results laser spectrum\\feedback lasers averaged.svg")
# angle is grating normal to mirror normal
# Relative to light from non feedback lasing laser
