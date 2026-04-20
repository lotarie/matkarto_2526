% Face 1 - Tetrahedron
% Draw graticule, gnomonic projection, oblique aspect

%Grid Limits 
umin = -40 * pi / 180;
umax = 90 * pi / 180;
vmin = -20 * pi / 180;
vmax = 130 * pi / 180;

Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 1000;

%Center of the Face
uk = 19.4712 * pi/180;
vk = 60 * pi/180;
proj = @gnom;

%Boundary Triangle
uj = -19.4712 * pi/180;
ub = [90 * pi/180, uj, uj, 90 * pi/180];
vb = [60 * pi/180, 0, 120 * pi/180, 60 * pi/180];

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

