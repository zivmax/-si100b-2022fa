function Hd = fir500
%FIR500 返回离散时间滤波器对象。

% MATLAB Code
% Generated by MATLAB(R) 9.12 and DSP System Toolbox 9.14.
% Generated on: 27-Nov-2022 20:58:49

% Equiripple Bandpass filter designed using the FIRPM function.

% All frequency values are in Hz.
Fs = 8192;  % Sampling Frequency

Fstop1 = 250;             % First Stopband Frequency
Fpass1 = 260;             % First Passband Frequency
Fpass2 = 500;             % Second Passband Frequency
Fstop2 = 510;             % Second Stopband Frequency
Dstop1 = 1e-05;           % First Stopband Attenuation
Dpass  = 0.057501127785;  % Passband Ripple
Dstop2 = 1e-05;           % Second Stopband Attenuation
dens   = 20;              % Density Factor

% Calculate the order from the parameters using FIRPMORD.
[N, Fo, Ao, W] = firpmord([Fstop1 Fpass1 Fpass2 Fstop2]/(Fs/2), [0 1 ...
                          0], [Dstop1 Dpass Dstop2]);

% Calculate the coefficients using the FIRPM function.
b  = firpm(N, Fo, Ao, W, {dens});
Hd = dfilt.dffir(b);

% [EOF]
