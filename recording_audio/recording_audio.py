# -*- encoding:utf-8 -*-
"""
動作確認: python3.4+, ubuntu15.10

指定時間録音をする。10分毎にファイルを保存する。
"""
import pyaudio
import wave
import time
from datetime import datetime


# 初期化設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2**11
SAMPLING_TIME = 10 * 60

audio = pyaudio.PyAudio()
frames = []
def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return (None, pyaudio.paContinue)

def wave_save(filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=5,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

print('recoding...')
start_time = time.time()   # 録音開始時間の記録
count = 1
stream.start_stream()
try:
    while True:
        time.sleep(1) # 一秒の待ち時間を作る
        if time.time() >= (start_time + SAMPLING_TIME * count):
            filename = "{0}.wav".format(datetime.now().strftime('%Y%m%d-%H%M%S'))
            wave_save(filename)
            print("saved file : "+filename)
            # init
            frames = []
            count += 1
except KeyboardInterrupt:
    filename = "{0}.wav".format(datetime.now().strftime('%Y%m%d-%H%M%S'))
    wave_save(filename)
    print("saved file : "+filename)

print('end')

stream.stop_stream()
stream.close()
audio.terminate()
