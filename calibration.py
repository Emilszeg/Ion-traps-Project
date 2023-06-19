# %%
import sympy

p, S, B, C, D = sympy.symbols('p S B C D')
equ = S + p * B + p**2 * C + p**3 * D
print(equ.subs(p, 1736.72))
print(equ.subs(p, 2756.45))
print(equ.subs(p, 2968.9))
print(equ.subs(p, 2198.79))
print(equ.subs([(B, 0.386976930), (C, -0.0001347436658),
      (D, 1.766982496*10**-8), (S, 227.0331396)]))

# %%


def pixel_to_wave(pixel, calibration):
    return calibration[3]*pixel**3 + calibration[2]*pixel**2 + calibration[1]*pixel + calibration[0]


def time_to_pixel(time):
    return 531.1077 * time

# %%
wave = [585.25, 640.23, 650.65, 614.31]
pixel = [time_to_pixel(2.98), time_to_pixel(
    4.92), time_to_pixel(5.3), time_to_pixel(3.85)]
system_equations = [equ.subs(p, pixel[0]) - wave[0], equ.subs(p, pixel[1]) -
                    wave[1], equ.subs(p, pixel[2])-wave[2], equ.subs(p, pixel[3])-wave[3]]

awnser = sympy.nonlinsolve(system_equations, [S, B, C, D])
print(awnser.args[0])
#%%
# print(time_to_pixel(3))
# print(awnser.args[0])
print(pixel_to_wave(time_to_pixel(6.59), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(5.75), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(3.46), awnser.args[0]))
print(pixel_to_wave(time_to_pixel(4.35), awnser.args[0]))

#%%
import matplotlib.pyplot as plt
import numpy as np

px = np.linspace(0, 3500, 10000)

lam = pixel_to_wave(px, awnser.args[0])

plt.plot(px, lam)
plt.xlabel("Pixel")
plt.ylabel("Wavelength (nm)")
plt.title("Calibration curve")