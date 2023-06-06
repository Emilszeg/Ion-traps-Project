#%%
from math import sin, cos, tan, pi, sqrt, atan,asin, radians, degrees

def formula(incomming_angle, order, lambdaa, a):
    return degrees(asin((order * lambdaa - a*sin(radians(incomming_angle)))/a))

a = 7.4982*10**(-7)
lambdaa = 600*10**(-9)
invoer = float(input("Incomming angle: "))
order = int(input("Order: "))
print(formula(invoer, order, lambdaa, a))
#%%
print(400*10**(-9)/(sin(radians(45)) - sin(radians(10))))

#%%
def length_first_order(incomming_angle, a, distance_screen):
    red_angle = -formula(incomming_angle, 1, 600*10**(-9), a)
    blue_angle = -formula(incomming_angle, 1, 380*10**(-9), a)
    return distance_screen * tan(radians(incomming_angle-red_angle)) - distance_screen * tan(radians(incomming_angle-blue_angle))

#%%
print(length_first_order(45, 7.4982*10**(-7), 0.111))