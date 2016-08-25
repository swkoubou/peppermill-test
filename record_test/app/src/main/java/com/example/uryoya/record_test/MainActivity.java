package com.example.uryoya.record_test;

import android.content.Context;
import android.media.MediaPlayer;
import android.os.Bundle;
<<<<<<< HEAD
import android.os.Handler;
import android.os.MemoryFile;
=======
>>>>>>> 77e31f5ba2b220634ccd51798d5ca8732c9c0c2a
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
    private MediaPlayer   mPlayer = null;
    private static String mFileName = "/data/data/com.example.uryoya.record_test/audiorecordtest.3gp";
    private static final String LOG_TAG = "AudioRecordTest";
<<<<<<< HEAD
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
=======
>>>>>>> 77e31f5ba2b220634ccd51798d5ca8732c9c0c2a

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
<<<<<<< HEAD
        };
        _handler.postDelayed(stopRecordAfter5sec, 5000);


        //convert 3gp to wav

        ConvertWAV convertWAV = new ConvertWAV(mFileName);

=======
        });
>>>>>>> 77e31f5ba2b220634ccd51798d5ca8732c9c0c2a
    }

}
