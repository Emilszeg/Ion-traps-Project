from math import sin, cos, tan, pi, sqrt, atan,asin

def formula(incomming_angle, order, lambdaa, a):
    return asin(order * lambdaa / (a*sin(incomming_angle)))

a = 1000
lambdaa = 0.0000005
invoer = float(input("Incomming angle: "))
order = int(input("Order: "))
print(formula(invoer, order, lambdaa, a))