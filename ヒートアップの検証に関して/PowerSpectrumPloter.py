#coding:utf-8

import wave
import numpy
import scipy.fftpack
from pylab import *

def func(pathName):
    #フーリエ変換したい音データを開く
    filename = pathName;
    wf = wave.open(filename , "r")
    
    #開いた音声ファイルからサンプリング周波数を取得する
    fs = wf.getframerate()

    #オーディオフレーム数(ビットフレーム数)を文字変換して取得
    x = wf.readframes(wf.getnframes())

    #ビットレートをint型の一次元配列として格納する
    x = frombuffer(x , dtype = "int16") / 32768.0

    #wavファイルを閉じる
    wf.close()




    start = 0   #サンプリングする開始位置
    N = 2048     #FFTのサンプル数

    #ビットレートの一次元配列をFFT変換した時の値(解)を取得する(実数と複素数で構成される)
    X = scipy.fftpack.fft(x[start:start + N])

    #サンプリング周波数を取得する
    freqList = numpy.fft.fftfreq(N , d = 1.0 / fs)



    #周波数スペクトルの値を取得して対数に変換
    Adft = numpy.abs(X)
    AdftLog = 20 * numpy.log10(Adft)

    #パワースペクトルの値を取得して対数に変換
    Pdft = numpy.abs(X) ** 2
    PdftLog = 10 * numpy.log10(Pdft)


    #ケプストラム分析
    Acps = numpy.real(numpy.fft.ifft((AdftLog))) #振幅スペクトル
    Pcps = numpy.real(numpy.fft.ifft((PdftLog))) #パワースペクトル

    #ケプストラム次数
    cepCoef = 20
    AcpsLif = numpy.array(Acps)  #振幅スペクトル
    PcpsLif = numpy.array(Pcps)  #パワースペクトル

    #高周波数成分を除去
    AcpsLif[cepCoef:len(AcpsLif) - cepCoef + 1] = 0   #振幅スペクトル
    PcpsLif[cepCoef:len(PcpsLif) - cepCoef + 1] = 0   #パワースペクトル

    #ケプストラムをフーリエ変換し直してスペクトルに変換し直す
    AdftSpc = numpy.fft.fft(AcpsLif , N)    #振幅スペクトル
    PdftSpc = numpy.fft.fft(PcpsLif , N)    #パワースペクトル


    #ケプストラム分析の近似直線を描画
    X = freqList[0:N/2]
    Y = PdftSpc[0:N/2]

    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]


    #終端のケプストラムの値を直線で繋ぐ
    X = freqList[0:N/2]
    Y = PdftSpc[0:N/2]
    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]

    #傾きの値を分かりやすい数値に変換
    a = float(a)
    a = a * 10000

    #切片の値を分かりやすい数値に変換
    b = int(b)
    b = abs(b)

    # print "slope : " + str(a)
    # print "slice : " + str(b)

    print str(abs(a)) + ","
    print str(b) + ","

    #Value = 4.58
    Value = 9.979034

    #ヒートアップ検知
    if(abs(a) > Value):
        print "Normal,"
        return True
    else:
        print "Angry,"
        return False

    # show()

if __name__ == "__main__":
    func();