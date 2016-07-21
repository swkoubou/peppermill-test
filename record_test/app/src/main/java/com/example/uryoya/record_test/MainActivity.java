package com.example.uryoya.record_test;
import android.app.Activity;
import android.content.Context;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Environment;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.aldebaran.qi.QiCallback;
import com.aldebaran.qi.sdk.Qi;
import com.aldebaran.qi.sdk.object.interaction.Say;

import java.io.IOException;
import java.io.StringReader;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "MainActivity";

    private Handler _handler = new Handler();
    private Runnable stopRecordAfter5sec;

    private MediaPlayer   mPlayer = null;
    private MediaRecorder mRecorder = null;
    private static String mFileName = null;
    private static final String LOG_TAG = "AudioRecordTest";




    public MainActivity() {
        //mFileName = Environment.getExternalStorageDirectory().getAbsolutePath();
        //mFileName = getApplicationContext().getFilesDir().getAbsolutePath();
        mFileName = "/data/data/com.example.uryoya.record_test";
        mFileName += "/audiorecordtest.3gp";
        Log.d(">>>", mFileName);
    }


    private void onRecord(boolean start) {
        if (start) {
            startRecording();
        } else {
            stopRecording();
        }
    }

    private void onPlay(boolean start) {
        if (start) {
            startPlaying();
        } else {
            stopPlaying();
        }
    }

    private void startPlaying() {
        mPlayer = new MediaPlayer();
        try {
            mPlayer.setDataSource(mFileName);
            mPlayer.prepare();
            mPlayer.start();
        } catch (IOException e) {
            Log.e(LOG_TAG, "prepare() failed");
        }
    }

    private void stopPlaying() {
        mPlayer.release();
        mPlayer = null;
    }

    private void startRecording() {
        //mFileName = Environment.getExternalStorageDirectory().getAbsolutePath();
        //mFileName += "/audiorecordtest.3gp";
        mRecorder = new MediaRecorder();
        mRecorder.setAudioSource(MediaRecorder.AudioSource.MIC);
        mRecorder.setOutputFormat(MediaRecorder.OutputFormat.THREE_GPP);
        mRecorder.setOutputFile(mFileName);
        mRecorder.setAudioEncoder(MediaRecorder.AudioEncoder.AMR_NB);

        try {
            mRecorder.prepare();
        } catch (IOException e) {
            Log.e(LOG_TAG, "prepare() failed");
            Log.e(LOG_TAG, e.toString());
        }

        mRecorder.start();
    }

    private void stopRecording() {
        mRecorder.stop();
        mRecorder.release();
        mRecorder = null;
    }



    @Override
    public void onCreate(Bundle icicle) {
        super.onCreate(icicle);
        Log.d(LOG_TAG, "program start");
        Log.d(LOG_TAG, mFileName);

        onRecord(true);
        Log.d(LOG_TAG, "Now Recording...");
        stopRecordAfter5sec = new Runnable() {
            @Override
            public void run() {
                onRecord(false);
                Log.d(LOG_TAG, "Stop Recording!");
                Log.d(LOG_TAG, "Start Playing");
                onPlay(true);
                Log.d(LOG_TAG, "Stop Playing");
            }
        };
        _handler.postDelayed(stopRecordAfter5sec, 5000);



    }

}