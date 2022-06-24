import wave

import pyaudio

FRAMES_FOR_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNEL = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    frames_per_buffer=FRAMES_FOR_BUFFER,
    format=FORMAT,
    channels=CHANNEL,
    rate= RATE,
    input= True,
)

print("start recording")

seconds = 5
frames = []

for i in range(0, int(RATE/FRAMES_FOR_BUFFER*seconds)):
    data = stream.read(FRAMES_FOR_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj = wave.open("output.wav","wb")
obj.setnchannels(CHANNEL)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
