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
