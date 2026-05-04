import shapefile
from math import *
import numpy as np

def geographic_to_cartesian(lon, lat):
    lon_rad = radians(lon)
    lat_rad = radians(lat)
    X = cos(lat_rad) * cos(lon_rad)
    Y = cos(lat_rad) * sin(lon_rad)
    Z = sin(lat_rad)
    return X, Y, Z

def get2VectorsAngle(p_center, p_ref, p_target):
    """
    Calculates the angle between two vectors sharing a center point.
    Returns the angle in radians from 0 to 2*PI.
    """
    # Vector 1 (Reference vector: pj to pj1)
    v1_x = p_ref[0] - p_center[0]
    v1_y = p_ref[1] - p_center[1]
    
    # Vector 2 (Target vector: pj to pol[i])
    v2_x = p_target[0] - p_center[0]
    v2_y = p_target[1] - p_center[1]
    
    # Calculate absolute angles using atan2
    angle1 = atan2(v1_y, v1_x)
    angle2 = atan2(v2_y, v2_x)
    
    # Get the difference
    omega = angle2 - angle1
    
    # Normalize to strictly positive (0 to 2*PI)
    if omega < 0:
        omega += 2 * pi
        
    return omega

def createCH(points):
    # Convert input to a list of unique tuples 
    pol = list(set(points))
    ch = []
    
    # Find pivot q (minimize y) -> k[1] is the y-coordinate
    q = min(pol, key=lambda k: k[1])

    # Find left-most point (minimize x) -> k[0] is the x-coordinate
    s = min(pol, key=lambda k: k[0])
    
    # Initial segment
    pj = q
    pj1 = (s[0], q[1]) 
    
    # Add to CH
    ch.append(pj)
    
    # Find all points of CH
    while True:
        omega_max = -1
        index_max = -1
        
        # Browse all points
        for i in range(len(pol)):
            # Different points
            if pj != pol[i]:
                # Compute omega
                omega = get2VectorsAngle(pj, pj1, pol[i])
        
                # Actualize maximum
                if omega > omega_max:
                    omega_max = omega
                    index_max = i
                
        # Add point to the convex hull
        next_point = pol[index_max]
        ch.append(next_point)
        
        # Reassign points
        pj1 = pj
        pj = next_point
        
        # Stopping condition
        if pj == q:
            # Remove the last point because it duplicates the first one (q)
            ch.pop() 
            break
        
    return ch

def find_conic_pole(shapefile_path):
    all_points = []
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            all_points.extend(shape_record.shape.points)
            
    #Get the boundary points using your Convex Hull
    boundary_points = createCH(all_points)
    
    #Pick 3 points spread across the boundary
    p1_geo = boundary_points[0]
    p2_geo = boundary_points[len(boundary_points) // 3]
    p3_geo = boundary_points[(2 * len(boundary_points)) // 3]

    #Convert to 3D Cartesian
    X1, Y1, Z1 = geographic_to_cartesian(p1_geo[0], p1_geo[1])
    X2, Y2, Z2 = geographic_to_cartesian(p2_geo[0], p2_geo[1])
    X3, Y3, Z3 = geographic_to_cartesian(p3_geo[0], p3_geo[1])

    #Create vectors and Cross Product
    V1 = [X2 - X1, Y2 - Y1, Z2 - Z1]
    V2 = [X3 - X1, Y3 - Y1, Z3 - Z1]
    N = np.cross(V1, V2)

    #If the pole is pointing opposite to the country, flip it 180 degrees
    if np.dot(N, [X1, Y1, Z1]) < 0:
        N = -N
        
    #Normalize and convert back to geographic
    n = N / np.linalg.norm(N)
    uk_deg = asin(n[2]) * 180/pi
    vk_deg = atan2(n[1], n[0]) * 180/pi
    
    return vk_deg, uk_deg



def get_conic_boundary_points(shapefile_path, uk_deg, vk_deg):
    all_points = []
    
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            all_points.extend(shape_record.shape.points)
            
    unique_points = list(set(all_points))
    
    uk = radians(uk_deg)
    vk = radians(vk_deg)
    
    max_s = -float('inf')
    min_s = float('inf')
    p_north = None
    p_south = None
    
    for lon, lat in unique_points:
        u = radians(lat)
        v = radians(lon)
        
        # Calculate cartographic latitude
        s = asin(sin(u)*sin(uk) + cos(u)*cos(uk)*cos(v-vk))
        
        # Track Northernmost (maximum s)
        if s > max_s:
            max_s = s
            p_north = (lat, lon) # Storing as (u, v)
            
        # Track Southernmost (minimum s)
        if s < min_s:
            min_s = s
            p_south = (lat, lon) # Storing as (u, v)
            
    return p_north, p_south

#Execution
vk_ger, uk_ger = find_conic_pole('shp\\nemecko.shp')
print(f"Germany Conic Pole (uk, vk): {uk_ger}, {vk_ger}")

vk_jap, uk_jap = find_conic_pole('shp\\japonsko.shp')
print(f"Japan Conic Pole (uk, vk): {uk_jap}, {vk_jap}")

NP_GER, SP_GER = get_conic_boundary_points('shp\\nemecko.shp', uk_ger, vk_ger)
print(f"Germany Points (u,v): {NP_GER[0], NP_GER[1]}, {SP_GER[0], SP_GER[1]}")

NP_JAP, SP_JAP = get_conic_boundary_points('shp\\japonsko.shp', uk_jap, vk_jap)
print(f"Japan Points (u,v): {NP_JAP[0], NP_JAP[1]}, {SP_JAP[0], SP_JAP[1]}")
