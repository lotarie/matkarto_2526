% Face 8 - Octahedron (Southern Hemisphere, 90 to 180 degrees)
% Draw graticule, gnomonic projection, oblique aspect

clc
clear

% Grid Limits
umin = -90 * pi / 180;
umax = 10 * pi / 180;
vmin = 260 * pi / 180; 
vmax = 370 * pi / 180; 

Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 1000;

% Center of the Face 
uk = -35.2644 * pi/180;
vk = 315 * pi/180;
proj = @gnom;

% Boundary Triangle
ub = [-90, 0, 0, -90] * pi/180;     
vb = [315, 270, 360, 315] * pi/180;   

% Load Continents
conts = {'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\afrika.txt',...
    'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\antarktida.txt',...
    'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\australie.txt',...
    'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\eurasie.txt',...
    'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\j_amerika.txt',...
    'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\s_amerika.txt'};

uv = [umin, umax, vmin, vmax];
steps = [Du, Dv, du, dv];

% Create the face
createGlobeFace(uv, steps, R, uk, vk, proj, conts, ub, vb)

hold on