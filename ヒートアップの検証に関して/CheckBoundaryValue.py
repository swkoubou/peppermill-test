#coding:utf-8

import os
import PowerSpectrumPloter

#スペクトルを取得する関数
def PowerSpectrumProcessor(filename):

    #音声ファイルを開く
    #wf = wave.open(filename , "r")
    print filename


if __name__ == "__main__":
    name = os.listdir('Voices');
    normal = 0
    angry = 0

    while(1):

        #判定をしたいファイルの選択
        print "FileName?"
        filename = raw_input()

        #もし入力したファイル名が存在したら，ファイルに関する処理をする
        for index in range(0,len(name)):
            if(filename == name[index]):
                print("File is found");
                os.chdir('Voices/' + filename)

                #ディレクトリ内の音声ファイルを取得・処理する
                for i in range(0, len(os.listdir(os.getcwd()))):
                    filename = os.listdir(os.getcwd())[i]

                    #ヒートアップ検知
                    flag = PowerSpectrumPloter.func(filename)

                    #通常時であればnormalを，
                    # 興奮時であればangry変数をインクリメントする
                    if(flag):
                        normal += 1
                    else:
                        angry += 1

                #結果を出力する
                print "Normal : " + str(normal)
                print "Angry  : " + str(angry)


                #再度ディレクトリを移動する
                os.chdir('../..')
                print os.getcwd()

        #リダイレクト用の終了処理
        if(normal + angry == 60):
            break