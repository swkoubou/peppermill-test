package com.myown.convert3gptowav;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		Convert3gpToWAV convert3gpToWAV = new Convert3gpToWAV();
		convert3gpToWAV.convert(MainActivity.this);
	}
}
