from math import *
from pole_azimuthal import *


R = 1
#Stereographic projection
#GERMANY
#Pole
uk_G = pole_coords_G[1] * pi/180 
vk_G = pole_coords_G[0] * pi/180

#Southern-most point
u1_G = P1_G[0] * pi/180
v1_G = P1_G[1] * pi/180

# Convert to oblique aspect
s1_G = asin(sin(u1_G) * sin(uk_G) + cos(u1_G) * cos(uk_G) * cos(v1_G-vk_G))

#Substitution
psi1_G = pi/2 - s1_G

#Compute mi
mi_G = (2*cos(psi1_G/2)**2)/(1+(cos(psi1_G/2))**2)

#Psi0
psi0_G = 2*acos(sqrt(mi_G))
s0_G = pi/2 - psi0_G

#Local linear scales
m1_G = mi_G/(cos(psi1_G/2)**2)
m2_G = mi_G/(cos(0)**2)
m0_G = mi_G/(cos(psi0_G/2)**2)


#Distortions
ny1_G = (m1_G -1) * 1000
ny2_G = (m2_G -1) * 1000
ny0_G = (m0_G - 1) * 1000

print("Distortions for Germany:")
print(round(ny1_G, 6), round(ny2_G, 6), round(ny0_G))


#JAPAN
#Pole
uk_J = pole_coords_J[1] * pi/180
vk_J = pole_coords_J[0] * pi/180

#Southern-most point
u1_J = P1_J[0] * pi/180
v1_J = P1_J[1] * pi/180

# Convert to oblique aspect
s1_J = asin(sin(u1_J) * sin(uk_J) + cos(u1_J) * cos(uk_J) * cos(v1_J-vk_J))

#Substitution
psi1_J = pi/2 - s1_J

#Compute mi
mi_J = (2*cos(psi1_J/2)**2)/(1+(cos(psi1_J/2))**2)

#Psi0
psi0_J = 2*acos(sqrt(mi_J))
s0_J = pi/2 - psi0_J

#Local linear scales
m1_J = mi_J/(cos(psi1_J/2)**2)
m2_J = mi_J/(cos(0)**2)
m0_J = mi_J/(cos(psi0_J/2)**2)

#Distortions
ny1_J = (m1_J -1) * 1000
ny2_J = (m2_J -1) * 1000
ny0_J = (m0_J - 1) * 1000

print("Distortions for Japan:")
print(round(ny1_J, 6), round(ny2_J, 6), round(ny0_J, 6))