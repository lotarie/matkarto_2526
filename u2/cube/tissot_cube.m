

umin = 30 * pi / 180;
umax = 90 * pi / 180;
vmin = -180 * pi / 180;
vmax = 180 * pi / 180;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
R = 6380 * 1000;
uk = 90*pi/180;
vk = 0;
proj = @gnom 


[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, proj);

%Draw meridians and parallels
hold on;
axis equal;
plot(XM', YM', 'k');
plot(XP', YP', 'k');


%draw tissot
%Local latitude of the edge 
un_local = 35.2644 * pi/180; 
vn_local = 0;

%Get the projected coordinates
[xs, ys] = gnom(R, un_local, vn_local);

%Calculate distortion scale factors (a and b)
c = pi/2 - un_local;
a = 1 / (cos(c)^2);  
b = 1 / cos(c);     


visual_radius = R / 12; 
a_vis = a * visual_radius;
b_vis = b * visual_radius;

%Draw the ellipse
dt = 0.05;
fi = 0; 

[xt, yt] = elipse_Tissot(a_vis, b_vis, dt, xs, ys, fi);
plot(xt, yt, 'r', 'LineWidth', 1.5); 