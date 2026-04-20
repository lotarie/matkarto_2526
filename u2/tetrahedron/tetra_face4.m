% Face 4 - Tetrahedron 
% Draw graticule, gnomonic projection, oblique aspect

%Grid Limits
umin = -90 * pi / 180;
umax = -10 * pi / 180;
vmin = -180 * pi / 180;
vmax = 180 * pi / 180;

Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 100;

%Center of the Face 
uk = -90*pi/180;
vk = 0;
proj = @gnom;

uj = -19.4712 * pi/180;
ub = [uj, uj, uj, uj];
vb = [0, 120 * pi/180, 240 * pi/180, 0];

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

