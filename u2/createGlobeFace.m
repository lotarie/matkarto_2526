function [] = createGlobeFace(uv, steps, R, uk, vk, proj, conts, ub, vb)
% Create graticule
umin = uv(1,1);
umax = uv(1,2);
vmin = uv(1,3);
vmax = uv(1,4);

Du = steps(1,1);
Dv = steps(1,2);
du = steps(1,3);
dv = steps(1,4);

vb1 = vb(1,1);
vb2 = vb(1,2);
vb3 = vb(1,3);
vb4 = vb(1,4);


[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, proj);

%Draw meridians and parallels
hold on;
axis equal;
plot(XM', YM', 'k');
plot(XP', YP', 'k');

%Draw continents
for i=1: length(conts)
    [XC, YC] = drawContinent(conts{i}, R, uk, vk, proj);
    plot (XC, YC, 'r', 'LineWidth', 1);
end

%Draw cutting lines
[XB,YB] = boundary(R, uk, vk, proj, ub, vb);
plot (XB, YB, 'b', 'LineWidth', 1);

end