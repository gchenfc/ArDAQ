%%  Gerry Chen
%   Reads the data output by the python program

%% load data
clear;
load data/data
% only get stabilized data
DC = data(:,8);
changeInds = find(diff(DC)~=0);
boxAvgSamps = 5;
indsToSave = changeInds;
for i=1:boxAvgSamps-1
    indsToSave = [indsToSave,changeInds-i];
end
% data = data(sort(indsToSave(:)),:);
for i = 2:size(indsToSave,1)
    tmpData(i,:) = mean(data(indsToSave(i,:),:),1);
end
data = tmpData;

% import variables
t   = data(:,1);
Vin = data(:,2);
Iin = data(:,3);
Win = data(:,4);
Vout= data(:,5);
Iout= data(:,6);
Wout= data(:,7);
DC  = data(:,8);
Ceff = data(:,9);
Temp = data(:,10);
H2 = data(:,size(data,2));%-.2*1000/60/.08235;
% offset data
stInd = 1;
H2(1:end-stInd+1) = H2(stInd:end);

%% calculations
H2energyDensity = 1.20E+05;
H2power = H2/1000/60*0.08235*H2energyDensity;
eff = Win./H2power;

%% plots
% figure(1);clf;
% plot(t,Vin,'k-',...
%      t,Vout,'r-')
% xlabel('time (s)');
% ylabel('Voltage (V)');
% title('Voltage');
% legend('FC in','SC out');
% 
% figure(2);clf;
% plot(t,Iin,'k-',...
%      t,Iout,'r-')
% xlabel('time (s)');
% ylabel('Current (A)');
% title('Current');
% legend('FC in','SC out');

figure(1);clf;
plot(Win,eff*100,'r*',...
    Win,eff*100,'b-');
xlabel('Power (W)');
ylabel('Efficiency (%)');
title('Efficiency vs. Power');
grid on
% print -depsc plots/effVsPower

figure(3);clf;
plot(t,Win,'k-',...
     t,Wout,'r-')
xlabel('time (s)');
ylabel('power (W)');
title('Power');
legend('FC in','SC out');
% print -depsc plots/powerVsTime

figure(4);clf;
plot(t,H2,'-');
xlabel('time (s)');
ylabel('H2');
title('H2 consumption');
% print -depsc plots/H2vsTime
% 
figure(5);clf;
plot(Iin,Vin)
title('V vs I');
xlabel('I (A)');
ylabel('V (V)');
grid on;
print -depsc plots/VvsI_bubbler

figure(6);clf;
plot(t,Win);
hold on
plot(t,DC*700);
yyaxis right
plot(t,H2);
% print -depsc plots/AllvsTime