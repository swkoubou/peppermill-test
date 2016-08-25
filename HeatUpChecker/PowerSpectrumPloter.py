#coding:utf-8

import wave
import numpy
import scipy.fftpack
import time
from pylab import *
from datetime import datetime

count = 1
start_time = time.time()
SAMPLING_TIME = 2
preslope = 0
slope = []
limit = []

if __name__ == "__main__":
    try:
        while True:
            if (time.time() - start_time) >= (SAMPLING_TIME * count):
                #フーリエ変換したい音データを開く
                #filename = raw_input()
                #filename = "output_files/" + filename
                filename = "output_files/sample.wav"

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


                #ケプストラム分析の近似曲線をピックアップしたもの
                # figure(figsize=(12,9))
                # title("PowSpec")
                # #スペクトル領域を描画
                # plot(freqList[0:N/2], PdftLog[0:N/2])
                # #分離処理をしたスペクトル包絡を描画
                # plot(freqList[0:N/2], PdftSpc[0:N/2], 'r', linewidth = 2)
                # #終端のケプストラムの値を直線で繋ぐ
                X = freqList[0:N/2]
                Y = PdftSpc[0:N/2]
                A = np.array([X,np.ones(len(X))])
                A = A.T
                a,b = np.linalg.lstsq(A,Y)[0]
                #plt.plot(X,(a*X+b), "g", linewidth = 2)
                # #グラフの概要に関する内容
                # xlabel("frequency [Hz]")
                # ylabel("power spectrum")
                # xlim(0, 20000)

                #傾きの値を分かりやすい数値に変換
                a = float(a)
                a = a * 10000

                slope.append(a)
                limit.append(-4.58)
                # plot(count, a, "-")
                # plot(count, 4.58, "-")

                #切片の値を分かりやすい数値に変換
                b = int(b)
                b = abs(b)

                print(a)
                print(b)

                #ヒートアップ検知
                if(abs(a) > 4.58 and abs(a) >= preslope):
                    print "Normal"

                else:
                    print "Angry"

                #時間のカウント
                count += 1;
                preslope = abs(a)

                if(SAMPLING_TIME * count > 12 ):
                    x = range(0,0+6)
                    plot(x, slope, "ro-")
                    plot(x, limit, "g-")
                    show()
                    break



    except KeyboardInterrupt:
        print "finish"