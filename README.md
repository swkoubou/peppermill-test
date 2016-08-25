# peppermill-test
PEPPER_MILL プロジェクトのテスト用ファイルとかを突っ込むプロジェクト

## PEPPER_MILLリポジトリ概要
### 現行リポジトリ
| リポジトリ名									|	概要																					|
|-------------------------------|-----------------------------------------------|
| peppermill-test								| 本リポジトリ。テスト用ファイル等を格納する。	|
| peppermill-timekeeper-android	| タイムキーパーアプリ													|
| peppermill-heatupAPI					| 興奮検知のためのAPI。burst-ditectorに依存。		|
| peppermill-burst-ditector			| 興奮検知の本体。heatupAPIに被依存。						|
| peppermill-wedding-atraction	| 結婚式の受付アプリ														|
| pepperimll-wedding-ringboy		| 結婚式のリングボーイアプリ										|

### 本リポジトリに統合されたもの
| ディレクトリ名				|	概要																								|
|-----------------------|-----------------------------------------------------|
|heatup-animation				| 興奮時のアニメーションのテスト											|
|heatup-post						| Androidアプリ(Pepper)からheatupAPIを利用するテスト	|
|HeatUpChecker					| 興奮検知のテスト																		|
|meetingsupport					| choregrapheとタブレットの通信テスト									|
|MMSE_STSA							| ノイズ除去スクリプト																|
|record_test						| Androidアプリによる録音のテスト											|
|recording_audio				| Pythonによる録音のテスト														|
|test-depth							| Pepperの深度カメラ及びRGBの生データ取得テスト				|
|timekeeper-choregraphe	| choregraphe時代のtimekeeperアプリ										|
