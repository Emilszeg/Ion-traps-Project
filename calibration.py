#%%
import sympy

l, p, S, B, C, D = sympy.symbols('l p S B C D')
equ = S + p * B + p**2 * C + p**3 * D
print(equ.subs(p, 1736.72))
print(equ.subs(p, 2756.45))
print(equ.subs(p, 2968.9))
print(equ.subs(p, 2198.79))
print(equ.subs([(B, 0.386976930), (C, -0.0001347436658), (D, 1.766982496*10**-8), (S, 227.0331396)]))

#%%
def pixel_to_wave(pixel):
    return 1.766982496e-8*pixel**3 - 0.0001347436658*pixel**2 + 0.38697693*pixel + 227.0331396

def time_to_pixel(time):
    return 531.1077 * time

print(pixel_to_wave(time_to_pixel(6.40)))