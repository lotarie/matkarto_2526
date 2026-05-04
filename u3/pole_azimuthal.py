from math import *
import shapefile


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


#Find the center of a circle defined by 2 points
def circle_from_2_points(p1, p2):
    
    center_lon = (p1[0] + p2[0]) / 2
    center_lat = (p1[1] + p2[1]) / 2
    
    #compute radius using pythagorean theorem
    radius  = hypot(p2[0] - p1[0], p2[1] - p1[1]) / 2
    return (center_lon, center_lat), radius

#Find the center of a circle defined by 3 points
def circle_from_3_points(p1, p2, p3):
    #compute temporary values
    temp = p2[0]*p2[0] + p2[1]*p2[1]
    bc = (p1[0]*p1[0] + p1[1]*p1[1] - temp) / 2
    cd = (temp - p3[0]*p3[0] - p3[1]*p3[1]) / 2
    
    det = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])
    
    #If the determinant is close to zero, the points are collinear and we cannot define a unique circle
    if abs(det) < 1e-6:
        return None, float('inf') 
      
    #Calculate center coordinates    
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / det
    cy = ((p1[0] - p2[0])*cd - (p2[0] - p3[0])*bc) / det
    
    #compute radius using pythagorean theorem
    radius = hypot(p2[0] - cx, p2[1] - cy)
    
    return (cx, cy), radius

#Check if a circle contains all boundary points
def is_valid_circle(center, radius, points):
    for p in points:
        #If any point is further from the center than the radius, it's invalid circle
        #We add 1e-5 to account for tiny floating point rounding errors
        if hypot(p[0] - center[0], p[1] - center[1]) > radius + 1e-5:
            return False
    return True

def find_minimum_enclosing_circle(shapefile_path):
    all_points = []
    
    #Extract all points
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            all_points.extend(shape_record.shape.points)
            
    #Find the Convex Hull 
    boundary_points = createCH(all_points)
    
    min_radius = float('inf')
    best_center = None
    
    #Test all 2-point combinations on the boundary
    for i in range(len(boundary_points)):
        for j in range(i + 1, len(boundary_points)):
            center, radius = circle_from_2_points(boundary_points[i], boundary_points[j])
            
            if radius < min_radius and is_valid_circle(center, radius, boundary_points):
                min_radius = radius
                best_center = center
                
    #Test all 3-point combinations on the boundary
    for i in range(len(boundary_points)):
        for j in range(i + 1, len(boundary_points)):
            for k in range(j + 1, len(boundary_points)):
                center, radius = circle_from_3_points(boundary_points[i], boundary_points[j], boundary_points[k])
                
                if center and radius < min_radius and is_valid_circle(center, radius, boundary_points):
                    min_radius = radius
                    best_center = center
                    
    return best_center, min_radius

def get_azimuthal_boundary_point(shapefile_path, uk_deg, vk_deg):
    all_points = []
    
    with shapefile.Reader(shapefile_path) as shp:
        for shape_record in shp.shapeRecords():
            if not shape_record.shape.points:
                continue
            all_points.extend(shape_record.shape.points)
            
    unique_points = list(set(all_points))
    
    uk = radians(uk_deg)
    vk = radians(vk_deg)
    
    #We are looking for the minimum 's'
    min_s = float('inf')
    p1 = None
    
    for lon, lat in unique_points:
        u = radians(lat)
        v = radians(lon)
        
        #Calculate cartographic latitude relative to the new pole
        s = asin(sin(u)*sin(uk) + cos(u)*cos(uk)*cos(v-vk))
        
        #The furthest point has the SMALLEST cartographic latitude
        if s < min_s:
            min_s = s
            p1 = (lat, lon) 
            
    return p1

#Execution
pole_coords_G, circle_radius_G = find_minimum_enclosing_circle('shp\\nemecko.shp')
print(f"Cartographic Pole - Germany (u_k, v_k):  {pole_coords_G[1]},  {pole_coords_G[0]}")
pole_coords_J, circle_radius_J = find_minimum_enclosing_circle('shp\\japonsko.shp')
print(f"Cartographic Pole - Japan (u_k, v_k): {pole_coords_J[1]},  {pole_coords_J[0]}")


P1_G = get_azimuthal_boundary_point('shp\\nemecko.shp', pole_coords_G[1], pole_coords_G[0])
print(f"Azimuthal Boundary Point - Germany: Lon {P1_G[1]}, Lat {P1_G[0]}")

P1_J = get_azimuthal_boundary_point('shp\\japonsko.shp', pole_coords_J[1], pole_coords_J[0])
print(f"Azimuthal Boundary Point - Japan: Lon {P1_J[1]}, Lat {P1_J[0]}")