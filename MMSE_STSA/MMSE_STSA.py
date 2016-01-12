# -*- coding: utf-8 -*-

import wave
import sys
import os
import math
from glob import glob
import scipy as sp
import scipy.special as spc
import numpy as np
np.seterr(divide='ignore', invalid='ignore')

WINSIZE=1024

noisefile='noise.wav'
source='src'
dist='dist'

def read_signal(filename, winsize):
    wf=wave.open(filename,'rb')
    n=wf.getnframes()
    str=wf.readframes(n)
    params = ((wf.getnchannels(), wf.getsampwidth(),
               wf.getframerate(), wf.getnframes(),
               wf.getcomptype(), wf.getcompname()))
    siglen=((int )(len(str)/2/winsize) + 1) * winsize
    signal=sp.zeros(siglen, sp.int16)
    signal[0:len(str)/2] = sp.fromstring(str,sp.int16)
    return [signal, params]

def get_frame(signal, winsize, no):
    shift=winsize/2
    start=no*shift
    end = start+winsize
    return signal[start:end]

def add_signal(signal, frame, winsize, no ):
    shift=winsize/2
    start=no*shift
    end=start+winsize
    signal[start:end] = signal[start:end] + frame

def write_signal(filename, params ,signal):
    wf=wave.open(filename,'wb')
    wf.setparams(params)
    s=sp.int16(signal).tostring()
    wf.writeframes(s)

def calc_noise(filepath):
    noise_sum=None
    signal, params = read_signal(filepath, WINSIZE)
    nf = len(signal)/(WINSIZE/2) - 1
    noise_sum=sp.zeros(WINSIZE,sp.float32)
    window = sp.hanning(WINSIZE)
    for no in xrange(nf):
        y = get_frame(signal, WINSIZE, no)
        Y = sp.fft(y*window)
        Yr = sp.absolute(Y)
        Yp = sp.angle(Y)
        if ( no < 20 ):
            noise_sum = noise_sum + Yr**2
        else:
            break
    return noise_sum

def mmse_stsa(infile, outfile, noise_sum):
    signal, params = read_signal(infile, WINSIZE)
    nf = len(signal)/(WINSIZE/2) - 1
    sig_out=sp.zeros(len(signal),sp.float32)

    G = sp.ones(WINSIZE)
    prevGamma = G
    alpha = 0.98
    window = sp.hanning(WINSIZE)
    gamma15=spc.gamma(1.5)
    lambdaD = noise_sum / 5.0
    percentage = 0
    for no in xrange(nf):
        p = int(math.floor(1. * no / nf * 100))
        if (p > percentage):
            percentage = p
            print "{}%".format(p),

        y = get_frame(signal, WINSIZE, no)
        Y = sp.fft(y*window)
        Yr = sp.absolute(Y)
        Yp = sp.angle(Y)
        gamma = Yr**2/lambdaD
        xi = alpha * G**2 * prevGamma + (1-alpha)*sp.maximum(gamma-1, 0)
        prevGamma = gamma
        nu = gamma * xi / (1+xi)
        G = (gamma15 * sp.sqrt(nu) / gamma ) * sp.exp(-nu/2) * ((1+nu)*spc.i0(nu/2)+nu*spc.i1(nu/2))
        idx = sp.isnan(G) + sp.isinf(G)
        G[idx] = xi[idx] / (xi[idx] + 1)
        Yr = G * Yr
        Y = Yr * sp.exp(Yp*1j)
        y_o = sp.real(sp.ifft(Y))
        add_signal(sig_out, y_o, WINSIZE, no)
    
    write_signal(outfile, params, sig_out)

if __name__ == '__main__':
    print "create noise sum from {}...".format(noisefile)
    noise_sum = calc_noise(noisefile)
    print "done"

    for inpath in glob("{}/*.wav".format(source)):
        infilename = os.path.basename(inpath)
        outfilename = infilename.replace(".wav", "_filtered.wav")
        outpath = os.path.join(dist, outfilename)
        print "filter out noise from {} to {}...".format(infilename, outfilename)
        mmse_stsa(inpath, outpath, noise_sum)
        print "done"

