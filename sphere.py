# Nicolas Tracewell
# ntracewe@ucsc.edu
# programming assignment 1
# This program computes the volume and surface area of a sphere when the radius is input.

import math
r = float(input("Enter the radius of the sphere: "))
p = math.pi
area = 4*p*r**2
volume = (4/3)*p*r**3
print("Surface Area: ", area)
print("Volume: ", volume)