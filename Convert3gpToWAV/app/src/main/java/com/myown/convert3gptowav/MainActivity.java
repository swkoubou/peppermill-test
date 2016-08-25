package com.myown.convert3gptowav;

import android.app.Application;
import android.content.res.AssetManager;
import android.net.Uri;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class MainActivity extends AppCompatActivity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		String in_filePath = "/data/data/com.myown.convert3gptowav/audiorecordtest.3gp";
		String out_filePath = "/data/data/com.myown.convert3gptowav/audiorecordtest.wav";
		Handler handler = new Handler();

		Convert3gpToWAV convert3gpToWAV = new Convert3gpToWAV(MainActivity.this);
		convert3gpToWAV.convert(in_filePath, out_filePath, new Runnable() {
			@Override
			public void run() {

			}
		});

	}

}
