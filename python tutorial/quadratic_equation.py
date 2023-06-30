# Solve the quadratic equation ax**2 + bx + c = 0
import math

a = 6
b = -7
c = -3

# calculate the discriminant
d = (b**2) - (4*a*c)

if d>0 or d==0:
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
else:
    print("Invalid Number")