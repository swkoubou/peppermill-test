#coding:utf-8

import wave
import numpy
import scipy.fftpack
from pylab import *

if __name__ == "__main__":
    #フーリエ変換したい音データを開く
    filename = raw_input()
    filename = "output_files/" + filename
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
    Adft = numpy.array([x for x in Adft])
    print(Adft)
    AdftLog = 20 * numpy.log10(Adft)

    #パワースペクトルの値を取得して対数に変換
    Pdft = numpy.abs(X) ** 2
    Pdft = numpy.array([x for x in Pdft])
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



    #波形を描画
    figure(figsize=(12,9))
    subplot(221)
    title("Wave")
    #得られた値の描画
    plot(range(start,start + N) , x[start:start + N])
    #軸ラベル名の指定
    xlabel("time[s]")
    ylabel("amplitute")
    xlim(0, 2000)

    #振幅スペクトルを描画
    subplot(222)
    title("AmpSpec")
    #スペクトル領域を描画
    plot(freqList[0:N/2], AdftLog[0:N/2])
    #分離処理をしたスペクトル包絡を描画
    plot(freqList[0:N/2], AdftSpc[0:N/2], 'r', linewidth = 2)
    xlabel("frequency [Hz]")
    ylabel("amplitude spectrum")
    xlim(0, 5000)

    # パワースペクトルを描画
    subplot(223)
    title("PowSpec")
    #スペクトル領域を描画
    plot(freqList[0:N/2], PdftLog[0:N/2])
    #分離処理をしたスペクトル包絡を描画
    plot(freqList[0:N/2], PdftSpc[0:N/2], 'r', linewidth = 2)
    #終端のケプストラムの値を直線で繋ぐ(ボツ案)
    #plot([0, 5000], [PdftSpc[0], PdftSpc[N/2]], 'yo-', lineWidth = 3)

    #ケプストラム分析の近似直線を描画
    X = freqList[0:N/2]
    Y = PdftSpc[0:N/2]

    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]
    plt.plot(X,(a*X+b),"g--")

    #グラフの概要に関する内容
    xlabel("frequency [Hz]")
    ylabel("power spectrum")
    xlim(0, 5000)



    #ケプストラム分析の近似曲線をピックアップしたもの
    figure(figsize=(12,9))
    title("PowSpec")
    #スペクトル領域を描画
    plot(freqList[0:N/2], PdftLog[0:N/2])
    #分離処理をしたスペクトル包絡を描画
    plot(freqList[0:N/2], PdftSpc[0:N/2], 'r', linewidth = 2)
    #終端のケプストラムの値を直線で繋ぐ
    X = freqList[0:N/2]
    Y = PdftSpc[0:N/2]
    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]
    plt.plot(X,(a*X+b), "y", linewidth = 2)
    #グラフの概要に関する内容
    xlabel("frequency [Hz]")
    ylabel("power spectrum")
    xlim(0, 20000)

    #傾きの値を分かりやすい数値に変換
    if(math.isnan(a)):
        a = NaN
    else:
        a = float(a)
        a = a * 10000

    #切片の値を分かりやすい数値に変換
    if(math.isnan(b)):
        b = NaN
    else:
        b = int(b)
        b = abs(b)

    print(a)
    print(b)

    #ヒートアップ検知
    if(abs(a) > 4.58):
        print "Normal"
    else:
        print "Angry"

    show()
