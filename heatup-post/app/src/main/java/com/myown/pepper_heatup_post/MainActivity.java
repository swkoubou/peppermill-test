package com.myown.pepper_heatup_post;

import android.content.Context;
import android.content.res.AssetFileDescriptor;
import android.content.res.AssetManager;
import android.os.AsyncTask;
import android.os.Environment;
import android.os.Handler;
import android.support.v4.content.res.TypedArrayUtils;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.view.ActionMode;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.net.http.*;
import android.widget.DialerFilter;
import android.widget.Toast;

import com.aldebaran.qi.sdk.object.interaction.Say;
import com.squareup.okhttp.Headers;
import com.squareup.okhttp.MediaType;
import com.squareup.okhttp.MultipartBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;


import org.json.JSONObject;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

	private Button btn = null;

	private final String server_url = "http://10.0.2.2:5000/analyze";
	private final String file_name = "sample.wav";

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);

		btn = (Button)findViewById(R.id.send_request_button);
		btn.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View view) {
				new Thread(new Runnable() {
					@Override
					public void run() {
						//do post
						HeatUpPost heatUpPost = new HeatUpPost(server_url);
						String response_string = heatUpPost.uploadFile(MainActivity.this, file_name);
						if(response_string != null){
							Log.d("server response : ", " " + response_string);
						}else {
							Log.d("server response : ", "server response is null");
						}
					}
				}).start();
			}
		});

	}


}
