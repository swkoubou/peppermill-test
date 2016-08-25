# coding: utf-8

import wave
import pyaudio
from pylab import *

def PlayWaveFile(wf):
    #　open stream　#
    audio = pyaudio.PyAudio()
    stream = audio.open(format = audio.get_format_from_width(wf.getsampwidth()),
                        channels = wf.getnchannels(),
                        rate = wf.getframerate(),
                        output = True)

    #　play the wave file　#
    CHUNK = 1024
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(CHUNK)

def PlotWaveFile(wf):
    #　get the information for plot　#
    buffer = wf.readframes(wf.getnframes())
    data = frombuffer(buffer, dtype="int16")

    #　plot the wave　#
    plot(data)
    #ion()#モードの変更#
    show()

if __name__ == '__main__':

    #　open the wave file　#
    print "Please enter the file name of the wave form"
    wfname = raw_input()
    wf1 = wave.open(wfname , "r")
    wf2 = wave.open(wfname , "r")

    #　open the wave file　#
    PlayWaveFile(wf1)

    #　plot the wave　#
    PlotWaveFile(wf2)
