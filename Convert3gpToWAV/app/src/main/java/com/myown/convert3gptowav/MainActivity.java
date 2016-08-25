package com.myown.convert3gptowav;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		String in_filePath = "/data/data/com.myown.convert3gptowav/audiorecordtest.3gp";
		String out_filePath = "/data/data/com.myown.convert3gptowav/audiorecordtest.wav";

		Convert3gpToWAV convert3gpToWAV = new Convert3gpToWAV(MainActivity.this);
		convert3gpToWAV.convert(in_filePath, out_filePath, new Runnable() {
			@Override
			public void run() {

			}
		});

	}

}
