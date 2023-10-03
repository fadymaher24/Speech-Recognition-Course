# Audio processing basics
# Audio Formats
# Signal parameters
# wave module
#  plot waveform
# microphone recorded
# load mp3

# Audio file formats
# .mp3 lossy compression (loss the data)
# .flac compress but we can go to original data easily
# .wav the best and largest(CD Audio Quality)

import wave

# Audio Signal parameters
# number of channels
# sample width
# framerate/sample_rate 44,100 Hz
# number of frames
# values of a frame

obj = wave.open('audio_files/down_to_cases.wav', 'r')
print('Number of channels: ', obj.getnchannels())
print('Sample width: ', obj.getsampwidth())
print('Frame rate: ', obj.getframerate())
print('Number of frames: ', obj.getnframes())
print('Parameters: ', obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print('Audio length: ', t_audio, 's')

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))

obj.close()


obj_new = wave.open('audio_files/down_to_cases_new.wav', 'wb')
obj_new.setnchannels(1)
obj_new.setsampwidth(1)
obj_new.setframerate(11025.0)

obj_new.writeframes(frames)

obj_new.close()