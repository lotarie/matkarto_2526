from math import *
from pole_conic import *

# Optimal LCC projection
R = 1

#GERMANY
#Pole
uk_G =  uk_ger * pi/180
vk_G = vk_ger * pi/180 

#Northernmost point
u1_G = NP_GER[0] *pi/180
v1_G = NP_GER[1] *pi/180

#Southernmost point
u2_G = SP_GER[0] *pi/180
v2_G = SP_GER[1] *pi/180

#Transformation to the oblique aspect
s1_G = asin(sin(u1_G) * sin(uk_G) + cos(u1_G) * cos(uk_G) * cos(vk_G-v1_G))
s2_G = asin(sin(u2_G) * sin(uk_G) + cos(u2_G) * cos(uk_G) * cos(vk_G-v2_G))

#Constant c of the conic projection
cn_G = log10(cos(s1_G)) - log10(cos(s2_G))
cd_G = log10(tan(s2_G/2+pi/4))-log10(tan(s1_G/2+pi/4))
c_G = cn_G / cd_G

#Compute s0
s0_G = asin(c_G)

#Compute rho0: radius of the parallel (u = u0)
rho0_n_G = 2*R*cos(s0_G)*cos(s1_G)*(tan(s1_G/2+pi/4))**c_G
rho0_d_G = c_G*(cos(s0_G)*(tan(s0_G/2+pi/4))**c_G+cos(s1_G)*(tan(s1_G/2+pi/4))**c_G)
rho0_G = rho0_n_G/rho0_d_G

#Compute rho1: radius of the north parallel (u = u1)
rho1_G = rho0_G*((tan(s0_G/2+pi/4))/(tan(s1_G/2+pi/4)))**c_G

#Compute rho2: radius of the south parallel (u = u2)
rho2_G = rho0_G*((tan(s0_G/2+pi/4))/(tan(s2_G/2+pi/4)))**c_G

#Scales
m1_G = (c_G * rho1_G)/(R * cos(s1_G))
m2_G = (c_G * rho2_G)/(R * cos(s2_G))
m0_G = (c_G * rho0_G)/(R * cos(s0_G))

ny1_G = (m1_G -1) * 1000
ny2_G = (m2_G -1) * 1000
ny0_G = (m0_G - 1) * 1000

print("Distortions for Germany")
print(ny1_G, ny2_G, ny0_G)


#JAPAN
#Pole
uk_J = uk_jap * pi/180
vk_J = vk_jap * pi/180 

#Northernmost point
u1_J = NP_JAP[0] *pi/180
v1_J = NP_JAP[1] *pi/180

#Southernmost point
u2_J = SP_JAP[0] *pi/180
v2_J = SP_JAP[1] *pi/180

#Transformation to the oblique aspect
s1_J = asin(sin(u1_J) * sin(uk_J) + cos(u1_J) * cos(uk_J) * cos(vk_J-v1_J))
s2_J = asin(sin(u2_J) * sin(uk_J) + cos(u2_J) * cos(uk_J) * cos(vk_J-v2_J))

#Constant c of the conic projection
cn_J = log10(cos(s1_J)) - log10(cos(s2_J))
cd_J = log10(tan(s2_J/2+pi/4))-log10(tan(s1_J/2+pi/4))
c_J = cn_J / cd_J

#Compute s0
s0_J = asin(c_J)

#Compute rho0: radius of the parallel (u = u0)
rho0_n_J = 2*R*cos(s0_J)*cos(s1_J)*(tan(s1_J/2+pi/4))**c_J
rho0_d_J = c_J*(cos(s0_J)*(tan(s0_J/2+pi/4))**c_J+cos(s1_J)*(tan(s1_J/2+pi/4))**c_J)
rho0_J = rho0_n_J/rho0_d_J

#Compute rho1: radius of the north parallel (u = u1)
rho1_J = rho0_J*((tan(s0_J/2+pi/4))/(tan(s1_J/2+pi/4)))**c_J

#Compute rho2: radius of the south parallel (u = u2)
rho2_J = rho0_J*((tan(s0_J/2+pi/4))/(tan(s2_J/2+pi/4)))**c_J

#Scales
m1_J = (c_J * rho1_J)/(R * cos(s1_J))
m2_J = (c_J * rho2_J)/(R * cos(s2_J))
m0_J = (c_J * rho0_J)/(R * cos(s0_J))

ny1_J = (m1_J -1) * 1000
ny2_J = (m2_J -1) * 1000
ny0_J = (m0_J - 1) * 1000

print("Distortions for Japan")
print(ny1_J, ny2_J, ny0_J)