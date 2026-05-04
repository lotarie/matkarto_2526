from math import *
from merc_pole_parallel import *


#Optimal Mercator projection

#GERMANY
#Points on the equator
u1_G = point_1_ger[1] * pi/180
v1_G = point_1_ger[0] * pi/180
u2_G = point_2_ger[1] * pi/180
v2_G = point_2_ger[0] * pi/180

#Northernmost point
u3_G = point_3_ger[0] * pi/180
v3_G = point_3_ger[1] * pi/180

#Southernmost point
u4_G = point_4_ger[0] * pi/180
v4_G = point_4_ger[1] * pi/180

#Pole
vk = v_n
uk = u_n

#Transformation to the oblique aspect
s1_G = asin(sin(u1_G) * sin(uk) + cos(u1_G) * cos(uk) * cos(vk-v1_G))
s2_G = asin(sin(u2_G) * sin(uk) + cos(u2_G) * cos(uk) * cos(vk-v2_G))
s3_G = asin(sin(u3_G) * sin(uk) + cos(u3_G) * cos(uk) * cos(vk-v3_G))
s4_G = asin(sin(u4_G) * sin(uk) + cos(u4_G) * cos(uk) * cos(vk-v4_G))


#True parallel
s0_G = calculate_standard_parallel(s_south)

#Scales
m1_G = cos(s0_G)/cos(s1_G)
m2_G = cos(s0_G)/cos(s2_G)
m3_G = cos(s0_G)/cos(s3_G)
m4_G = cos(s0_G)/cos(s4_G)

#Distortions
ny1_G = (m1_G -1) *1000
ny2_G = (m2_G -1) *1000
ny3_G = (m3_G -1) *1000
ny4_G = (m4_G -1) *1000

print("Distortions for Germany:")
print(round(ny1_G, 6), round(ny2_G, 6), round(ny3_G, 6), round(ny4_G, 6))


#JAPAN
#Points on the equator
u1_J = point_1_jap[1] * pi/180
v1_J = point_1_jap[0] * pi/180
u2_J = point_2_jap[1] * pi/180
v2_J = point_2_jap[0] * pi/180

#northernmost point
u3_J = point_3_jap[0] * pi/180
v3_J = point_3_jap[1] * pi/180

#southernmost point
u4_J = point_4_jap[0] * pi/180
v4_J = point_4_jap[1] * pi/180

#Pole
uk_J = u_j
vk_J = v_j

#Transformation to the oblique aspect
s1_J = asin(sin(u1_J) * sin(uk_J) + cos(u1_J) * cos(uk_J) * cos(vk_J-v1_J))
s2_J = asin(sin(u2_J) * sin(uk_J) + cos(u2_J) * cos(uk_J) * cos(vk_J-v2_J))
s3_J = asin(sin(u3_J) * sin(uk_J) + cos(u3_J) * cos(uk_J) * cos(vk_J-v3_J))
s4_J = asin(sin(u4_J) * sin(uk_J) + cos(u4_J) * cos(uk_J) * cos(vk_J-v4_J))

#True parallel
s0_J = calculate_standard_parallel(s_j_north)

#Scales
m1_J = cos(s0_J)/cos(s1_J)
m2_J = cos(s0_J)/cos(s2_J)
m3_J = cos(s0_J)/cos(s3_J)
m4_J = cos(s0_J)/cos(s4_J)

#Distortions
ny1_J = (m1_J -1) *1000
ny2_J = (m2_J -1) *1000
ny3_J = (m3_J -1) *1000
ny4_J = (m4_J -1) *1000

print("Distortions for Japan:")

print(round(ny1_J, 6), round(ny2_J, 6), round(ny3_J, 6), round(ny4_J, 6))