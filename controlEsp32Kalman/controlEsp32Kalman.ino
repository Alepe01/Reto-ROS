% close all
% clear
% clc
% 
% iter = 10;
% Xk = 0;
% 
% for k = 1: iter
%     Xk = Xk - (3 + (Xk - 2)^3)/(3 * (Xk - 2)^2); 
% 
% end
% 
% fprintf("Xk = %f \n",Xk)
% 
% figure(1)
% x = 0:0.001:1;
% y = 3 + (x - 2).^3;
% plot(x,y)
% hold on
% grid on
% plot(Xk, 3 + (Xk - 2)^3,"or")
% 
% 
clc; 
clear; 
close all;

% Problema 2
syms q1 q2

%fq = [cos(q1) + cos(q1 + q2);sin(q1) + sin(q1 + q2)]
% j = jacobian(fq,[q1, q2])

iter_max = 100;
epsilon = 1e-3;
Xd = [1.2; 1.2];
qk = [1; -1];

for k = 1:iter_max
    q1 = qk(1,1); q2 = qk(2,1);
    J = [- sin(q1 + q2) - sin(q1), -sin(q1 + q2);...
        cos(q1 + q2) + cos(q1),  cos(q1 + q2)];
    fq = [cos(q1 + q2) + cos(q1);...
         sin(q1 + q2) + sin(q1)];
    qk = qk + inv(J)*(Xd - fq);
    e = (Xd - fq);
    if abs(e) < epsilon
        break
    end
end

fprintf("q1 = %f \n",qk(1,1))
fprintf("q2 = %f \n",qk(2,1))
