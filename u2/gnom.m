function [x, y] = gnom(R, s, d)
    %Gnomonic projection in oblique aspect
    x = R * tan(pi/2-s).*cos(d);
    y = R * tan(pi/2-s).*sin(d);
end

