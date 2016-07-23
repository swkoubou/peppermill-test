package com.example.uryoya.record_test;

import android.media.MediaRecorder;
import android.os.Handler;
import android.util.Log;

import java.io.IOException;


public class Recorder {
    private static final String LOG_TAG = "Recorder";

    private MediaRecorder mRecorder = null;
    private String mFileName = null;

    public Recorder() {
        mFileName = "/data/data/com.example.uryoya.record_test";
        mFileName += "/audio_record.3gp";
    }

    public void recording(int seconds) {
        Handler handler = new Handler();
        Runnable runUntilWaitTime;

        startRecording();
        Log.d(LOG_TAG, "Recording now...");
        runUntilWaitTime = new Runnable() {
            @Override
            public void run() {
                stopRecording();
                Log.d(LOG_TAG, "Stop Recording...");
            }
        };
        handler.postDelayed(runUntilWaitTime, seconds * 1000);
    }

    private void startRecording() {
        mRecorder = new MediaRecorder();
        mRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        mRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        mRecorder.setOutputFile(mFileName);
        mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);

        try {
            mRecorder.prepare();
        } catch (IOException e) {
            Log.e(LOG_TAG, e.getMessage());
        }

        try {
            mRecorder.start();
        } catch (IllegalStateException e) {
            Log.e(LOG_TAG, e.getMessage());
        }
    }

    private void stopRecording() {
        mRecorder.stop();
        mRecorder.release();
        mRecorder = null;
    }
}
