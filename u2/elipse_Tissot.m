function [xt, yt] = elipse_Tissot(a, b, dt, xs, ys, fi)
    %Create ellipse at [0,0]
    [xe, ye] = ellipse(a, b, dt); 
    %Rotate ellipse by fi
    [xer,yer] = rotate(xe,ye,fi); 
    %Shift ellipse
    xt = xer + xs;
    yt = yer + ys; 
end

function [xe, ye] = ellipse(a, b, dt)
    %Create ellipse
    t = 0:dt:2*pi;
    xe = a*cos(t);  
    ye = b*sin(t); 
end

function [xer,yer] = rotate(xe,ye,fi)
    %Rotate points
    xer = cos(fi)*xe - sin(fi)*ye; 
    yer = sin(fi)*xe + cos(fi)*ye;  
end