%Face 5
%Draw graticule, gnomonic projection, normal aspect
umin = -70 * pi / 180;
umax = 70 * pi / 180;
vmin = 100 * pi / 180;
vmax = 290 * pi / 180;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 1000;
uk = 0;
vk = 225 * pi/180;
proj = @gnom 

conts = {'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\afrika.txt',...
'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\antarktida.txt',...
'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\australie.txt',...
'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\eurasie.txt',...
'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\j_amerika.txt',...
'C:\Users\kusak\OneDrive - Univerzita Karlova\Homework\VŠ\Matematická kartografie\u2 V2\u2\continents_points\s_amerika.txt'};

uv = [umin, umax, vmin, vmax];
steps = [Du, Dv, du, dv];
u = 35.2644 * pi/180;
ub = [-u, -u, u, u, -u];
vb = [180, 270, 270, 180, 180] * pi/180;
createGlobeFace(uv, steps, R, uk, vk, proj, conts, ub, vb)

hold on