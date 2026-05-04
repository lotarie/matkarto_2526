import shapefile
from math import *
from numpy import *


def geographic_to_cartesian(lon, lat):
    #Convert degrees to radians
    lon_rad = radians(lon)
    lat_rad = radians(lat)
    
    #3D Cartesian conversion on a unit sphere (Radius = 1)
    X = cos(lat_rad) * cos(lon_rad)
    Y = cos(lat_rad) * sin(lon_rad)
    Z = sin(lat_rad)
    
    return X, Y, Z

def find_longest_axis(shapefile_path):
    all_points = []
    
    #Extract all points from the shapefile
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            #shape.points are returned as (x, y) which is (longitude, latitude)
            all_points.extend(shape_record.shape.points)
            
    #Remove duplicate points to speed up the calculation
    unique_points = list(set(all_points))
    
    cartesian_points = [geographic_to_cartesian(lon, lat) for lon, lat in unique_points]
    
    max_dist_sq = -1
    p1 = None
    p2 = None
    
    
    
    #We compare every point against every other point
    for i in range(len(cartesian_points)):
        x1, y1, z1 = cartesian_points[i]
        
        #Start the inner loop at i+1 so we don't calculate the same pair twice
        for j in range(i + 1, len(cartesian_points)):
            x2, y2, z2 = cartesian_points[j]
            
            #Calculate the 3D Euclidean distance 
            dist_sq = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
            
            #Update maximum
            if dist_sq > max_dist_sq:
                max_dist_sq = dist_sq
                p1 = unique_points[i]
                p2 = unique_points[j]
                
    return p1, p2


def Find_Boundary_Points(shapefile_path, uk, vk):
    all_points = []
    
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            all_points.extend(shape_record.shape.points)
            
    unique_points = list(set(all_points))
 
    
    s_max_positive = 0
    s_max_negative = 0
    p3 = None
    p4 = None
    
    for i in range(len(unique_points)):
        lon, lat = unique_points[i]
        
        u = radians(lat)
        v = radians(lon)
        
        #Calculate cartographic latitude 
        s = asin(sin(u)*sin(uk) + cos(u)*cos(uk)*cos(v-vk))
        
        #Track the northernmost cartographic boundary
        if s > s_max_positive:
            s_max_positive = s
            # Storing as (u, v) for your merc.py script
            p3 = (lat, lon) 
            
        # Track the southernmost cartographic boundary
        elif s < s_max_negative:
            s_max_negative = s
            p4 = (lat, lon) 
            
    return p3, p4, s_max_positive, s_max_negative


def calculate_standard_parallel(s_max_rad):
    #Apply Equation
    numerator = 2 * cos(s_max_rad)
    denominator = 1 + cos(s_max_rad)
    
    cos_s0 = numerator / denominator
    
    s0_rad = acos(cos_s0)
    
    return s0_rad
       
     

#Execution
point_1_ger, point_2_ger = find_longest_axis('shp\\nemecko.shp')

point_1_jap, point_2_jap = find_longest_axis('shp\\japonsko.shp')



#conversion uv, to x,y,z
#Germany
XN1, YN1, ZN1 = geographic_to_cartesian(point_1_ger[0], point_1_ger[1])
XN2, YN2, ZN2 = geographic_to_cartesian(point_2_ger[0], point_2_ger[1])

#Japan
XJ1, YJ1, ZJ1 = geographic_to_cartesian(point_1_jap[0], point_1_jap[1])
XJ2, YJ2, ZJ2 = geographic_to_cartesian(point_2_jap[0], point_2_jap[1])


#calculate cross product
N_G = cross([XN2-XN1, YN2-YN1, ZN2-ZN1], [XN1, YN1, ZN1])
N_J = cross([XJ2-XJ1, YJ2-YJ1, ZJ2-ZJ1], [XJ1, YJ1, ZJ1])

#normalize N
n_G = N_G/linalg.norm(N_G)
n_J = N_J/linalg.norm(N_J)

#convert back to uv
u_n = asin(n_G[2]) 
v_n = atan2(n_G[1], n_G[0]) 

u_j = asin(n_J[2]) 
v_j = atan2(n_J[1], n_J[0]) 

print("Germany")
point_3_ger, point_4_ger, s_north, s_south = Find_Boundary_Points('shp\\nemecko.shp', u_n, v_n)
print(u_n *180/pi, v_n *180/pi)
print(f"P1 (u1, v1): {point_1_ger[1]}, {point_1_ger[0]}")
print(f"P2 (u2, v2): {point_2_ger[1]}, {point_2_ger[0]}")
print(f"P3 (u3, v3): {point_3_ger[0]}, {point_3_ger[1]}")
print(f"P4 (u4, v4): {point_4_ger[0]}, {point_4_ger[1]}")

print(40*"-")

print("Japan")
point_3_jap, point_4_jap, s_j_north, s_j_south = Find_Boundary_Points('shp\\japonsko.shp', u_j, v_j)
print(u_j*180/pi, v_j*180/pi)
print(f"P1 (u1, v1): {point_1_jap[1]}, {point_1_jap[0]}")
print(f"P2 (u2, v2): {point_2_jap[1]}, {point_2_jap[0]}")
print(f"P3 (u3, v3): {point_3_jap[0]}, {point_3_jap[1]}")
print(f"P4 (u4, v4): {point_4_jap[0]}, {point_4_jap[1]}")


