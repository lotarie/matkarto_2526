
import numpy as np
from pyproj import *
from matplotlib.pyplot import *



def project(proj_name, R_z, lat, lon, lat0, lon0):
    # Create new projection given by proj_name
    my_proj =  Proj(proj=proj_name, R=R_z, lat_1 = lat0, lon_0 = lon0)

    # Project point calculation
    [X,Y] = my_proj(lon, lat)

    #Distortions
    dist = my_proj.get_factors(lon, lat)
    a = dist.tissot_semimajor
    b = dist.tissot_semiminor

    return X, Y, a, b 

def graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name):
    #Create graticule of the given map projection
    #Create meridians
    lat_mer = np.arange(lat_min, lat_max + dlat/2, dlat)
    lon_mer = np.arange(lon_min, lon_max + Dlon/2, Dlon)
    
    #Create parallels
    lat_par = np.arange(lat_min, lat_max + Dlat/2, Dlat)
    lon_par = np.arange(lon_min, lon_max + dlon/2, dlon)

    #Create meshgrid
    lat_merg, lon_merg = np.meshgrid(lat_mer, lon_mer)
    lon_parg, lat_parg = np.meshgrid(lon_par, lat_par)
    
    #Project meridians
    mer_proj = project(proj_name, R, lat_merg, lon_merg, lat0, lon0)

    #Project parallels
    par_proj = project(proj_name, R, lat_parg, lon_parg, lat0, lon0)
    
    return mer_proj, par_proj   

#Define projection
#proj_name = "sinu"
#proj_name = "bonne"
#proj_name = "eck5"
#proj_name = "wintri"
proj_name = "aitoff"

R = 6380000
lat0 = 55
lon0 = 90


#Define projection grid
lat_min = 35
lat_max = 85
lon_min = 0
lon_max = 200
Dlat = 10
Dlon = 10
dlat = 0.1 * Dlat
dlon = 0.1 * Dlon
nlat = 100
nlon = 100

#Create intervals
lat = np.linspace(lat_min, lat_max, nlat)
lon = np.linspace(lon_min, lon_max, nlon)

#Create  meshgrid
latg, long = np.meshgrid(lat, lon)

#Project meshgrid
X, Y, a, b = project(proj_name, R, latg, long, lat0, lon0)

#Airy local
h2_a = 0.5*((a-1)**2+(b-1)**2)

#Complex local
h2_c = 0.5*(abs(a-1)+abs(b-1)) + a/b - 1

#Airy global
H2_a = np.mean(h2_a)

#Complex global
H2_c = np.mean(h2_c)

#Airy weighted global
w = np.cos(latg * np.pi /180)
H2_aw = np.sum(w*h2_a)/ np.sum(w)

#Complex weighted global
H2_cw = np.sum(w*h2_c)/ np.sum(w) 


print("airy global", H2_a)
print("airy weighted", H2_aw)
print("complex global", H2_c)
print("complex weighted", H2_cw)


# Load continents
continents = np.loadtxt("warsaw_pact_points.txt", encoding='utf-8-sig')


#Calculate the distance between every consecutive point
distances = np.sqrt(np.sum(np.diff(continents, axis=0)**2, axis=1))

#Find where the distance jumps by an unnaturally large amount (e.g., > 2 degrees)
jump_indices = np.where(distances > 2.0)[0] + 1

#Insert NaN values at those jump locations to "lift the pen"
continents = np.insert(continents, jump_indices, np.nan, axis=0)

# Extract coordinates
latc = continents[:, 0]
lonc = continents[:, 1]

# Project points
Xc, Yc, ac, bc = project(proj_name, R, latc, lonc, lat0, lon0)


#Create meridians and parallels
mer_proj, par_proj = graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name)

#Extract coordinates
Xm = mer_proj[0]
Ym = mer_proj[1]

Xp = par_proj[0]
Yp = par_proj[1]

#PLot meridians and parallels
plot(np.transpose(Xm), np.transpose(Ym), color = 'black', linewidth = 0.5)
plot(np.transpose(Xp), np.transpose(Yp), color = 'black', linewidth = 0.5)

#Variable map scale
S = 100000000
Sv = S/a

#Create contour lines
dS = np.arange(20000000, 200000000, 10000000)
contours = contour(X, Y, Sv, levels = dS, colors = 'red', linewidths = 0.5)

#Create contour labels
clabel(contours, inline_spacing = -20)
plot(Xc, Yc, linewidth=1.5, color='blue')

show()





#How to compute the change in M was discussed with AI.
#Implementation was done by me, but the logic was based on the discussion with AI.

#Calculate the percentage of the area where the change in M is less than 50%
#M is the map scale factor, which is given by M = 1/a. 
#We want to find the percentage of the area where the change in M is less than 50%, which means we want to find the area where |1/a - 1| < 0.5.

#We will use the weights w to calculate the weighted percentage of the area where the change in M is less than 50%. 
#The total area weight is the sum of all weights, and the valid M weights are the weights where the change in M is less than 50%. 
#The percentage is then calculated as the sum of valid M weights divided by the total area weight, multiplied by 100 to get a percentage.
total_area_weight = np.sum(w)

#Calculate the change in M
change_M = np.abs(1/a - 1)

valid_M_weights = w[change_M < 0.5]
percent_M = (np.sum(valid_M_weights) / total_area_weight) * 100

print(f"Change: M < 50 %: {percent_M:.2f} %")
