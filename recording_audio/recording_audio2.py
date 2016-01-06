# -*- coding: utf-8 -*-
import pyaudio
import wave
import time

chunk = 1024
pyaudio_format = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SAMPLING_TIME = 10

p = pyaudio.PyAudio()

# microphone device number
input_device_index = 5

# get data at microphone
stream = p.open(format = pyaudio_format,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

def wave_save(frame, filename):
    data = ''.join(frame)
    out = wave.open(filename, 'w')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(RATE)
    out.writeframes(data)
    out.close()

count = 1
frame = []
start_time = time.time()
try:
    while True:
        data = stream.read(chunk)
        frame.append(data)
        if (time.time() - start_time) >= (SAMPLING_TIME * count):
            print len(frame)
            filename = "{}.wav".format(count)
            wave_save(frame, filename)
            frame = []
            count += 1
except KeyboardInterrupt:
    print len(frame)
    filename = "{}.wav".format(count)
    wave_save(frame, filename)

stream.close()

p.terminate()
