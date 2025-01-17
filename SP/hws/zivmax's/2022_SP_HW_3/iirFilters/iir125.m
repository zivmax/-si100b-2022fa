function Hd = iir125
%IIR125 返回离散时间滤波器对象。

% MATLAB Code
% Generated by MATLAB(R) 9.12 and Signal Processing Toolbox 9.0.
% Generated on: 28-Nov-2022 12:02:02

% Butterworth Bandpass filter designed using FDESIGN.BANDPASS.

% All frequency values are in Hz.
Fs = 8192;  % Sampling Frequency

Fstop1 = 65;          % First Stopband Frequency
Fpass1 = 75;          % First Passband Frequency
Fpass2 = 125;         % Second Passband Frequency
Fstop2 = 135;         % Second Stopband Frequency
Astop1 = 60;          % First Stopband Attenuation (dB)
Apass  = 1;           % Passband Ripple (dB)
Astop2 = 80;          % Second Stopband Attenuation (dB)
match  = 'stopband';  % Band to match exactly

% Construct an FDESIGN object and call its BUTTER method.
h  = fdesign.bandpass(Fstop1, Fpass1, Fpass2, Fstop2, Astop1, Apass, ...
                      Astop2, Fs);
Hd = design(h, 'butter', 'MatchExactly', match);

% [EOF]
