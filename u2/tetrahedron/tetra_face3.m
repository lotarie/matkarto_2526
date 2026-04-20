% Face3 - Tetrahedron 
% Draw graticule, gnomonic projection, oblique aspect

%Grid Limits 
umin = -40 * pi / 180;
umax = 90 * pi / 180;
vmin = 220 * pi / 180;
vmax = 380 * pi / 180;

Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 1000;

%Center of the Face
uk = 19.4712 * pi/180;
vk = 300 * pi/180;
proj = @gnom;

uj = -19.4712 * pi/180;
ub = [90 * pi/180, uj, uj, 90 * pi/180];
vb = [300 * pi/180, 240 * pi/180, 360 * pi/180, 300 * pi/180];

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

