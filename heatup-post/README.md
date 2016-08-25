# pepper_mill_heatup_post

1. repositoryをcloneする.  
2. Android Studioでcloneしてきたプロジェクトを開く.  
3. プロジェクトを実行する.  
4. エミュレータが立ち上がったら(アプリの起動を確認したら)terminal or command promptを開く.  
5. 音楽ファイルのあるディレクトリに移動する.  
6. 移動の後  
$ adb push [音楽ファイル名] storage/   
のコマンドを実行する (音楽ファイル名は自分の環境に合わせる)  
もしpushに失敗する場合(Read-Only file systemなど)には以下を参照してください.  
https://tsingdao.wordpress.com/2012/02/16/read-only-file-system/  
7. pushされたことを確認した後、Android Studioからアプリをもう一度実行する.  
8. $python heatup.pyでサーバを起動する(127.0.0.1:5000のURLを表示されたら起動成功)  
9. Androidエミュレータでアプリが起動していることを確認してButtonをクリックする.  
10. Android StudioのLogcatにサーバからのresponseが出力されていることを確認する.  

以下は参考サイト
android emulatorにダミーの音楽ファイルを置くには下記を参照する  
http://qiita.com/t2low/items/cb37cec5f864c4748e14  
  
