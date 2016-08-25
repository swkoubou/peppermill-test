# peppermill-test
PEPPER_MILL プロジェクトのテスト用ファイルとかを突っ込むプロジェクト

## Memory
Prefix: PepperMill/MeetingSupport/

|Key|Type|Example|Description|
|-----|-------|-----------|---------------|
|State|String|"idle", "running", "sleep", "error"|アプリの状態|
|TimeKeeper/State|String|"idle", "running", "pause", "stopped", "error"|タイムキーパーの状態|
|TimeKeeper/TimeOver|None|None|タイムオーバー時に発火|
|TimeKeeper/RemainingTime|Number|52|残り時間(秒)|
|TimeKeeper/SettingTime|Number|120|設定時間(秒)|
|HeatUp/State|String|"idle", "running", "sleep", "error"|ヒートアップアプリの状態|
|HeatUp/Burst|None|None|ヒートアップ時に発火|
|HeatUp/Params|Mixed|{...}|Tablet上のヒートアップ状態の可視化用|

## PEPPER_MILLリポジトリ概要
### 現行リポジトリ
- peppermill-test: 本リポジトリ。テスト用ファイル等を格納する。
- peppermill-timekeeper-android: タイムキーパーアプリ
- peppermill-heatupAPI: 興奮検知のためのAPI。burst-ditectorに依存。
- peppermill-burst-ditector: 興奮検知の本体。heatupAPIに被依存。
- peppermill-wedding-atraction: 結婚式の受付アプリ
- pepperimll-wedding-ringboy: 結婚式のリングボーイアプリ

### 本リポジトリに統合されたもの
- heatup-animation: 興奮時のアニメーションのテスト
- heatup-post: Androidアプリ(Pepper)からheatupAPIを利用するテスト
- HeatUpChecker: 興奮検知のテスト
- meetingsupport: choregrapheとタブレットの通信テスト
- MMSE_STSA: ノイズ除去スクリプト
- record_test: Androidアプリによる録音のテスト
- recording_audio: Pythonによる録音のテスト
- test-depth: Pepperの深度カメラ及びRGBの生データ取得テスト
- timekeeper-choregraphe: choregraphe時代のtimekeeperアプリ
