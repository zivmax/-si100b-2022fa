clear

[speech, Fs] = audioread("speech.wav");
[noise, Fs_noise] = audioread("noise.wav");

% Add noise to the speech signal.
Noised = noise + speech;


%sound(noised_speech, Fs);


% get_time_domain
[x1_speech, y1_speech] = get_time_domain(speech, Fs);
[x1_Noised, y1_Noised] = get_time_domain(Noised, Fs);


% get_frequency_domain
[x2_speech, y2_speech] = get_frequency_domain(speech, Fs);
[x2_Noised, y2_Noised] = get_frequency_domain(Noised, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs.
subplot(1,1,1)
subplot(4, 1, 1);
plot(x1_speech, y1_speech), 
title("Original's Time Domain")
xlabel("Time(second)")

subplot(4, 1, 2);
plot(x1_Noised, y1_Noised)
title("Noised's Time Domain")
xlabel("Time(second)")

subplot(4, 1, 3);
plot(x2_speech, y2_speech)
title("Original's Frequency Domain")
xlabel("Frequency(Hz)")

subplot(4, 1, 4);
plot(x2_Noised, y2_Noised)
title("Noised's Frequency Domain")
xlabel("Frequency(Hz)")

% set Coefficients
Aplha = 0.2;
T0 = 1;
N0 = T0 * Fs;

% bulid a empty container for the new echoed sound
Echoed = zeros(size(Noised, 1) + N0, 1);

% add the echo
Echoed(N0 + 1 : end) = Aplha * (Noised);

% add the original
Echoed(1:length(Noised)) = Echoed(1:length(Noised)) + Noised;


%sound(echoed_speech, Fs);


% get_time_domain
[x1_Echoed, y1_Echoed] = get_time_domain(Echoed, Fs);

% get_frequency_domain
[x2_Echoed, y2_Echoed] = get_frequency_domain(Echoed, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs.
subplot(1,1,1);
subplot(2, 1, 1);
plot(x1_Echoed, y1_Echoed), 
title("Echoed's Time Domain"),
xlabel("Time(second)")

subplot(2, 1, 2);
plot(x2_Echoed, y2_Echoed)
title("Echoed's Frequency Domain")
xlabel("Frequency(Hz)")

b = 1;
a = [b, zeros(1,N0 - 1), Aplha];

DeEchoed = filter(b, a, Echoed);


%sound(Echoed, Fs);


% get_time_domain
[x1_DeEchoed, y1_DeEchoed] = get_time_domain(DeEchoed, Fs);

% get_frequency_domain
[x2_DeEchoed, y2_DeEchoed] = get_frequency_domain(DeEchoed, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs.
subplot(1,1,1);
subplot(2, 1, 1);
plot(x1_Echoed, y1_Echoed), 
title("Echoed's Time Domain"),
xlabel("Time(second)")

subplot(2, 1, 2)
plot(x1_DeEchoed, y1_DeEchoed)
title("DeEchoed's Time Domain"),
xlabel("Time(second)")

% declare the filter type you used and briefly explain the design parameters you choose 

Hd = noise_cancellation_filter;  
% Tpye = lowpass
% Fpass = 7900
% Fstop = 8000
% Apass = 1
% Astop = 200
% go to the "My fucntions" at the EOF for the complete details 

Denoised = filter(Hd, DeEchoed);


sound(Denoised, Fs)


% code from Tutorial
Hd = noise_cancellation_filter; % load the filter (correspond to the filename)
[H,w]=freqz(Hd); % use funciton freqz to plot the magnitude response of lowpass filter 
dbH=20*log10(abs(H)/max(abs(H))); % set y-axis in dB 


% get_time_domain
[x1_Denoised, y1_Denoised] = get_time_domain(Denoised, Fs);

% get_frequency_domain
[x2_Denoised, y2_Denoised] = get_frequency_domain(Denoised, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs
subplot(1,1,1)
subplot(5, 1, 1)
plot(w * Fs/(2 * pi), dbH, 'b'); 
axis([0 Fs/2 -250 25]); %Set the display range of the axis
title('Magnitude response of lowpass filter/dB');
xlabel('f/Hz');ylabel('Magnitude/dB')

subplot(5, 1, 2)
plot(x1_DeEchoed, y1_DeEchoed)
title("DeEchoed's Time Domain")
xlabel("Time(second)")

subplot(5, 1, 3)
plot(x1_Denoised, y1_Denoised)
title("Denoised's Time Domain")
xlabel("Time(second)")

subplot(5, 1, 4)
plot(x2_DeEchoed, y2_DeEchoed)
title("DeEchoed's Frequency Domain")
xlabel("Frequency(Hz)")

subplot(5, 1, 5)
plot(x2_Denoised, y2_Denoised)
title("Denoised's Frequency Domain")
xlabel("Frequency(Hz)")

clear

[music, Fs] = audioread("handel.wav");

% get_time_domain
[x1_spliced, y1_spliced] = get_time_domain(music, Fs);

% get_frequency_domain
[x2_music, y2_music] = get_frequency_domain(music, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs
subplot(1,1,1);
subplot(2, 1, 1);
plot(x1_spliced, y1_spliced)
title("Music's Time Domain")
xlabel("Time(second)")

subplot(2, 1, 2);
plot(x2_music, y2_music)
title("Music's Frequency Domain")
xlabel("Frequency(Hz)")


% Since 8 filters are quite many, I'm not going to show their source code 
% in this PDF


% filter 8 bands
slice(:,1) = filter(fir32, music);
slice(:,2) = filter(fir64, music);
slice(:,3) = filter(fir125, music);
slice(:,4) = filter(fir250, music);
slice(:,5) = filter(fir500, music);
slice(:,6) = filter(fir1000, music);
slice(:,7) = filter(fir2000, music);
slice(:,8) = filter(fir4000, music);


% spliced 8 bands back
spliced = zeros(length(music),1);
for i = 1:8 
    spliced = spliced + slice(:,i);
end


%sound(spliced, Fs)
%sound(music, Fs)


% get_frequency_domain
[x2_music, y2_music] = get_frequency_domain(music, Fs);
[x2_spliced, y2_spliced] = get_frequency_domain(spliced, Fs);

% get the difference
x_difference = x2_music;
y_difference = y2_music - y2_spliced;


% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs
subplot(1,1,1);
plot(x_difference, y_difference)
title("Difference in Frequency Domain")
xlabel("Frequency(Hz)")

% set the weights
e(1) = -3;  % 32Hz
e(2) = -3;  % 64Hz
e(3) = 0;   % 125Hz
e(4) = 0;   % 250Hz
e(5) = 4;   % 500Hz
e(6) = -5;  % 1KHz
e(7) = 5;   % 2KHz
e(8) = 0;   % 4KHz


% spliced 8 bands back
equalized = zeros(length(music),1);
for i = 1:8 
    equalized_slice(:,i) = slice(:,i) .* 10^(e(i)/20);
    equalized = equalized + equalized_slice(:,i);
end


%sound(equalized, Fs)


audiowrite("equalized_handle.wav", equalized, Fs);


% get_frequency_domain
[x2_equalized, y2_equalized] = get_frequency_domain(equalized, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs
subplot(1, 1, 1);
plot(x2_equalized, y2_equalized)
title("Equalized's Frequency Domain")
xlabel("Frequency(Hz)")


clear

[before, Fs] = audioread("handel.wav");


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% downsample
p = 7200;
q = Fs;

y = resample(before, p, q);
stretched_y = stretchAudio(y, p / q);

%sound(stretched_y, Fs)
%pause(9)


% padding(recover the downsampled audio)
l = length(y);

x = 1: 1: l; 
xi = 1: (p / q): l;
y = interp1(x, y, xi);

%fsound(y, Fs)
%pause(9)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% upsample !(gender transform)!
p = 9400;
q = Fs;

after = resample(before, p, q);
stretched_after = stretchAudio(after, p / q);

%sound(stretched_after, Fs)
%pause(9)


% drop out weak signals(recover the upsampled audio)
l = length(after);
    
x = 1: 1: l; 
xi = 1: (p / q): l;
z = interp1(x, after, xi);

%sound(z, Fs)
%pause(9)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% get_time_domain
[x1_before, y1_before] = get_time_domain(before, Fs);
[x1_after, y1_after] = get_time_domain(stretched_after, Fs);


% get_frequency_domain
[x2_before, y2_before] = get_frequency_domain(before, Fs);
[x2_after, y2_after] = get_frequency_domain(stretched_after, Fs);

% go to the "My fucntions" at the EOF for the source code of these two functions 


% show the graphs.
subplot(1,1,1)
subplot(4, 1, 1);
plot(x1_before, y1_before), 
title("Before's Time Domain")
xlabel("Time(second)")

subplot(4, 1, 2);
plot(x1_after, y1_after)
title("After's Time Domain")
xlabel("Time(second)")

subplot(4, 1, 3);
plot(x2_before, y2_before)
title("Before's Frequency Domain")
xlabel("Frequency(Hz)")

subplot(4, 1, 4);
plot(x2_after, y2_after)
title("After's Frequency Domain")
xlabel("Frequency(Hz)")