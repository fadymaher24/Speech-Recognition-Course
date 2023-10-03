from pydub import AudioSegment

# audio = AudioSegment.from_mp3("test.mp3")
audio = AudioSegment.from_wav("audio_files/recorded_audio.wav")

# increase volume by 6 dB
audio = audio + 6

# repeat the audio two times
audio = audio * 2

# fade in and fade out by 2 seconds
audio = audio.fade_in(2000).fade_out(2000)

# save the result
audio.export("audio_files/mashup.mp3", format="mp3")

audio2 = AudioSegment.from_mp3("audio_files/mashup.mp3")
print("done")
