package com.example.uryoya.record_test;

import android.content.Context;
import android.media.MediaPlayer;
import android.media.MediaRecorder;
import android.os.Bundle;
import android.os.Handler;
import android.os.MemoryFile;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.github.hiteshsondhi88.libffmpeg.FFmpeg;
import com.github.hiteshsondhi88.libffmpeg.FFmpegExecuteResponseHandler;
import com.github.hiteshsondhi88.libffmpeg.LoadBinaryResponseHandler;
import com.github.hiteshsondhi88.libffmpeg.exceptions.FFmpegNotSupportedException;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {
    private Handler _handler = new Handler();
    private Runnable stopRecordAfter5sec;

    private MediaPlayer   mPlayer = null;
    private MediaRecorder mRecorder = null;
    private static String mFileName = null;
    private static final String LOG_TAG = "AudioRecordTest";
    private static final String wavfilename = "audiorecordtest.wav";


    public MainActivity() {
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
            Log.e(LOG_TAG, e.getMessage());
        }
    }

    private void stopPlaying() {
        mPlayer.release();
        mPlayer = null;
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
            Log.e(LOG_TAG, "prepare() failed");
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


        //convert 3gp to wav

        ConvertWAV convertWAV = new ConvertWAV(mFileName);

    }

}