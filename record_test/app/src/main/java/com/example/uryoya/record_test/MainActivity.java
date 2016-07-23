package com.example.uryoya.record_test;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private MediaPlayer   mPlayer = null;
    private static String mFileName = "/data/data/com.example.uryoya.record_test/audiorecordtest.3gp";
    private static final String LOG_TAG = "AudioRecordTest";

    private void startPlaying() {
        mPlayer = new MediaPlayer();
        try {
            mPlayer.setDataSource(mFileName);
            mPlayer.prepare();
            mPlayer.start();
        } catch (IOException e) {
            Log.e(LOG_TAG, e.getMessage());
        }
    }

    private void stopPlaying() {
        mPlayer.release();
        mPlayer = null;
    }

    @Override
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);
        Log.d(LOG_TAG, "program start");
        Log.d(LOG_TAG, mFileName);

        Recorder recorder = new Recorder(mFileName);
        recorder.recording(10, new Runnable() {
            @Override
            public void run() {
                startPlaying();
            }
        });
    }

}
