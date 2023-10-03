import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open('audio_files/down_to_cases.wav', 'rb')

sample_freq = obj.getframerate()
num_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

# the length of the signal in seconds
t_audio = num_samples/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# time vector for plotting
# linspace gets zero as the starting point and the end point is the length of the signal
times = np.linspace(0, t_audio, num=num_samples//2)


plt.figure(figsize=(12, 4))
plt.plot(times, signal_array)
plt.title('Audio Signal')
plt.xlabel('Time (s)')
plt.ylabel('Signal wave')
plt.xlim(0, t_audio)
plt.show()