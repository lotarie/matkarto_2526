from pyproj import Proj
import math

#define projection parameters for gnomonic projection
p = Proj(proj='gnom', lat_0=35.2644, lon_0=45, R=6380000)  

#coordinates of point Q (replace with actual coordinates)
lon_Q = 45
lat_Q = 0

#factors of distortion at point Q
factors = p.get_factors(lon_Q, lat_Q)

# meridional_scale m_p
print(f"m_p: {factors.meridional_scale:.6f}")

#jako parallel_scale m_r
print(f"m_r: {factors.parallel_scale:.6f}")

#a, b / Tissot
print(f" a:   {factors.tissot_semimajor:.6f}")
print(f" b:   {factors.tissot_semiminor:.6f}")

#omega 
print(f"omega': {factors.meridian_parallel_angle:.6f}°")

#dDelta omega - max angular distortion
print(f"delta omega: {factors.angular_distortion:.6f}°")

#P
print(f"P: {factors.areal_scale:.6f}")

#meridian convergence 
print(f"meridian convergence: {factors.meridian_convergence:.6f}°")