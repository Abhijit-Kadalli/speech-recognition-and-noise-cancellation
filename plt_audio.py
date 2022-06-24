import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("output.wav", "rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_sample/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype= np.int32)

times = np.linspace(0,t_audio,num= n_sample)

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal")
plt.xlabel("time")
plt.xlim(0, t_audio)
plt.show()